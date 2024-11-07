import json
import os
import re
import sys
import time
import uuid
from datetime import datetime, timedelta

import requests
import urllib3
from apscheduler.schedulers.background import BackgroundScheduler

# config path -> D:\Dev\Data\input\badminton\config.json

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

DEBUG_MODE = False

HEADERS = None


def detect_sku(debug_mode: bool = False):
    global DEBUG_MODE
    DEBUG_MODE = debug_mode
    # 初始化 _config
    print(f"---------------attempt at:{datetime.now().strftime('%Y-%m-%d %H:%M')}---------------")
    init()
    global _config
    if "user_infos" not in _config:
        print("user_infos in config is empty, return.")
        return
    for user_info in _config['user_infos']:
        auth_token = user_info["auth_token"] if "auth_token" in user_info and user_info[
            "auth_token"] != "" else "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdCI6MTcyOTk4ODIxOSwiaWQiOiIxNzI5OTg4MjE5MDE1NzMiLCJhaWQiOjEwMTAxLCJtaWQiOjQsInRpZCI6NSwicGFyYW1zIjoie1wiY29tcGFueV9pZFwiOjYxNSxcImFjY291bnRfdHlwZVwiOjMxLFwiYWNjb3VudF9pZFwiOjEwMDk2MTYsXCJtZW1iZXJfaWRcIjoxMTkyMjk4LFwic2FmZV9sXCI6MSxcInBlcnNvbm5lbF9pZFwiOjExOTIyOTh9In0.zzamXD2BJ0vdpkUbdtsXkTgP7DOsUX4chPTTWW8vVCg"
        request_id = user_info["auth_code"] if "auth_code" in user_info and user_info[
            "auth_code"] != "" else str(uuid.UUID)
        account_id = user_info["account_id"] if "account_id" in user_info and user_info[
            "account_id"] != "" else "UNKNOWN_ACCOUNT"
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
        global HEADERS
        HEADERS = headers
        # 替换
        has_order = False
        for target in _config['targetList']:
            print(f"--------monitor target:{target}")
            for time_date in target['date_detail']:
                limit = target['limit']
                limit_date = build_date(interval=limit)
                if limit_date < target['date_detail'][0]:
                    print(
                        f"field:{target['field']},current date:{datetime.now().strftime('%Y-%m-%d')},limit_date:{limit_date},limit:{target['limit']}--->skip")
                    break
                print(f"current request date:{time_date}")
                has_order = api_order_list(request_id=request_id, target=target)
                if has_order:
                    break
                api_request(time_date=time_date, request_id=request_id, headers=headers, target=target)
            if has_order:
                break


def api_request(time_date: str, request_id: str, headers: dict, target: dict):
    business_id, stadium_id, group_id, field, duration = target['business_id'], target['stadium_id'], target[
        'group_id'], target[
        'field'], target['duration'] if 'duration' in target else 2
    data = {
        'business_id': str(business_id),
        'stadium_id': str(stadium_id),
        'ground_id': str(group_id),
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
        # B---result--->{'code': 40101, 'data': None, 'message': '请重新登陆'}
        print(f"==========================:message:{result['message']},code:{result['code']}")
        return
    collect_info = []
    try:
        dig_sku_list(collect_info, result, time_date)
    except Exception as ex:
        print(f"detect_sku--->{ex}")
    cube_info = cube_collect_info(collect_info=collect_info, target=target)
    print("----cube_info:", cube_info)
    if cube_info is not None and len(cube_info) > 0:
        content = """
        ### **%s**
        """ % field
        if DEBUG_MODE is None or not DEBUG_MODE:
            # 提交订单，订单只有8分钟的支付时间
            sku_body = build_sku_slice(get_random_sku_slice(collect_info=cube_info, duration=duration))
            print(f"sku_body->{sku_body}")
            if sku_body and sku_body != "":
                data = f"business_id={business_id}&stadium_id={stadium_id}&sys_id=13&sku_slice={sku_body}&business_type=1301&order_from=2&handle_info=%7B%22date_str%22%3A%22%22%7D&sales_id=0&request_id={request_id}"
                print("data->", data)
                response = requests.post('https://api.wesais.com/shop/order/create', headers=headers, data=data,
                                         verify=False)
                print("order create response--->", response.json())
            else:
                print("==========================没有可选的场次,无法提交预定订单")
                return
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
            if warning_info[today] >= 1:
                if DEBUG_MODE is None or not DEBUG_MODE:
                    print("=======================恭喜你，去我的订单付款吧=======================")
                print("warning_info has already send 1 times,quit")
                return


def api_order_list(request_id: str, target: dict):
    business_id = target['business_id']
    data = {
        'business_id': str(business_id),
        'stadium_id': '0',
        'order_from': '2',
        'order_status': '-1',
        'sort': '-1',
        'page': '1',
        'size': '8',
        'request_id': request_id,
    }
    try:
        response = requests.post('https://api.wesais.com/shop/order/list', headers=HEADERS, data=data, verify=False)
        result = response.json()
        print("order list response--->", result)
        if "code" in result and result['code'] == 200:
            if len(result['data']['list']) > 0:
                first_order = result['data']['list'][0]
                if ("order_status_str" in first_order and first_order["order_status_str"] == "未支付") or (
                        "order_status" in first_order and first_order['order_status'] == 0):
                    print("=======================我的订单有未支付订单，去支付，付款时间只有8分钟")
                    return True
    except Exception as ex:
        print(f"api_order_list exception--->{ex}")
    return False


def dig_sku_list(collect_info, result, time_date):
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


def create_warn_content(field: str = "", match: str = "", field_status: str = ""):
    warnContent = """
    > 场地:<font color="info">""" + field + """</font> 
    > 场次:<font color="warning">""" + match + " " + field_status + """</font> 
    """
    return warnContent


def init():
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


def build_date(interval: int = 6):
    current_date = datetime.now()
    interval_days = timedelta(days=interval)
    future_date = current_date + interval_days
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date


def build_sku_slice(candidates: list):
    if not candidates or len(candidates) <= 1:
        return ""
    sku_slice = ""
    for i in range(0, len(candidates)):
        sku_slice += candidates[i] + "%3A1"
        if i != len(candidates) - 1:
            sku_slice += "%2C"
    print("sku_slice:", sku_slice)
    return sku_slice


def get_random_sku_slice(collect_info: list, duration: int = 2):
    if collect_info and len(collect_info) <= 1:
        print("==========================当前的场次不够，无法支付")
        return []
    candidates = []
    for item in collect_info:
        candidates.append(item.split(split_symbol)[-1])
        global _config
        if len(candidates) == duration:
            print("candidates->", candidates)
            return candidates
    return candidates


def cube_collect_info(collect_info: list, target: dict):
    raw_cube_info = []
    venue_detail = target['venue_detail']
    # court = item['court']
    for candidate in collect_info:
        arr = candidate.split(split_symbol)
        if arr[0].split("_")[1] in venue_detail:
            raw_cube_info.append(candidate)
    return sort_cube_info(raw_cube_info=raw_cube_info, target=target)


def sort_cube_info(raw_cube_info: [], target: dict):
    cube_info = []
    cube_map = {}
    for v_d in target['venue_detail']:
        for raw in raw_cube_info:
            arr = raw.split(split_symbol)
            if v_d == arr[0].split("_")[1]:
                match = arr[1]
                cube_list = cube_map.get(match, [])
                cube_list.append(raw)
                cube_map.setdefault(match, cube_list)
    for match, cube_list in cube_map.items():
        if len(cube_list) > 0:
            cube_info.append(cube_list[0])
    return cube_info


def parse_config():
    if len(sys.argv) < 2:
        print("using default config path...")
        config_path = r"D:\Dev\Data\input\badminton\config.json"
    else:
        config_path = sys.argv[1]
    # 打印所有参数
    print("config path:", config_path)
    directory = os.path.dirname(config_path)
    with open(config_path, 'r', encoding='utf-8') as file:
        # 读取文件内容
        content = file.read()
    global _config
    _config = json.loads(content)
    print("before _config:", _config)
    user_infos = fill_user_infos(directory)
    _config['user_infos'] = user_infos
    for item in _config['targetList']:
        field = item['field']
        business_id, stadium_id, group_id = get_basic_info(field=field)
        item['business_id'] = business_id
        item['stadium_id'] = stadium_id
        item['group_id'] = group_id
        limit = get_limit_days(field=field)
        item['limit'] = limit
        _symbol = get_tail_symbol(field=field)
        venue_detail = [f"{item['court']}{_symbol[0]}{venue}{_symbol[1]}" for venue in item['venue']]
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


def fill_user_infos(directory: str):
    user_infos = []
    for dir_path, dir_names, file_names in os.walk(directory):
        for file_name in file_names:
            if file_name.startswith("response_"):
                response_file_path = os.path.join(dir_path, file_name)
                # 处理文件
                print(response_file_path)
                with open(response_file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                if not lines or len(lines) == 0:
                    print(f"response.txt is empty,fill the file first.->{file_name}")
                    continue
                response_content = lines[-1] if lines else None
                if response_content:
                    _response_content = json.loads(response_content)
                    if _response_content:
                        if "response_data" in _response_content:
                            _response_data = _response_content['response_data']
                            if "code" in _response_data and _response_data['code'] == 200:
                                _data = _response_data['data']
                                account_id, account_type, auth_token = _data['account_id'], _data['account_type'], \
                                    _data[
                                        'token']
                                user_info = dict()
                                user_info['account_id'] = account_id
                                user_info['account_type'] = account_type
                                user_info['auth_token'] = auth_token
                                user_info['auth_code'] = get_auth_code(_response_content['request_body'])
                                user_infos.append(user_info)
    return user_infos


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


def get_limit_days(field: str):
    if field == "奥体中心":
        return 6
    elif field == "南部市民中心":
        return 2
    return 6


def get_auth_code(request_body: str):
    pattern = r'auth_code=([a-zA-Z0-9]+)'
    match = re.search(pattern, request_body)
    # 如果找到匹配项，则提取auth_code的值
    if match:
        auth_code = match.group(1)
        return auth_code
    else:
        randon_auth_code = str(uuid.UUID)
        print(f"No auth_code found.->{randon_auth_code}")
        return randon_auth_code


def get_basic_info(field: str):
    business_id, stadium_id, ground_id = 10000935, 11733, 11733001
    if field == "奥体中心":
        business_id, stadium_id, ground_id = 10000935, 11733, 11733001
    elif field == "南部市民中心":
        business_id, stadium_id, ground_id = 10000785, 11501, 11501001
    return business_id, stadium_id, ground_id


def get_tail_symbol(field: str):
    if field == "奥体中心":
        return "---", "#"
    elif field == "南部市民中心":
        return "--", "号"
    return "---", "#"


def start_job():
    print("start_job_core start")
    start_job_core()


def start_job_core():
    print("------------------timer:start------------------")
    # 创建后台调度器
    scheduler = BackgroundScheduler()
    # 添加任务，interval参数表示间隔时间，单位为秒
    scheduler.add_job(detect_sku, 'interval', seconds=60 * 1, next_run_time=datetime.now())
    # 启动调度器
    scheduler.start()
    # 为了防止程序退出，主线程在这里等待
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        # 关闭调度器
        scheduler.shutdown()
# B---result--->{'code': 40101, 'data': None, 'message': '请重新登陆'}

if __name__ == '__main__':
    start_job()
    # detect_sku(debug_mode=False)
