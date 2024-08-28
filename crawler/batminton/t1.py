import json
import os
import sys
from datetime import datetime, timedelta

import time
from concurrent.futures import Future, ThreadPoolExecutor

import urllib3
from apscheduler.schedulers.background import BackgroundScheduler
import requests

# 关掉不安全证书的警告
urllib3.disable_warnings()

target_list = {
    "date": [],
    "match": ["17:00--18:00", "18:00--19:00", "19:00--20:00", "20:00--21:00", "21:00--22:00"]
}

warning_info = dict()


def detect_sku(time_date: str = None):
    #
    if not time_date:
        time_date = build_date(interval=2)
    init()
    headers = {
        'Host': 'api.wesais.com',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11177',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdCI6MTcyNDg0Nzk1OSwiaWQiOiIxNzI0ODQ3OTU5MDM4NTIiLCJhaWQiOjEwMTAxLCJtaWQiOjQsInRpZCI6NSwicGFyYW1zIjoie1wiY29tcGFueV9pZFwiOjYxNSxcImFjY291bnRfdHlwZVwiOjMxLFwiYWNjb3VudF9pZFwiOjEwMDk2MTYsXCJtZW1iZXJfaWRcIjoxMTkyMjk4LFwic2FmZV9sXCI6MSxcInBlcnNvbm5lbF9pZFwiOjExOTIyOTh9In0.caa3WW1zF2psLRSvtdFxBkzA1FJuaCKPGhBTxTnjxiE',
        'Origin': 'https://xcx.wesais.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://xcx.wesais.com/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    data = {
        'business_id': '10000785',
        'stadium_id': '11501',
        'ground_id': '11501001',
        'time_date': time_date,
        'request_id': '97e2b446d763a52c592c39225f0e8b87',
    }
    print(f"detect time_date:{time_date}")
    if time_date not in target_list['date']:
        print(f"{time_date} is not in candidate date")
        return
    response = requests.post('https://api.wesais.com/field/wxFieldBuyPlan/getList', headers=headers, data=data,
                             verify=False)
    result = response.json()
    print(f"A---result--->{result}")
    if "code" not in result or result['code'] != 200:
        print(f"B---result--->{result}")
        return
    collect_info = []
    try:
        sku_list = result['data']['skuList']
        for sku in sku_list:
            for sku_item in sku:
                for s in sku_item:
                    if time_date in target_list['date']:
                        if not s['is_lock'] and s['time_str'] in target_list['match']:
                            collect_info.append(
                                time_date + "_" + s['sku_name'] + "#" + s['time_str'] + "#" + ("已定" if s[
                                    'is_lock'] else "空闲"))
                            print(s['sku_name'] + "场次:" + time_date + " " + s['time_str'] + (
                                "已定" if s['is_lock'] else "空闲"))
    except Exception as ex:
        print(f"detect_sku--->{ex}")
    if collect_info is not None and len(collect_info) > 0:
        content = """
    ### **南部市民中心**
    """
        for item in collect_info:
            v = item.split("#")
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
                sys.exit()


def create_warn_content(field: str = "", match: str = "", field_status: str = ""):
    warnContent = """
    > 场地:<font color="info">""" + field + """</font> 
    > 场次:<font color="warning">""" + match + " " + field_status + """</font> 
    """
    return warnContent


def init():
    today = datetime.now()
    today_weekday = today.weekday()
    if today_weekday == 5:
        days_to_saturday = 7
    else:
        days_to_saturday = (5 - today_weekday) % 7
    next_saturday = today + timedelta(days=days_to_saturday)
    formatted_next_saturday = next_saturday.strftime('%Y-%m-%d')
    global target_list
    # target_list['date'].clear()
    target_list['date'].append(formatted_next_saturday)
    print(f"target_list---->{target_list}")


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
    start_job()
    # detect_sku()
