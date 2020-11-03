from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import pymongo
from bs4 import BeautifulSoup
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

key_word = '祛斑'
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
        if page >= 2:

            # #waci-wrap > div:nth-child(5) > ul > li:nth-child(10) > a

            # next_page = wait.until(EC.element_to_be_clickable(
            #     (By.CSS_SELECTOR, '#waci-wrap > div:nth-child(5) > ul > li:nth-child(10) > a')))
            # EC.element_to_be_clickable
            next_page = browser.find_element_by_xpath('//a[@aria-label="Next"]')
            next_page.click()
            time.sleep(3)
            # add_time = str(int(round(time.time() * 1000)))
            # url_2 = "https://www.5118.com/seo/newwords/1956b597/?isPager=true&pageIndex=" + str(
            #     page) + "&sortfields=&filters=&filtersName=&addTime=&_=" + add_time
            # browser.get(url_2)  # 连接淘宝网
        else:
            url = "https://www.5118.com/seo/newwords/1956b597"
            browser.get(url)  # 连接淘宝网

        """
        in_put = browser.find_element(By.CSS_SELECTOR, '#mainsrp-pager .form>input')  #输入框
        submit = browser.find_element(By.CSS_SELECTOR, '#mainsrp-pager .form>.btn')   #提交按钮
        """
        # in_put = wait.until(EC.presence_of_element_located(
        #     (By.CSS_SELECTOR, '#app > div.container-fluid.j-container-fluid > div > div.search-box')))
        # submit = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, '#app > div.container-fluid.j-container-fluid > div > div.search-box > form > button')))
        # # in_put.clear()  # 清空输入信息， 每次都要
        # in_put.send_keys(key_word)  # 输入信息
        # submit.click()  # 点击提交按钮
        # time.sleep(5)  #
        # sort_sales = wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_relative > div.sort-row > div > ul > li:nth-child(2)')))
        # sort_sales.click()  # 点击提交按钮 #J_relative > div.sort-row > div > ul > li:nth-child(2)
        print('连接成功')
        item_info()
    except TimeoutException:
        page_get(page)


def item_info():
    html = browser.page_source  # 获取html
    doc = pq(html)
    print("获取成功")
    soup = BeautifulSoup(str(doc), 'lxml')
    trs = soup.select("#waci-wrap > div.list-table-content > table > tbody > tr")
    for tr in trs:
        tds = tr.select('td')

        img_item = tds[1].find_all('img')
        src = ''
        if img_item:
            src = img_item[0].get('src')
        word = tds[0].find('a').text
        company_cnt = tds[2].find('a').text
        long_tail = tds[3].find('a').text
        # td[0]
        items_info = {
            'word': word,
            'src': src,
            'company_cnt': company_cnt,
            'long_tail': long_tail,
        }
        # https://www.5118.com/seo/newwords/1956b597?isPager=true&pageIndex=2&sortfields=&filters=&filtersName=&addTime=&_=1598451345298
        result_save(items_info)  # 存储


# 获取信息
def item_info_origin():
    html = browser.page_source  # 获取html
    doc = pq(html)
    print("获取成功")

    items = doc('#waci-wrap > div.list-table-content > table > tbody > tr').items()  # 形成可迭代列表
    print('这一页商品的的个数是', len(doc('#mainsrp-itemlist .item')), '件')

    # soup = BeautifulSoup(doc, 'lxml')

    # 遍历获取商品的信息
    idx = 1
    for item in items:
        tds = item.find("td")
        img_item = doc(
            '#waci-wrap > div.list-table-content > table > tbody > tr:nth-child(' + str(
                idx) + ') > td:nth-child(2) > img')
        src = ''
        if img_item:
            src = img_item.attr('src')
        word = tds[0].find('a').text
        company_cnt = tds[2].find('a').text
        long_tail = tds[3].find('a').text
        # td[0]
        items_info = {
            'word': word,
            'src': src,
            'company_cnt': company_cnt,
            'long_tail': long_tail,
        }
        # 一件商品的信息提取完毕
        idx += 1
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
