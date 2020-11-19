# from openpyxl import load_workbook
import requests
import xlrd
import json

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

# 定义头文件，伪装成浏览器
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}


# 获取百度链接的真实源地址
# href = {str} 'https://www.baidu.com/link?url=gCQcWkErExKXSzK_LW_hVotcyJfh3qvF282lT00V3-plCGVMuVdqcaM5PBHm_1udhw2Kk6MVXdV-oDq3EZPvrK&amp;wd=&amp;eqid=af674e0d0000476c000000045fb51ddc'
# real_url = {str} 'https://www.zhihu.com/question/21122897'
def get_real_source_url():
    href = "https://www.baidu.com/link?url=gCQcWkErExKXSzK_LW_hVotcyJfh3qvF282lT00V3-plCGVMuVdqcaM5PBHm_1udhw2Kk6MVXdV-oDq3EZPvrK&amp;wd=&amp;eqid=af674e0d0000476c000000045fb51ddc"
    baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
    real_url = baidu_url.headers['Location']  # 得到网页原始地址
    if real_url.startswith('http'):
        print("dd")


def read_excel_file():
    """
    read excel file :get row value
    :return:
    """
    wb = xlrd.open_workbook(
        "D:\\Dev\\SrcCode\\leetcode-climbing-py\\get_bonus_idea\\zhihu_fine_goods\\data\\refrigerator_keywords_4_search_src.xls")
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
    result_json = {
        'url': '',
        'score': '',
        'keyword': '',
    }


def result_save(data):
    if True:
        print(data)
        file.write(str(data) + "\n")
    else:
        print("保存失败")


print("end")

if __name__ == '__main__':
    print("start")
    # get_real_source_url()
    # read_excel_file()
    test_json()
