import json
import os
import re
import sys
import threading
import time
import uuid
from datetime import datetime, timedelta

import requests
import urllib3
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

# config path -> D:\Dev\Data\input\badminton\config.json

# 苏州新时代文体联盟

# 关掉不安全证书的警告
urllib3.disable_warnings()

# A区 10-12,17-19

FILED_MAP = {
    "FILED_OLYMPIC": "奥体中心",
    "FILED_SOUTH": "南部市民中心",
    "FILED_NORTH": "北部市民中心",
}

_config = None

warning_info = dict()

split_symbol = "@#"

DEBUG_MODE = False

HEADERS = None

_scheduler = None
_job = None

DEFAULT_INTERVAL = 8

# 创建一个线程列表
threads = []


def detect_sku(debug_mode: bool = False):
    try:

        global DEBUG_MODE
        DEBUG_MODE = debug_mode
        # 初始化 _config
        init()
        write_log(
            log_context=f"---------------attempt at:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} begin---------------")
        global _config
        if "user_infos" not in _config:
            write_log(log_context="user_infos in config is empty, return.")
            return
        for user_info in _config['user_infos']:
            # 创建线程
            thread = threading.Thread(target=detect_sku_process, args=(user_info,))
            # 将线程添加到线程列表
            threads.append(thread)
            # 启动线程
            thread.start()

        # 等待所有线程完成
        for thread in threads:
            thread.join()
        write_log(
            log_context=f"---------------attempt at:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} end---------------")
    except Exception as ex:
        write_log(log_context=f"{threading.current_thread().name} except:{ex}")
    finally:
        write_log(log_context=f"{threading.current_thread().name} finally.")


def detect_sku_process(user_info: dict):
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
        write_log(log_context=f"{threading.current_thread().name}--------monitor target:{target}")
        for time_date in target['date_detail']:
            limit = target['limit']
            limit_date = build_date(interval=limit)
            if limit_date < target['date_detail'][0]:
                write_log(log_context=
                          f"field:{target['field']},current date:{datetime.now().strftime('%Y-%m-%d')},limit_date:{limit_date},limit:{target['limit']}--->skip")
                break
            write_log(log_context=f"current request date:{time_date}")
            has_order = api_order_list(request_id=request_id, target=target)
            if has_order:
                write_log(log_context="当前有未支付的订单，提前退出。")
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
    write_log(log_context=f"{threading.current_thread().name} detect time_date:{time_date}")
    response = None
    try:
        response = requests.post('https://api.wesais.com/field/wxFieldBuyPlan/getList', headers=headers, data=data,
                                 verify=False, timeout=(2, 10))
    except requests.exceptions.Timeout as to:
        write_log(f"field/wxFieldBuyPlan/getList timeout:{to}")
    except requests.exceptions.RequestException as e:
        write_log(f"field/wxFieldBuyPlan/getList other:{e}")
    if not response:
        write_log("field/wxFieldBuyPlan/getList result is None")
        return
    result = response.json()
    # write_log(log_context=f"A---result--->{result}")
    if "code" not in result or result['code'] != 200:
        write_log(log_context=f"{threading.current_thread().name}----B---result--->{result}")
        # B---result--->{'code': 40101, 'data': None, 'message': '请重新登陆'}
        # ----B---result--->{'code': 40101, 'data': None, 'message': '授权令牌不存，请重新登陆'}
        # ---B---result--->{'code': 40108, 'data': None, 'message': '^_^ 您的动作太快了，请休息一下 ☕️ '}
        write_log(log_context=
                  f"{threading.current_thread().name}:==========================:message:{result['message']},code:{result['code']}")
        write_log(log_context=f"{threading.current_thread().name}:刷新小程序的令牌")
        return
    collect_info = []
    try:
        dig_sku_list(collect_info, result, time_date)
    except Exception as ex:
        write_log(log_context=f"detect_sku--->{ex}")
    # write_log(log_context=f"{threading.current_thread().name}----collect_info:{collect_info}")
    cube_map = cube_collect_info(collect_info=collect_info, target=target)
    write_log(log_context=f"{threading.current_thread().name}----cube_map:{cube_map}")
    if cube_map is not None and len(cube_map) > 0:
        content = """
        ### **%s**
        """ % field
        # 提交订单，订单只有8分钟的支付时间
        if len(cube_map) < duration:
            write_log(log_context=f"{threading.current_thread().name}:当前的场地时段数量小于时长->{duration}")
            return
        first_item_len = 0
        for match, item in cube_map.items():
            first_item_len = len(cube_map[match])
            break
        push_msg = True
        candidates = []
        msgs = []
        for j in range(0, first_item_len):
            candidates.clear()
            msgs.clear()
            for match, item in cube_map.items():
                candidates.append(cube_map[match][j].split(split_symbol)[-1])
                msgs.append(cube_map[match][j])
            if len(candidates) < duration:
                write_log(log_context=f"{threading.current_thread().name}:当前的场地时段数量小于时长->{duration}")
                return
            write_log(log_context=f"{threading.current_thread().name}:candidates:{candidates}")
            sku_body = build_sku_slice(candidates=candidates, duration=duration)
            write_log(log_context=f"{threading.current_thread().name}:sku_body->{sku_body}")
            if DEBUG_MODE is None or not DEBUG_MODE:
                if sku_body and sku_body != "":
                    data = f"business_id={business_id}&stadium_id={stadium_id}&sys_id=13&sku_slice={sku_body}&business_type=1301&order_from=2&handle_info=%7B%22date_str%22%3A%22%22%7D&sales_id=0&request_id={request_id}"
                    write_log(log_context=f"{threading.current_thread().name}:data->{data}")
                    response = requests.post('https://api.wesais.com/shop/order/create', headers=headers, data=data,
                                             verify=False)
                    order_result = response.json()

                    write_log(
                        log_context=f"{threading.current_thread().name}---order create response--->{order_result}")
                    if "code" in order_result and order_result['code'] == 40004007:
                        if "message" in order_result and "提示" in order_result['message']:
                            write_log(log_context=f"{threading.current_thread().name}:{order_result}")
                            if "被其他人占用" in order_result['message'] or "不能再次预订" in order_result[
                                'message'] or "预定" in order_result['message']:
                                j += 1
                                continue
                            elif "订场操作频繁" in order_result['message']:
                                continue
                            else:
                                push_msg = False
                                break
                #     order create response---> {'code': 40004007, 'data': '', 'message': '提示:场地已被其他人占用'}
                #     order create response---> {'code': 40004007, 'data': '', 'message': '提示:所选场地不支持在现阶段预订'}
                #     order create response---> {'code': 40004007, 'data': '', 'message': '提示:订场操作频繁'}
                else:
                    write_log(log_context=
                              f"{threading.current_thread().name}:==========================没有可选的场次,无法提交预定订单")
                    return
        if not push_msg:
            return
        for item in msgs:
            v = item.split(split_symbol)
            content += create_warn_content(field=v[0], match=v[1], field_status=v[2])
        if content and content != "":
            send_weixin(content)
            today = datetime.now().strftime('%Y-%m-%d')
            if today not in warning_info:
                warning_info[today] = 0
            warning_info[today] += 1
            write_log(log_context=f"{threading.current_thread().name}:warning_info:{warning_info}")
            if warning_info[today] >= 1:
                if DEBUG_MODE is None or not DEBUG_MODE:
                    write_log(log_context=
                              f"{threading.current_thread().name}=======================恭喜你，去我的订单付款吧=======================")
                write_log(log_context=f"{threading.current_thread().name}:warning_info has already send 1 times,quit")
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
        # write_log(log_context="order list response--->", result)
        if "code" in result and result['code'] == 200:
            if len(result['data']['list']) > 0:
                first_order = result['data']['list'][0]
                if ("order_status_str" in first_order and first_order["order_status_str"] == "未支付") or (
                        "order_status" in first_order and first_order['order_status'] == 0):
                    write_log(log_context=
                              f"{threading.current_thread().name}:=======================我的订单有未支付订单，去支付，付款时间只有8分钟")
                    return True
    except Exception as ex:
        write_log(log_context=f"{threading.current_thread().name}:api_order_list exception--->{ex}")
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
                            # write_log(log_context=s['sku_name'].replace(" ", "") + "场次:" + time_date + " " + s['time_str'] + (
                            #     "已定" if s['is_lock'] else "空闲"))


def create_warn_content(field: str = "", match: str = "", field_status: str = ""):
    warnContent = """
    > 场地:<font color="info">""" + field + """</font> 
    > 场次:<font color="warning">""" + match + " " + field_status + """</font> 
    """
    return warnContent


def init():
    parse_config()


def refresh_job():
    time.sleep(2)
    global _scheduler
    global _job
    if _scheduler and _job:
        next_interval = _config['trigger']['interval'] if _config and 'trigger' in _config and 'interval' in _config[
            'trigger'] else DEFAULT_INTERVAL
        unit = _config['trigger']['unit'] if _config and 'trigger' in _config and 'unit' in _config[
            'trigger'] else None
        if unit and unit.lower() and unit.lower() == "s":
            next_run_time = datetime.now() + timedelta(seconds=next_interval)
            _job = _scheduler.reschedule_job(_job.id, trigger=IntervalTrigger(seconds=next_interval))
        else:
            next_run_time = datetime.now() + timedelta(minutes=next_interval)
            _job = _scheduler.reschedule_job(_job.id, trigger=IntervalTrigger(minutes=next_interval))
        # 更新下一次执行时间
        write_log(log_context=
                  f"reschedule_job job_id:{_job.id}---->next_run_time:{next_run_time.strftime('%Y-%m-%d %H:%M:%S')}->next_interval:{next_interval}")


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


def build_sku_slice(candidates: list, duration: int = 2):
    if not candidates or len(candidates) < duration:
        return ""
    sku_slice = ""
    end = min(len(candidates), duration)
    for i in range(0, end):
        sku_slice += candidates[i] + "%3A1"
        if i != end - 1:
            sku_slice += "%2C"
    write_log(log_context=f"sku_slice:{sku_slice}")
    return sku_slice


def get_random_sku_slice(cube_map: dict, duration: int = 2):
    if cube_map and len(cube_map) <= 1:
        write_log(log_context=f"{threading.current_thread().name}:==========================当前的场次不够，无法支付")
        return []
    candidates = []
    for item in cube_map:
        candidates.append(item.split(split_symbol)[-1])
    return candidates


def cube_collect_info(collect_info: list, target: dict):
    raw_cube_info = []
    venue_detail = target['venue_detail']
    for candidate in collect_info:
        arr = candidate.split(split_symbol)
        if arr[0].split("_")[1] in venue_detail:
            raw_cube_info.append(candidate)
    return sort_cube_info(raw_cube_info=raw_cube_info, target=target)


def sort_cube_info(raw_cube_info: [], target: dict):
    cube_map = {}
    for v_d in target['venue_detail']:
        for raw in raw_cube_info:
            arr = raw.split(split_symbol)
            if v_d == arr[0].split("_")[1]:
                match = arr[1]
                cube_list = cube_map.get(match, [])
                cube_list.append(raw)
                cube_map.setdefault(match, cube_list)
    return cube_map


def parse_config():
    if len(sys.argv) < 2:
        write_log(log_context="using default config path...")
        config_path = r"D:\Dev\Data\input\badminton\config.json"
    else:
        config_path = sys.argv[1]
    # 打印所有参数
    write_log(log_context=f"config path:{config_path}")
    directory = os.path.dirname(config_path)
    with open(config_path, 'r', encoding='utf-8') as file:
        # 读取文件内容
        content = file.read()
    try:
        global _config
        _config = json.loads(content)
    except Exception as ex:
        write_log(log_context=f"解析的config.json文件可能存在错误,请检查。{ex}")
        return
    write_log(log_context=f"before _config:{_config}")
    user_infos = fill_user_infos(directory)
    _config['user_infos'] = user_infos
    # _config['trigger']['interval'] if _config and 'trigger' in _config and 'interval' in _config[
    #     'trigger'] else DEFAULT_INTERVAL
    for item in _config['targetList']:
        field = item['field']
        business_id, stadium_id, group_id = get_basic_info(field=field)
        item['business_id'] = business_id
        item['stadium_id'] = stadium_id
        item['group_id'] = group_id
        if "limit" not in item or item['limit'] is None:
            limit = get_limit_days(field=field)
            item['limit'] = limit
        _symbol = get_tail_symbol(field=field)
        _prefix = _symbol[1] if _symbol[2] == "PREFIX" else ""
        _suffix = _symbol[1] if _symbol[2] == "SUFFIX" else ""
        venue_detail = [
            f"{item['court']}{_symbol[0]}{_prefix}{venue}{_suffix}" for venue in item['venue']]
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
        this_monday_str = this_monday.strftime("%Y-%m-%d")
        write_log(
            log_context=f"{threading.current_thread().name}:This Monday's date:{this_monday_str}")
        for offset in item['offset']:
            for week in item['week']:
                next_date = this_monday + timedelta(days=week - 1 + offset * 7)
                date_detail.append(next_date.strftime("%Y-%m-%d"))
                next_date_str = next_date.strftime("%Y-%m-%d")
                write_log(log_context=f"{threading.current_thread().name}:{next_date_str}")
        item['date_detail'] = date_detail
    write_log(log_context=f"after _config:{_config}")


def fill_user_infos(directory: str):
    user_infos = []
    for dir_path, dir_names, file_names in os.walk(directory):
        for file_name in file_names:
            if file_name.startswith("response_"):
                response_file_path = os.path.join(dir_path, file_name)
                # 处理文件
                write_log(log_context=response_file_path)
                with open(response_file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                if not lines or len(lines) == 0:
                    write_log(log_context=f"response.txt is empty,fill the file first.->{file_name}")
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
    if field == FILED_MAP['FILED_OLYMPIC']:
        return 6
    elif field == FILED_MAP['FILED_SOUTH']:
        return 2
    elif field == FILED_MAP['FILED_NORTH']:
        return 6
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
        write_log(log_context=f"No auth_code found.->{randon_auth_code}")
        return randon_auth_code


def get_basic_info(field: str):
    business_id, stadium_id, ground_id = 10000935, 11733, 11733001
    if field == FILED_MAP['FILED_OLYMPIC']:
        business_id, stadium_id, ground_id = 10000935, 11733, 11733001
    elif field == FILED_MAP['FILED_SOUTH']:
        business_id, stadium_id, ground_id = 10000785, 11501, 11501001
    elif field == FILED_MAP['FILED_NORTH']:
        business_id, stadium_id, ground_id = 10000932, 11726, 11726001
    return business_id, stadium_id, ground_id


def get_beijing_time(sync_time=True):
    if not sync_time:
        return
    # 请求World Time API获取东八区（北京时间）的时间
    response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Shanghai')
    if response.status_code == 200:
        # 解析JSON响应
        data = response.json()
        # 获取当前时间并转换为datetime对象
        beijing_time = datetime.fromisoformat(data['datetime']).strftime('%Y-%m-%d %H:%M:%S')
        write_log(log_context=f'sync time beijing time:{beijing_time}')
        return beijing_time
    else:
        write_log(log_context=f'Failed to get time:{response.status_code}')
        return None


def get_tail_symbol(field: str):
    if field == FILED_MAP['FILED_OLYMPIC']:
        return "---", "#", "SUFFIX"
    elif field == FILED_MAP['FILED_SOUTH']:
        return "--", "号", "SUFFIX"
    elif field == FILED_MAP['FILED_NORTH']:
        return "--", "场地", "PREFIX"
    return "---", "#", "SUFFIX"


def write_log(file_name: str = None, log_context: str = ""):
    current_date = datetime.now().strftime("%Y%m%d")
    full_name = file_name
    if not file_name:
        folder_path = "logs"
        dir_path = "D:\\Dev\\Data\\input\\badminton\\" + folder_path + "\\"
        # 检查文件夹是否存在，如果不存在则创建
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)  # exist_ok=True 表示如果文件夹已存在不会抛出错误
        file_name = f"{current_date}.txt"
        full_name = dir_path + file_name
    if not full_name:
        print(f"{log_context}")
        return
    with open(file=full_name, mode='a', encoding='utf-8') as file:
        print(f"{log_context}")
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{now_str} {log_context}\n")


def start_job(debug_mode=False):
    write_log(log_context="start_job_core start")
    init()
    run_dates = _config['trigger']['run_dates'] if _config and 'trigger' in _config and 'run_dates' in _config[
        'trigger'] else []
    sync_time = _config['trigger']['sync_time'] if _config and 'trigger' in _config and 'sync_time' in _config[
        'trigger'] else "False"
    if run_dates and len(run_dates) > 0:
        run_dates = sorted(run_dates)
        for run_date in run_dates:
            start_job_core(run_date=run_date, debug_mode=debug_mode, sync_time=sync_time)
    else:
        start_job_core(run_date=None, debug_mode=debug_mode)


def start_job_core(run_date=None, debug_mode=False, sync_time=False):
    write_log(log_context=
              f"------------------timer:start:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:sync_time:{get_beijing_time(sync_time)}------------------")
    # 创建后台调度器
    global _scheduler
    _scheduler = BackgroundScheduler()
    # 添加任务，interval参数表示间隔时间，单位为秒
    _init_next_interval = 60 * DEFAULT_INTERVAL
    next_run_time = datetime.now() + timedelta(seconds=_init_next_interval)
    global _job
    if run_date is None:
        _job = _scheduler.add_job(detect_sku, 'interval', seconds=_init_next_interval, next_run_time=datetime.now(),
                                  args=(debug_mode,), max_instances=5)
        write_log(log_context=
                  f"[interval mode] add_job job_id:{_job.id}---->next_run_time:{next_run_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        today = datetime.now().strftime('%Y-%m-%d')
        actual_run_date = "%s %s" % (today, run_date)
        _job = _scheduler.add_job(detect_sku, 'date', run_date=actual_run_date, args=(debug_mode,), max_instances=5)
        write_log(log_context=f"[date mode]add_job job_id:{_job.id}---->next_run_time:{actual_run_date}")
    # 启动调度器
    _scheduler.start()

    if run_date is None:
        refresh_job()
    # 为了防止程序退出，主线程在这里等待
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        # 关闭调度器
        _scheduler.shutdown()


# B---result--->{'code': 40101, 'data': None, 'message': '请重新登陆'}
# 每日预定时长不能大于2小时

if __name__ == '__main__':
    try:
        # start_job(debug_mode=True)
        start_job(debug_mode=False)
        # detect_sku(debug_mode=True)
    except Exception as ex:
        write_log(log_context=f"{threading.current_thread().name} outer ex:{ex}")
    finally:
        write_log(log_context=f"{threading.current_thread().name} outer finally.")
