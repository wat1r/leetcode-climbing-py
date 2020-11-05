from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import pymongo
from urllib.parse import quote
import time
import sys

import random

browser = webdriver.Chrome()  # 初始化浏览器
wait = WebDriverWait(browser, 30)  # 指定延时时间

# 连接数据库，数据库的初始化
"""
需要保存的数据：                       提取表达式
goods_name：商品的名称             #mainsrp-itemlist a>span
price: 价钱                        #mainsrp-itemlist .price>strong
people: 购买人数                   #mainsrp-itemlist .item 
shop_name: 商店名称
location ： city
"""

# 数据库连接
# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client['taobao']  # 使用的数据库是中括号
# collection = db['ipad']  # 使用的集合 也是中括号

key_word = '20201105_skin_comments'
file = open(key_word + '.txt', mode='w')


def page_get(page):
    if (page > 100):
        sys.exit(0)
    """
      首先获得一个产品的信息，然后存入数据库
    """
    print('正在爬取第', page, '页')
    if (page % 10 == 0):
        randint = random.randint(40, 80)
        print('===============睡', randint, '秒===================')
        time.sleep(randint)
    try:
        # url = "https://s.taobao.com/search?q=" + quote(key_word)
        url = "https://item.taobao.com/item.htm?spm=a230r.1.14.2.61539c14EEPlui&id=613889135290&ns=1&abbucket=13#detail"
        browser.get(url)  # 连接淘宝网
        comment_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_TabBar > li.selected > a')))
        comment_tab.click()  #
        # time.sleep(5)  #
        # sort_sales = wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_relative > div.sort-row > div > ul > li:nth-child(2)')))
        # sort_sales.click()  # 点击提交按钮 #J_relative > div.sort-row > div > ul > li:nth-child(2)
        print('连接成功')
        item_info()
    except TimeoutException:
        page_get(page)


# 获取信息
def item_info():
    html = browser.page_source  # 获取html
    doc = pq(html)
    print("获取成功")
    lis = 'doc.find('#reviews > div > div > div > div > div > div.tb-revbd > ul > li')
    # print('这一页商品的的个数是', len(doc('#mainsrp-itemlist .item')), '件')
    for i in range(lis.size()):
        curr_li = lis[i]

        print()

        # result_save(None)  # 存储


def result_save(data):
    if True:
        print(data)
        file.write(str(data) + "\n")
    else:
        print("保存失败")


def main():
    print("working")
    for page in range(1, 101):
        page_get(page)


if __name__ == '__main__':
    main()
