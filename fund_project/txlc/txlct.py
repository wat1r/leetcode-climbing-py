import os
import re
import sys
import time
import uuid
from datetime import datetime, timedelta
from typing import Dict, Tuple, Any
from concurrent.futures import ThreadPoolExecutor
from pymongo import MongoClient
import pandas
import requests
import json
import urllib3

# 获取设备id
device_id = str(uuid.uuid1())
print("设备id：", device_id)

# 关掉不安全证书的警告
urllib3.disable_warnings()


# MongoDB 连接信息
host = '219.141.235.67'  # MongoDB 服务器的主机名或 IP 地址
port = 28819  # MongoDB 服务器的端口号
username = 'root'  # MongoDB 用户名
password = 'yQYCqibqif*z3DWK'  # MongoDB 密码
database = 'TXLCT_test'  # 要连接的数据库名称
client = MongoClient(host, port, username=username, password=password)
db = client[database]

INPUT = "input"

COOKIES = {
    "qlskey": "",
    "qluin": "",
}

HEADERS = {
    'Host': 'www.tencentwm.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://www.tencentwm.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
VIP_ENUMERATION = {
    0: "否",
    1: "否",
    2: "是",
    3: "是",
    4: "是",
}






def nb_print(*args, sep=' ', end='\n', file=None):
    # 获取被调用函数在被调用时所处代码行数
    line = sys._getframe().f_back.f_lineno
    # 获取被调用函数所在模块文件名
    file_name = sys._getframe(1).f_code.co_filename
    # sys.stdout.write(f'"{__file__}:{sys._getframe().f_lineno}"    {x}\n')
    args = (str(arg) for arg in args)  # REMIND 防止是数字不能被join
    sys.stdout.write(f'"{file_name}:{line}"  {time.strftime("%H:%M:%S")}  \033[0;94m{"".join(args)}\033[0m\n')  # 36  93 96 94
# print = nb_print


def insert_or_update(table_name: str,data_dict: dict,):
    """
    插入或更新
    :param table_name: MongoDB 集合名
    :param data_dict: 带_id主键的数据
    :return:
    """

    coll = db[table_name]
    # 0 区
    dt0 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    _id = data_dict.get("_id", "")
    if not _id:
        raise Exception("数据存储需要唯一id")
    data_dict['lastCrawlTime'] = dt0
    update_dict = {'$set': data_dict, '$setOnInsert': {'firstCrawlTime': dt0, 'delete_time': 0}}
    return coll.update_one({"_id": _id}, update_dict, upsert=True)

# 搜索接口
def api_source_data(fund_code):
    params = {
        # 'report_platform': 'mp',
        # '_': '55202875',
    }

    data = json.dumps({
        "OutPutType": "JSON",
        "s_key_word": fund_code,
        "i_finish": 1,
        "i_filter_not_sale": 0,
        "s_uin": COOKIES['qluin'],
        "i_account_type": 2,
        "s_seq_no": COOKIES['qluin'].replace("@wx.tenpay.com", "_1697186717603"),
        "st_search_comm_extend_req": {
            "s_abt_traffic_distributed_info": "[{\"graypolicyId\":\"130472\",\"group_name\":\"algorithm\",\"version_type\":\"3\"}]",
            "s_manual_traffic_distributed_info": "",
            "s_scene_arguments": []
        },
        "s_scene_type": "9",
        "i_channel": 1,
        "b_record_history": True,
        # "g_tk": "468001664"
    })

    response = requests.post(
        'https://www.tencentwm.com/fbp/fund/v1/fund.fuapl_search_ao.FuaplSearchAo.FsaSearchResultV2',
        params=params,
        headers=HEADERS,
        cookies=COOKIES,
        data=data,
        verify=False,
    )
    # print(response.text)
    return response.json()


def api_post_list(fund_id, begin: str = "", begin_score: str = "", order: str = 'time') -> dict:
    """
    获得讨论区的列表页
    :param fund_id: 基金id
    :param begin:
    :param begin_score:
    :param order: 排序类型，最新和精华，"最新":'time',"精华":'hot_time'
    :return:
    """
    url = 'https://www.tencentwm.com/fbp/cont/v1/trpc.com.tencent.fit.fucont.feeds.ao.facade.FucontFeedsAoService.GetSubjectListByCommunity'

    data = json.dumps({
        "hideCgiLoading": True,
        "customBoxErr": True,
        "ignoreSpecialErr": True,
        "stock_id": fund_id,
        "begin": begin,
        "begin_score": begin_score,
        "limit": 10,
        "order": order,
        "need_user": False,
        "hideLoading": True,
        # "g_tk": "1136833025"
    })

    response= requests.post(url, headers=HEADERS,cookies=COOKIES, data=data)
    return response.json()


# 获取机构详情
def api_institution_detail(sp_id, fund_code):
    url = "https://www.txfund.com/fbp/fund/v1/fund.fuitem_query_vo.FuitemQueryVo.QuerySkuDetailInfo"
    data = {
        "sku_info": {
            "spid": sp_id,
            "fund_code": fund_code
        },
        # "g_tk": "251938191"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data)
    return response.json()


def api_user_detail(user_id):
    url = "https://www.tencentwm.com/fbp/cont/v1/trpc.com.tencent.fit.fucont.account.query.ao.facade.fucont_account_query_ao_service.GetUserInfo"
    params = {
    }
    data = {
        "hideCgiLoading": True,
        "customBoxErr": True,
        "ignoreSpecialErr": True,
        "cont_userid": user_id,
        "need_follow_num": 1,
        "need_relation": 1,
        "need_statistics_info": 1,
        "hideLoading": True,
        # "g_tk": "1838094363"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=HEADERS, cookies=COOKIES, params=params, data=data)
    return response.json()


# 获取帖子的回复
def api_get_reply(comment_id, begin=''):
    url = 'https://www.tencentwm.com/fbp/cont/v1/trpc.com.tencent.fit.fucont.feeds.ao.facade.FucontFeedsForGoAoService.GetCommentListBySubjectID'
    data = json.dumps(
        {
            'hideCgiLoading': True,
            'customBoxErr': True,
            'ignoreSpecialErr': True,
            'subject_id': comment_id,
            'begin': begin,
            'limit': 20,
            'need_user': False,
            'hideLoading': True,
        }

    )
    response = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data, verify=False)
    return response.json()


# 解析内容
def process_string(content: str, is_format: bool = False) -> str:
    """
    解析评论内容并进行处理。

    Args:
        content (str): 要处理的内容。
        is_format (bool, optional): 是否进行格式化处理，默认为False。

    Returns:
        str: 处理后的内容。

    """
    try:
        json_data = json.loads(content)

        content = "\n".join([i['value'] for i in json_data])

        if is_format:
            pattern = r"<[^>]+>"
            content = re.sub(pattern, "", content)

        return content
    except ValueError:
        return content


# 解析时间
def convert_to_china_time(time_str):

    return time_str.split("+")[0].replace("T", " ")


# 计算用户状态
def math_status(param_dict):
    """
    计算用户状态，。计算规则为：
        用户状态是有一个多个参数的字典表示的，。哪个的值为1代表用户的状态是哪个值。然后因为参数名是英文。所以需要再转化一遍中文
    :param param_dict:
    :return:
    """
    if param_dict is {}:
        return "0"

    param_chinese_dict = {
        "hoding_investment": "持有中",
        "bought_investment": "买过",
        "fixed_investment": "定投中",
    }

    for k, v in param_dict.items():
        if v == 1:
            return param_chinese_dict.get(k, k)
    return 0


# 解析评论数据
def exc_reply(comment_id):
    """
    获取并解析评论数据
    :return:
    """
    all_reply_list = []
    begin = ""
    # 开始循环获取所有回复内容
    while True:
        res_data = api_get_reply(comment_id, begin)
        # print(res_data)
        reply_list = res_data['data']['comment']
        begin = res_data['data']['last_id']
        if len(reply_list) == 0:
            break
        else:
            all_reply_list += reply_list
    # print("已获取回复：", len(all_reply_list))
    # 重新排序一下
    all_reply_list.sort(key=lambda x: x['comment_id'], reverse=True)

    # 提取评论信息
    res_data = [
        {
            'comment_id': i['comment_id'],
            'comment_user_id': i['from_user'],
            'comment_user_name': i['user_name'],
            'comment_avatar_url': i['user_image'],
            'comment_body': i['content'],
            'comment_time': convert_to_china_time(i['created_at']),
            'comment_like': i['like_num'],
            'comment_to_user_name': i['to_user_name'],
            'comment_to_user': i['to_user'],
            'comment_to_user_img': i['to_user_image'],
            # 'comment_location': comment_location,
            # 'comment_source_reply': comment_source_reply
        } for i in all_reply_list
    ]
    return res_data

# 根据fund_code搜索基金并解析数据
def get_fund_detail(fund_code):
    """
    根据基金代码搜索基金并解析数据，并提取必要信息,然后上传基金的数据
    参数：
    fund_code (str): 基金代码

    返回：
    fund_id (str): 基金ID
    fund_name (str): 基金名称
    fund_code (str): 基金代码
    fund_detail (dict): 基金数据

    异常：
    ValueError: 检索结果为空

    示例：
    fund_code = '123456'
    fund_id, fund_name, fund_code = source_data(fund_code)
    print(fund_id, fund_name, fund_code)
    # 输出基金ID、基金名称和基金代码
    """
    for i in range(5):
        try:
            fund_data = api_source_data(fund_code)
            break
        except:
            time.sleep(5)
    if not fund_data['st_forum_results']['vst_forum_list']:
        raise ValueError("检索结果为空")
    # else:
    #     fund_data = fund_data[0]    # type:dict

    # 从搜索结果中提取必要信息
    # 基金的id，注意此处基金id并非基金code，而是腾讯自定义的基金id
    fund_id = fund_data['st_forum_results']['vst_forum_list'][0]['st_forum_detail']['s_forum_id']    # 基金id
    fund_name = fund_data['st_forum_results']['vst_forum_list'][0]['st_forum_detail']['s_forum_name']    # 基金名字
    fund_code = fund_data['st_forum_results']['vst_forum_list'][0]['st_forum_detail']['vst_forum_fund_list'][0]['s_fund_code']   # 基金代码
    sp_id = fund_data["st_product_results"]["vst_product_list"][0]["st_product_detail"]["st_fund_detail"]["s_spid"]   # 基金代码

    institution_detail = api_institution_detail(sp_id, fund_code)

    # 基金详情
    fund_detail = {
        "_id": fund_id,
        "sourceId": "TENCENT",                          # 渠道ID
        "sourceName": "腾讯",                            # 渠道名称
        "fundId": institution_detail["sku_detail_info"]["item_public_info"]["fund_info"]["i_company_code"],   # 机构代码
        "fundNane": institution_detail["sku_detail_info"]["item_public_info"]["fund_info"]["i_company_name"],  # 机构名称
        "fundCode": fund_code,                          # 基金代码
        "fundManager": fund_data["st_fund_manager_results"]["vst_fund_manager_list"][0]["st_fund_manager_detail"][
            "s_fund_manager_name"],                     # 基金经理
        "fundAbbr": institution_detail["sku_detail_info"]["item_public_info"]["fund_info"]["i_fund_brief_name"],   # 基金简称
        "fundType": fund_data["st_product_results"]["vst_product_list"][0]["st_product_detail"]["st_fund_detail"][
            "st_second_category"]["s_name"],            # 基金类型
        "forumName": institution_detail["sku_detail_info"]["item_public_info"]["fund_info"]["i_fund_brief_name"],  # 讨论区名称
        "forumUrl": f"https://www.tencentwm.com/h5/v6/pages/discussion/main/stock/index?stock_id={fund_id}",   # 讨论区地址
        "deviceIP": device_id,                             # 设备id
    }
    # print(fund_detail)
    insert_or_update('fund_detail', fund_detail)
    print("当前基金：",fund_id, '\t',fund_name, '\t',fund_code)
    return fund_id,fund_name,fund_code, fund_detail


def get_post_list(fund_id: str, start_date_format: int, end_date_format: int) -> Dict[Any, Any]:
    """
    获取基金的评论列表，并筛选出符合时间范围的评论

    参数：
    fund_id (str): 基金ID
    start_date_format (int): 开始日期（格式化后的整数）
    end_date_format (int): 结束日期（格式化后的整数）

    返回：
    all_comments_dict (dict): 符合时间范围的评论字典，键为评论的时间，值为评论的详细信息
    user_status_dict (dict): 返回用户的标签信息

    示例：
    fund_id = '123456'
    start_date_format = 20220101
    end_date_format = 20220131
    all_comments_dict = get_post_list(fund_id, start_date_format, end_date_format)
    print(all_comments_dict)
    # 输出符合时间范围的评论字典
    """
    begin = ""
    begin_score = ""
    all_comments_dict = {}
    used_begin=[]
    # user_status_dict = {}
    while True:
        # 开始进入评论区
        # print(begin)
        # 因为理财通的评论区存在一个现象：当下滑到某个限制时，会出现第一条评论，然后一直循环，所以这里判断一下，如果重复了就结束
        if begin in used_begin:
            break
        res_data = api_post_list(fund_id, begin, begin_score, 'time')
        # print(res_data)
        used_begin.append(begin)
        begin = res_data['begin']
        begin_score = res_data['begin_score']
        user_status_dict = res_data['map_user_fund_dict']
        reply_dict = res_data['subject_comment_dict']
        rss_dict = {i['subject_id']: i for i in res_data['rss_list']}

        # 遍历评论，取符合要求的（在需要的时间范围内的）
        for key, values in res_data['subject_dict'].items():
            if start_date_format <= int(key[:len(str(start_date_format))]) <= end_date_format:
                values['rss_data'] = rss_dict.get(key, {})      # 把评论和点赞数据加进来
                values['user_status'] = user_status_dict.get(values['user']['id'], {})      # 把用户状态数据加进来
                values['reply_dict'] = reply_dict.get(key, {})      # 把回复数据加进来
                all_comments_dict[key] = values
            elif int(key[:len(str(start_date_format))]) < start_date_format:
                continue
        # 这个是下一页的起始参数，如果这个参数表示时间的部分小于开始时间。即说明符合要求的评论都已经获取完毕了，可以退出了
        if int(begin[:len(str(start_date_format))]) < start_date_format:
            break
    # 按键名对字典降序排列
    all_comments_dict = dict(sorted(all_comments_dict.items(), key=lambda x: x[0], reverse=True))
    return all_comments_dict


def exc_post_data(post_id, post_data, fund_detail):
    # print(post_id)
    # exit
    post_from = fund_detail['forumName']            # 帖子来源（基金名字）
    fund_id = fund_detail['fundCode']               # 基金代码
    forumUrl = fund_detail['forumUrl']              # 讨论区链接
    post_url = f"https://www.tencentwm.com/h5/v6/pages/discussion/main/detail/index?stock_id={forumUrl}&subject_id={post_id}"          # 讨论区链接
    avatar_url = post_data['user']['image']         # 用户头像
    user_name = post_data['user']['name']           # 用户名
    user_id = post_data['user']['id']               # 用户id
    user_status = math_status(post_data['user_status'])                                         # 用户状态（基金收益）
    user_v = VIP_ENUMERATION.get(post_data['user']['vip_type'], post_data['user']['vip_type'])  # 用户vip等级
    post_time = post_data['created_at']             # 帖子创建时间
    post_title = post_data['title']                 # 帖子标题
    post_body = process_string(post_data['content'])                                # 帖子文本（带结构）
    post_body_str = process_string(post_data['content'], is_format=True)            # 帖子文本（）不带结构
    post_like = post_data['rss_data']['like_num']   # 点赞数
    post_comment = post_data['reply_dict']['cnt']   # 回复
    img_list = [i['origin'] for i in post_data.get('image_list', [])]                              # 帖子带有的所有图片的地址
    comment_list = []

    # 获取用户详情
    user_detail = api_user_detail(user_id)
    user_follow = user_detail.get('follow_num', 0)  # 用户关注
    relation = user_detail.get("relation", 0)       # 这个不知道是啥，蛮放着
    user_fans = user_detail.get('user_fans', 0)     # 用户粉丝数

    # 如果评论数不为0，就提取评论数据

    if post_comment != 0:
        comment_list = exc_reply(post_id)
    else:
        comment_list = []

    db_data = {
        '_id': post_id,
        'sourceId': "TENCENT",  # 渠道id，写死
        'sourceName': "腾讯",  # 渠道名称，写死
        'postSource': post_from,  # 帖子来源（基金名字）
        'forumId': fund_id,  # 基金代码
        "forumUrl": forumUrl,  # 评论区链接
        "postType": "主贴",  # 帖子类型
        "postUr": post_url,  # 帖子链接,小程序没有链接
        "postId": post_id,  # 帖子id
        "avatar": avatar_url,  # 用户头像
        "user_name": user_name,  # 用户名
        "userId": user_id,  # 用户id
        "userHomePage": "",  # 用户主页地址,小程序没有链接
        "gender": "",  # 用户性别,无
        "holdLabels": user_status,  # 用户状态（持有标识）
        "fundProfitsOrLosses": "",  # 理财通无
        "isV": user_v,  # 用户vip等级
        "createTime": convert_to_china_time(post_time),  # 帖子创建时间
        "postTitle": post_title,  # 帖子标题
        "postBody": post_body,  # 帖子文本（带结构）
        "postBodyStr": post_body_str,  # 帖子文本（）不带结构
        "fromPhone": "",  # 发帖设备
        "location": "",  # 发帖地址
        "readerNumber": "",  # 阅读数,无阅读数
        "likeNumber": post_like,  # 点赞数
        "commentNumber": post_comment,  # 评论数
        "shareNumber": "",  # 分享数，无分享数
        "commentList": comment_list,  # 评论列表
        'imgList': img_list,  # 帖子带有的所有图片的地址
        'relation': relation,  # 用户标签
        'userFollow': user_follow,  # 用户关注
        'userFans': user_fans,  # 用户粉丝
    }
    insert_or_update('post', db_data)


def get_fund_list():
    """
    获取基金列表函数

    该函数用于从指定目录中读取一个 Excel 文件，并返回其中的基金代码列表。

    Returns:
        list: 基金代码列表

    Raises:
        FileExistsError: 如果指定目录中存在多个文件夹，则抛出文件存在错误异常
    """
    filenames = [i for i in os.listdir(INPUT) if '~' not in i]
    if len(filenames) != 1:
        raise FileExistsError(f"存在多个文件夹：", len(filenames))

    data_df = pandas.read_excel(f"{INPUT}/{filenames[0]}", dtype='string')
    fund_code_list = data_df['fund_code']
    return fund_code_list


def run():
    for i in range(3):
        try:
            fund_code_list = get_fund_list()
            for fund_code in fund_code_list:
                print('当前基金：', fund_code)
                # 开始和结束时间 ,目前是获取三十天的所有数据
                start_date = datetime.strftime(datetime.now() - timedelta(days=10), "%Y-%m-%d %H:%M")
                end_date = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
                # 将日期转化为202310090000格式
                start_date_format = int(datetime.strptime(start_date, "%Y-%m-%d %H:%M").strftime("%Y%m%d%H%M"))
                end_date_format = int(datetime.strptime(end_date, "%Y-%m-%d %H:%M").strftime("%Y%m%d%H%M"))

                # 根据基金代码通过搜索接口获得基金信息
                fund_id, fund_name, fund_code, fund_detail = get_fund_detail(fund_code)

                # 获得post的列表页数据
                print('开始获得帖子')
                post_list = get_post_list(fund_id, start_date_format, end_date_format)
                # print(post_list)

                pool = ThreadPoolExecutor(max_workers=50)
                # 解析每个post
                print('开始解析帖子')
                for post_id,post_data in post_list.items():
                    pool.submit(exc_post_data, post_id, post_data, fund_detail)
                    # exc_post_data(post_id, post_data, fund_detail)
                pool.shutdown()
            print('运行结束')
            return
        except:
            pass

    print("发生异常，运行失败。下面可添加报警")


if __name__ == '__main__':
    run()
    pass
