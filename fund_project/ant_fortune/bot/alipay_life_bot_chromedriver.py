from selenium import webdriver
import time
driver = webdriver.Chrome()

ENTRANCE_URL = "https://s.alipay.com/"
USER_NAME = "mbdly2008@163.com"
PASSWORD = "mon1day!"

"""
转换content内容为去html格式的内容
抠出里面的图片，存储到蚂蚁的服务器，换一个图片地址
"""


def transform_content(content: str):
    pass


def login():
    driver.get(ENTRANCE_URL)
    time.sleep(3)
    pass


def main():
    # 登录
    login()

    # 退出
    driver.quit()


if __name__ == '__main__':
    # page.quit()
    main()
