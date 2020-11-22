# from openpyxl import load_workbook
import requests
import xlrd
import json
# 导入BaiduSpider
from baiduspider import BaiduSpider
from pprint import pprint
import time
import sys

import random

"""
https://mp.weixin.qq.com/s/z0DM5iaWjQ5aax10mNe7FA
"""

# 实例化BaiduSpider
spider = BaiduSpider()

# 点击率分布数据
clickrate = {
    1: 0.42134,
    2: 0.11897,
    3: 0.08498,
    4: 0.0606,
    5: 0.04916,
    6: 0.0405,
    7: 0.03412,
    8: 0.03014,
    9: 0.02849,
    10: 0.02995,
}

ERROR_LOG_PATH = './data/error_log.txt'

file = open('./data/refrigerator_search_result' + '.txt', mode='a', encoding='utf-8')
# error_log = open(ERROR_LOG_PATH, mode='a', encoding='utf-8')

threshold = 1071

#  headers info
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}


def get_real_source_url(src_url):
    """
    transform the baidu site  url to original site url
    :return:
    """
    if not src_url: return None
    baidu_url = requests.get(url=src_url, headers=headers, allow_redirects=False)
    real_url = None  # 得到网页原始地址
    if "Location" in baidu_url.headers: real_url = baidu_url.headers['Location']
    return real_url


def read_excel_file():
    """
    read excel file :get row value
    :return:
    """
    wb = xlrd.open_workbook("./data/refrigerator_keywords_4_search_src.xls")
    sheet = wb.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        if i <= threshold: continue
        sleep_if_need(i)
        curr_row = sheet.row_values(i)  # 0-6的字段名   curr_row[1]
        print(str(i) + "--->" + curr_row[1])
        try:
            baidu_search(curr_row[1])
        except:
            # print(data)
            error_log.write(str(i) + "--->" + curr_row[1] + "\n")


def sleep_if_need(i):
    randint = random.randint(5, 15)
    if i % 20 == 0:
        print('===============1:睡', randint, '秒===================')
        time.sleep(randint)
    if i % 100 == 0:
        print('===============2:睡', randint, '秒=================')
        time.sleep(randint)


def rerun_error_log():
    """
    rerun
    :return:
    """
    i = 0
    with open(ERROR_LOG_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            i += 1
            line = line.replace("\n", "")
            sleep_if_need(i)
            arr = line.split("--->")
            try:
                baidu_search(arr[1])
                print("success:--->" + line)
            except:
                print("error:--->" + line)


def process_result_json():
    """
    process result json data
    :return:
    """
    with open('./data/refrigerator_search_result.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        json_result = json.loads(line)
        print(json_result)


# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
# data = {'url': {'id': '', 'score': '', 'id': 'key_num', }}


def build_json_body(origin, real_url, src_url, title, keyword, score, curr_index, total_index, delta, time):
    """
    build the json result
    :return:
    """
    result_json = {
        'origin': origin,
        'real_url': real_url,
        'src_url': src_url,
        'title': title,
        'keyword': keyword,
        'score': score,
        'curr_index': curr_index,
        'total_index': total_index,
        'delta': delta,
        'time': time,
    }
    return result_json


def result_save(data):
    """
    save the result
    :param data:
    :return:
    """
    if True:
        # print(data)
        file.write(json.dumps(data) + "\n")
    else:
        print("保存失败")


def baidu_search(keyword):
    """
    remove some redundant item such as ads and statistics
    total_index and curr_index begin with 1
    :param keyword:
    :return:
    """
    data = spider.search_web(query=keyword)
    delta = 0
    data_list = data['results']
    total_index = len(data_list)
    for i in range(len(data_list)):
        data_item = data_list[i]
        data_type = data_item['type']
        if type and (data_type == 'total' or data_type == 'related' or data_type == 'news'):
            delta += 1
            continue
        origin = None
        if "origin" in data_item and data_item['origin']:
            origin = str(data_item['origin'])
            if not origin.__contains__("知乎"): continue
        curr_index = i + 1 - delta
        src_url = None
        if "url" in data_item: src_url = data_item['url']
        title = None
        if "title" in data_item: title = data_item['title']
        data_time = None
        if "time" in data_item: data_time = data_item['time']
        data = build_json_body(origin, get_real_source_url(src_url), src_url, title, keyword,
                               cal_score(curr_index), curr_index,
                               total_index, delta, data_time)
        result_save(data)


def cal_score(curr_index):
    """
    calculate score of one page
    :param curr_index:
    :return:
    """
    if clickrate[curr_index]:
        return clickrate[curr_index]


def process():
    print("begin to process")
    read_excel_file()


if __name__ == '__main__':
    print("start")
    # process()
    rerun_error_log()
