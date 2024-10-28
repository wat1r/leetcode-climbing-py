import json
import os
import sys
import time
from datetime import datetime, timedelta

import requests
import urllib3
from apscheduler.schedulers.background import BackgroundScheduler

# 苏州新时代文体联盟

# 关掉不安全证书的警告
urllib3.disable_warnings()

# A区 10-12,17-19

target_list = {
    "date": [],
    # "date": ['2024-11-01'],
    "match": ["19:00--20:00", "20:00--21:00"],
    # "match": ["10:00--11:00", "11:00--12:00", "12:00--13:00", "13:00--14:00", "14:00--15:00", "15:00--16:00",
    #           "16:00--17:00"]

}

_config = None

warning_info = dict()

split_symbol = "@#"


def detect_sku(time_date: str = None):
    #
    if not time_date:
        time_date = build_date(interval=6)
    init()
    # 替换
    ready_to_request = False
    global _config
    for target in _config['targetList']:
        if time_date in target['date_detail']:
            ready_to_request = True
            break
    if not ready_to_request:
        print(f"max {time_date} is not candidates ,return.")
        return
    auth_token = _config['user_info']["auth_token"] if "user_info" in _config and "auth_token" in _config[
        'user_info'] and _config['user_info'][
                                                           "auth_token"] != "" else "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdCI6MTcyOTk4ODIxOSwiaWQiOiIxNzI5OTg4MjE5MDE1NzMiLCJhaWQiOjEwMTAxLCJtaWQiOjQsInRpZCI6NSwicGFyYW1zIjoie1wiY29tcGFueV9pZFwiOjYxNSxcImFjY291bnRfdHlwZVwiOjMxLFwiYWNjb3VudF9pZFwiOjEwMDk2MTYsXCJtZW1iZXJfaWRcIjoxMTkyMjk4LFwic2FmZV9sXCI6MSxcInBlcnNvbm5lbF9pZFwiOjExOTIyOTh9In0.zzamXD2BJ0vdpkUbdtsXkTgP7DOsUX4chPTTWW8vVCg"
    request_id = _config['user_info']["request_id"] if "user_info" in _config and "request_id" in _config[
        'user_info'] and _config['user_info']["request_id"] != "" else '86a277d9bd81ffd4cdac54de0fa4f42d'
    headers = {
        'Host': 'api.wesais.com',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c0f)XWEB/11275',
        'Authorization': auth_token,
        'Origin': 'https://xcx.wesais.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://xcx.wesais.com/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    # 替换
    for target in _config['targetList']:
        for time_date in target['date_detail']:
            print(f"current request date:{time_date}")
            api_request(time_date=time_date, request_id=request_id, headers=headers)


def api_request(time_date: str, request_id: str, headers: dict):
    data = {
        'business_id': '10000935',
        'stadium_id': '11733',
        'ground_id': '11733001',
        'time_date': time_date,
        'request_id': request_id,  # 待替换
    }
    print(f"detect time_date:{time_date}")
    response = requests.post('https://api.wesais.com/field/wxFieldBuyPlan/getList', headers=headers, data=data,
                             verify=False)
    result = response.json()
    # print(f"A---result--->{result}")
    if "code" not in result or result['code'] != 200:
        print(f"B---result--->{result}")
        return
    collect_info = []
    try:
        sku_list = result['data']['skuList']
        for sku in sku_list:
            for sku_item in sku:
                for s in sku_item:
                    global _config
                    for target in _config['targetList']:
                        if time_date in target['date_detail']:
                            if not s['is_lock'] and s['time_str'] in target['match']:
                                if s['is_lock'] is not None and not s['is_lock']:
                                    collect_info.append(
                                        time_date + "_" + s['sku_name'].replace(" ", "") + split_symbol + s[
                                            'time_str'] + split_symbol + (
                                            "已定" if s[
                                                'is_lock'] else "空闲") + split_symbol + s['sku'])
                                # print(s['sku_name'].replace(" ", "") + "场次:" + time_date + " " + s['time_str'] + (
                                #     "已定" if s['is_lock'] else "空闲"))
    except Exception as ex:
        print(f"detect_sku--->{ex}")
    cube_info = cube_collect_info(collect_info)
    print("----cube_info:", cube_info)
    if cube_info is not None and len(cube_info) > 0:
        content = """
        ### **奥体中心**
        """

        # # 提交订单，订单只有8分钟的支付时间
        # sku_body = build_sku_slice(get_random_sku_slice(cube_info))
        # print("sku_body->", sku_body)
        # data = f"business_id=10000935&stadium_id=11733&sys_id=13&sku_slice={sku_body}&business_type=1301&order_from=2&handle_info=%7B%22date_str%22%3A%22%22%7D&sales_id=0&request_id={request_id}"
        #
        # response = requests.post('https://api.wesais.com/shop/order/create', headers=headers, data=data, verify=False)
        # print("order create response--->", response.json())

        for item in cube_info:
            v = item.split(split_symbol)
            content += create_warn_content(field=v[0], match=v[1], field_status=v[2])
        if content and content != "":
            send_weixin(content)
            today = datetime.now().strftime('%Y-%m-%d')
            if today not in warning_info:
                warning_info[today] = 0
            warning_info[today] += 1
            print(f"warning_info:{warning_info}")
            if warning_info[today] >= 3:
                print("warning_info has already send 3 times,quit")
                sys.exit(1)


def create_warn_content(field: str = "", match: str = "", field_status: str = ""):
    warnContent = """
    > 场地:<font color="info">""" + field + """</font> 
    > 场次:<font color="warning">""" + match + " " + field_status + """</font> 
    """
    return warnContent


def init():
    # today = datetime.now()
    # # 计算6天后的时间
    # six_days_later = today + timedelta(days=6)
    # formatted_six_days_later = six_days_later.strftime('%Y-%m-%d')
    # global target_list
    # # target_list['date'].clear()
    # target_list['date'].append(formatted_six_days_later)
    # print(f"target_list---->{target_list}")
    parse_config()


# warnContent = bytes(warnContent, 'utf-8').decode('unicode_escape')

def send_weixin(content):
    webHookUrl = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=1601b78b-eb16-43c8-8afa-04a3362b0746"
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": content,  # 让群机器人发送的消息内容。
            "mentioned_list": "@all",
        }
    }
    data = json.dumps(data)
    res = requests.post(webHookUrl, data=data, headers=headers, verify=False)  # 直接一句post就可以实现通过机器人在群聊里发消息


def build_date(interval: int):
    current_date = datetime.now()
    interval_days = timedelta(days=interval)
    future_date = current_date + interval_days
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date


def build_sku_slice(candidates: list):
    if not candidates or len(candidates) == 0:
        return
    sku_slice = ""
    for i in range(0, len(candidates)):
        sku_slice += candidates[i] + "%3A1"
        if i != len(candidates) - 1:
            sku_slice += "%2C"
    print("sku_slice:", sku_slice)
    return sku_slice


def get_random_sku_slice(collect_info: list):
    candidates = []
    for item in collect_info:
        candidates.append(item.split(split_symbol)[-1])
        if len(candidates) == 2:
            print("candidates->", candidates)
            return candidates


def cube_collect_info(collect_info: list):
    cube_info = []
    for target in _config['targetList']:
        venue_detail = target['venue_detail']
        # court = item['court']
        for candidate in collect_info:
            arr = candidate.split(split_symbol)
            if arr[0].split("_")[1] in venue_detail:
                cube_info.append(candidate)
    return cube_info


def parse_config():
    if len(sys.argv) < 2:
        print("Usage: python script.py <arg1> [<arg2>...]")
        sys.exit(1)
    config_path = sys.argv[1]
    # 打印所有参数
    print("config path:", config_path)
    directory = os.path.dirname(config_path)
    with open(config_path, 'r', encoding='utf-8') as file:
        # 读取文件内容
        content = file.read()
    with open(directory + "\\response.txt", 'r', encoding='utf-8') as file:
        # 读取所有行到一个列表中
        lines = file.readlines()
    # "D:\Dev\Data\input\batminton\response.txt"
    response_content = lines[-1] if lines else None
    if response_content:
        _response_content = json.loads(response_content)
    global _config
    _config = json.loads(content)
    print("before _config:", _config)
    if _response_content:
        _config['user_info']['auth_token'] = _response_content['auth_token']
        _config['user_info']['request_id'] = get_request_id(_response_content['request_body'])
    for item in _config['targetList']:
        venue_detail = [f"{item['court']}---{venue}#" for venue in item['venue']]
        item['venue_detail'] = venue_detail
        date_detail = []
        # 获取当前日期
        today = datetime.now()
        # 计算今天是周几（0是周一，6是周日）
        weekday = today.weekday()
        # 如果今天是周一（0），则直接获取日期，否则向后计算到周一
        if weekday == 0:  # 周一
            this_monday = today
        else:
            this_monday = today - timedelta(days=weekday)
        print("This Monday's date:", this_monday.strftime("%Y-%m-%d"))
        for offset in item['offset']:
            for week in item['week']:
                next_date = this_monday + timedelta(days=((week - 2 - this_monday.weekday())) % 7 + 1 + offset * 7)
                date_detail.append(next_date.strftime("%Y-%m-%d"))
                print(next_date.strftime("%Y-%m-%d"))
        item['date_detail'] = date_detail
    print("after _config:", _config)


def get_request_id(request_body: str):
    # 以'&'分割字符串，得到一个包含多个键值对的列表
    params = request_body.split('&')
    # 创建一个空字典来存储参数
    params_dict = {}

    # 遍历列表，将每个键值对分割并存储到字典中
    for param in params:
        key, value = param.split('=')
        params_dict[key] = value
    # 获取request_id的值
    request_id = params_dict.get('request_id', None)
    return request_id


def start_job():
    print("start_job_core start")
    start_job_core()


def start_job_core():
    print("------------------timer:start------------------")
    # 创建后台调度器
    scheduler = BackgroundScheduler()
    # 添加任务，interval参数表示间隔时间，单位为秒
    scheduler.add_job(detect_sku, 'interval', seconds=60 * 1)
    # 启动调度器
    scheduler.start()
    # 为了防止程序退出，主线程在这里等待
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        # 关闭调度器
        scheduler.shutdown()


if __name__ == '__main__':
    # start_job()
    detect_sku()
    # init()
    # parse_config()
    # get_target_date()
