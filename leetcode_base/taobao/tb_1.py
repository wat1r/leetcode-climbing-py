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

# key_word = '电子美容仪'
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
        url = "https://s.taobao.com/search?q=" + quote(key_word)
        browser.get(url)  # 连接淘宝网

        """
        in_put = browser.find_element(By.CSS_SELECTOR, '#mainsrp-pager .form>input')  #输入框
        submit = browser.find_element(By.CSS_SELECTOR, '#mainsrp-pager .form>.btn')   #提交按钮
        """
        in_put = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager .form>input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager .form>.btn')))
        in_put.clear()  # 清空输入信息， 每次都要
        in_put.send_keys(page)  # 输入信息
        submit.click()  # 点击提交按钮
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
    items = doc('#mainsrp-itemlist .item').items()  # 形成可迭代列表
    print('这一页商品的的个数是', len(doc('#mainsrp-itemlist .item')), '件')

    # 遍历获取商品的信息
    for item in items:
        is_tmall = ""
        is_tmall_item = item.find('.icon .icon-service-tianmao')
        standard = "尚天猫，就购了"
        is_equal = is_tmall_item.attr('title') == standard or (
                is_tmall_item.parent() is not None and is_tmall_item.parent().attr('title') == standard)
        if is_tmall_item is not None and is_equal:
            is_tmall = "天猫"
        items_info = {
            'name': item.find('.row-2').text(),
            'price': item.find('.price>strong').text(),
            'deal-cnt': item.find('.deal-cnt').text(),
            'shop_name': item.find('.row-3 a').text(),
            'location': item.find('.row-3 .location').text(),
            'is_tmall': is_tmall,
            'url': item.find('.title .J_ClickStat').attr('href'),
            'comment': item.find('.comment').text(),
        }
        # 一件商品的信息提取完毕
        result_save(items_info)  # 存储


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
