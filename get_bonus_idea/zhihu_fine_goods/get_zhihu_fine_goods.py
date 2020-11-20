# from openpyxl import load_workbook
import requests
import xlrd
import json
# 导入BaiduSpider
from baiduspider import BaiduSpider
from pprint import pprint

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
    10: 0.02995
}

file = open('./data/refrigerator_search_result' + '.txt', mode='a')

#  headers info
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}


def get_real_source_url():
    """
    transform the baidu site  url to original site url
    :return:
    """
    href = "http://www.baidu.com/link?url=tuzYguiCIT10b-dd1eg86SpvyYlxpxvcZShgNdVXRfx77xDQCbbW2fVdKyAIejGq5xm2u2C93Z6cEmK94yaKaa"
    baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
    real_url = baidu_url.headers['Location']  # 得到网页原始地址
    print(real_url)


def read_excel_file():
    """
    read excel file :get row value
    :return:
    """
    wb = xlrd.open_workbook("./data/refrigerator_keywords_4_search_src.xls")
    sheet = wb.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        curr_row = sheet.row_values(i)  # 0-6的字段名   curr_row[1]


def test_json():
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    # data = {'url': {'id': '', 'score': '', 'id': 'key_num', }}
    json_result = json.loads(json.dumps(data))
    print(json_result)
    print("d")


def build_json_body():
    """
    build the json result
    :return:
    """
    result_json = {
        'url': '',
        'score': '',
        'keyword': '',
    }


def result_save(data):
    """
    save the result
    :param data:
    :return:
    """
    if True:
        print(data)
        file.write(str(data) + "\n")
    else:
        print("保存失败")


def baidu_search(keyword):
    """
    remove some redundant item such as ads and statistics
    :param keyword:
    :return:
    """
    data = spider.search_web(query=keyword)
    for data_item in data['results']:
        # str(data_item['origin']).__contains__("知乎")
        # data_item['url']
        # data_item['title']
        # data_item['time']
        # total_index:
        # curr_index
        pprint(data_item)


print("end")

if __name__ == '__main__':
    print("start")
    # get_real_source_url()
    # read_excel_file()
    # test_json()
    # 搜索网页
    baidu_search("双开门冰箱推荐")
