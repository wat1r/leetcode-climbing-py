import base64
import json
import os

import requests
import shutil
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

key_word = 'field_detail_20240112'
file = open(key_word + '.txt', mode='w', encoding='utf-8')

quit_set = set()


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


def process2(start_page=1):
    page_index = start_page

    try:
        # 1、创建Chrome实例 。
        driver = webdriver.Chrome()
        # 设置隐形等待时间
        driver.implicitly_wait(10)

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

        ##1873.html

        down_select = driver.find_element(by=By.XPATH,
                                          value='//*[@id="pane-fieldDetail"]/div/div[2]/div/span[2]/div/div/span/span/i')
        down_select.click()
        time.sleep(2)

        two_hundred = None
        i = start_page
        while two_hundred is None:
            two_hundred = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div[1]/ul/li[7]/span')
            print("-----:" + str(i))
            i += 1
            time.sleep(2)
        two_hundred.click()
        time.sleep(10)

        which_page = driver.find_element(by=By.XPATH,
                                         value='//*[@id="pane-fieldDetail"]/div/div[2]/div/span[3]/div/input')
        which_page.clear()
        which_page.send_keys(str(start_page))
        # driver.refresh()
        time.sleep(2)
        which_page.send_keys(Keys.ENTER)
        time.sleep(2)
        # next_page = driver.find_element(by=By.XPATH, value='//*[@id="pane-fieldDetail"]/div/div[2]/div/button[2]/i')
        # next_page.click()

        # current_page = int(driver.find_element(by=By.CLASS_NAME, value='number.active').text)
        # page_index = current_page

        # page_top =58950
        prev_file_path = None
        while page_index <= 2948:
            print("===================page:", page_index)
            curr_file_path = "new_page_data/" + str(page_index) + '.html'
            f = open(curr_file_path, mode='w', encoding='utf-8')
            f.write(driver.page_source)  # 忽略非法字符

            # driver.page_source.e
            ele = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pane-fieldDetail"]/div/div[2]/div/button[2]/i'))
            )
            # driver.find_element(By.T)

            if prev_file_path:
                retry_times = 3
                while (os.path.getsize(prev_file_path) // 1000) == (os.path.getsize(curr_file_path) // 1000) \
                        and retry_times > 0:
                    # os.remove(curr_file_path)
                    # shutil.rmtree(curr_file_path)
                    time.sleep(5)
                    f = open(curr_file_path, mode='w', encoding='utf-8')
                    f.write(driver.page_source)  # 忽略非法字符
                    retry_times -= 1
                    print("page_index:,prev_size:,curr_size:,retry_times:,equals:", page_index,
                          os.path.getsize(prev_file_path) // 1000, os.path.getsize(curr_file_path) // 1000, retry_times,
                          os.path.getsize(prev_file_path) // 1000 == os.path.getsize(curr_file_path) // 1000)
            prev_file_path = curr_file_path
            next_page = driver.find_element(by=By.XPATH, value='//*[@id="pane-fieldDetail"]/div/div[2]/div/button[2]/i')
            next_page.click()
            page_index += 1
            # 关闭文件
            try:
                f.close()
            finally:
                print("--------------close")
            if page_index % 100 == 0 and page_index not in quit_set:
                driver.quit()
                quit_set.add(page_index)
                print("return page_index:,quit_set:", page_index, quit_set)
                return page_index
    except:
        print("except: page_index")
    finally:
        print("finally: page_index")
        return page_index


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

    i = 1
    while i <= 1:
        try:
            i = process2(i)
        except:
            print("except:i")
        finally:
            i = i

    # login()
    print()
