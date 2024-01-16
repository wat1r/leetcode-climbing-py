import base64
import json
import requests

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

key_word = 'field_detail_20240112'
file = open(key_word + '.txt', mode='w', encoding='utf-8')


def demo_test():
    # 1、创建Chrome实例 。
    driver = webdriver.Chrome()
    # 2、driver.get方法将定位在给定的URL的网页 。
    driver.get("https://www.baidu.com/")  # get接受url可以是如何网址，此处以百度为例
    # 3、定位元素 。
    # 3.1、用id定位输入框对象，
    driver.find_element_by_id("kw").send_keys("python")
    # 3.2、用id定位点击对象，用click()触发点击事件
    driver.find_element_by_id('su').click()
    time.sleep(3)  # 延迟3秒
    # 4、退出访问的实例网站。
    driver.quit()


def process2():
    # 1、创建Chrome实例 。
    driver = webdriver.Chrome()
    _url = 'http://116.211.22.80/'
    driver.get(_url)
    time.sleep(3)

    user_input = driver.find_element(by=By.XPATH, value='//*[@id="login"]/div[5]/div/div/form/div[1]/div/div/input')
    pwd_input = driver.find_element(by=By.XPATH, value='//*[@id="login"]/div[5]/div/div/form/div[2]/div/div/input')
    login_btn = driver.find_element(by=By.XPATH, value='//*[@id="login"]/div[5]/div/div/form/div[3]/div/div[1]')

    # 输入用户名和密码，点击登录
    user_input.send_keys('a****')
    pwd_input.send_keys('a******3')
    time.sleep(1)
    login_btn.click()
    time.sleep(2)

    c_1 = driver.find_element(by=By.XPATH, value='//*[@id="menu"]/ul/li[3]/div/span[2]')
    c_1.click()
    time.sleep(2)
    c_1_1 = driver.find_element(by=By.XPATH, value='//*[@id="menu"]/ul/li[3]/ul/li[1]')
    c_1_1.click()
    time.sleep(2)

    first = driver.find_element(by=By.XPATH,
                                value='//*[@id="classify-task"]/div[3]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[11]/div/button[2]/span')
    first.click()
    time.sleep(2)

    field = driver.find_element(by=By.XPATH, value='//*[@id="tab-fieldDetail"]')
    field.click()
    time.sleep(2)

    down_select = driver.find_element(by=By.XPATH,
                                      value='//*[@id="pane-fieldDetail"]/div/div[2]/div/span[2]/div/div/span/span/i')
    down_select.click()
    time.sleep(2)

    two_hundred = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[1]/div[1]/ul/li[7]/span")
    two_hundred.click()
    time.sleep(2)

    page_top_ele = driver.find_element(By.CLASS_NAME, value='el-pagination__total')
    reg = re.compile(r'共|条|\s')
    page_top = reg.sub('', page_top_ele.text)
    which_page = driver.find_element(by=By.XPATH, value='//*[@id="pane-fieldDetail"]/div/div[2]/div/span[3]/div/input')
    which_page.clear()
    which_page.send_keys('45045')
    time.sleep(2)
    next_page = driver.find_element(by=By.XPATH, value='//*[@id="pane-fieldDetail"]/div/div[2]/div/button[2]/i')
    next_page.click()

    current_page = int(driver.find_element(by=By.CLASS_NAME, value='number.active').text)

    page_index = current_page
    # page_top =58950
    page_top = int(page_top)
    while page_index <= page_top:
        print("===================page:", page_index)
        tr_eles = driver.find_element(By.XPATH,
                                      value='//*[@id="pane-fieldDetail"]/div/div[1]/div[3]/table/tbody').find_elements(
            By.TAG_NAME, value='tr')
        if tr_eles:
            flag = False
            for i in range(len(tr_eles)):
                td_eles = tr_eles[i].find_elements(By.TAG_NAME, 'td')
                if td_eles:
                    line_data = []
                    for j in range(2, max(2, len(td_eles))):
                        final_text = td_eles[j].text.replace("\t", " ").replace("\n", " ")
                        line_data.append(final_text)
                    if line_data:
                        try:
                            file.write(str('\t'.join(line_data)) + "\n")
                        except:
                            print("error:--->" + page_index)
                            flag = True
            if flag:
                continue
        next_page = driver.find_element(by=By.XPATH, value='//*[@id="pane-fieldDetail"]/div/div[2]/div/button[2]/i')
        next_page.click()
        page_index += 1
    print()


def process1():
    url = "http://116.211.22.80/dcgapiserver/api/task/column/page/list?page=1&size=10&task_id=6&order_by=1&field_comment=&assets_name=&db_name=&table_name="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': 'TGC=TGT-57fe84a9f3964c5f87583401521a6669; JSESSIONID=462CD8A0F85B784E658AB6AA861890CE; session=MTcwNDk3MTY0NXxEdi1CQkFFQ180SUFBUkFCRUFBQV81bl9nZ0FFQm5OMGNtbHVad3dLQUFoMWMyVnlUbUZ0WlFaemRISnBibWNNQndBRllXUnRhVzRHYzNSeWFXNW5EQVlBQkhWMWFXUUdjM1J5YVc1bkRDWUFKRFpoT1RBek9EQXdMVEJqWlRRdE5EQmhNQzA0TURRMUxXTmtPR014T0RjNVl6VXpNd1p6ZEhKcGJtY01CZ0FFY205c1pRVnBiblEyTkFRQ0FBSUdjM1J5YVc1bkRBZ0FCblZ6WlhKSlpBVnBiblEyTkFRQ0FBST18C_lqkTn8Cb1yAn6KN6PZIoZNw27jqCOQ2ftubKoVQoA=',
        'Sign-Txt': '3efafa7e5d05b3ae5cfe802a14b7e559'
    }
    resp = requests.get(url=url, headers=headers).json()

    print(resp)


def login():
    s = '共 589494 条'
    reg = re.compile(r'共|条|\s')
    page_top = reg.sub('', s)

    print()


if __name__ == '__main__':
    # pwd = get_pwd()
    # process1()
    # demo_test()
    process2()
    # login()
    print()
