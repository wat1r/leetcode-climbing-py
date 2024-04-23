from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.common import Settings
import time

Settings.raise_when_ele_not_found = True

# co = ChromiumOptions().auto_port()
page = ChromiumPage(timeout=1)
# co = ChromiumOptions().set_local_port(9111)
# page = ChromiumPage(co)
# print("init port:")

ENTRANCE_URL = "https://s.alipay.com/"
USER_NAME = "mbdly2008@163.com"
PASSWORD = "mon1day!"

"""
转换content内容为去html格式的内容
抠出里面的图片，存储到蚂蚁的服务器，换一个图片地址
"""


def transform_content(content: str):
    pass


def account_login():
    page.get(ENTRANCE_URL)
    life_btn = page('登录生活号(内容)', timeout=2)
    if life_btn:
        life_btn.click()
        page.wait.load_start()
    else:
        print("当前的life_btn未找到")

    account_login_entrance = page.ele('#J-qrcode-target')
    if account_login_entrance:
        account_login_entrance.click()
        page.wait.load_start()
    else:
        print("当前的account_login_entrance button未找到")
    pass
    # 定位到账号文本框并输入账号
    page.ele('#J-input-user', timeout=2).input(USER_NAME)
    # 定位到密码文本框并输入密码
    page.ele('#password_rsainput', timeout=2).input(PASSWORD)
    # 登录的按钮
    login_btn = page.ele('#J-login-btn', timeout=2)
    if login_btn:
        # login_btn.click()
        # page.wait.load_start()
        print("------")
    else:
        print("当前的login_btn button未找到")


def qr_code_login():
    pass


def write(data=""):
    creative_content_btn = page.ele('xpath://*[@id="J-sidenav"]/ul/li[2]/ul/li[2]/a')
    if not creative_content_btn:
        print("当前的creative_content_btn未找到")
        return
    creative_content_btn.click()
    page.wait.load_start()

    creative_right_now_btn = page.ele('xpath://*[@id="react-root"]/div/ul/li[1]/div/div[1]/div[3]/a/button')
    creative_right_now_btn.click(timeout=2)

    page.wait.load_start()

    title_input = page.ele(
        'xpath://*[@id="react-root"]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[1]/span/input')
    # title_input.input()

    abstract_input = page.ele(
        'xpath://*[@id="react-root"]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/textarea')

    # page.to_tab(page.latest_tab)
    # page.wait.load_start()
    content_input = page.ele(
        'xpath://*[@id="react-root"]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[2]')

    next_step_btn = page.ele('xpath://*[@id="react-root"]/div/div/div/div[1]/div[2]/div/div/div/div/button[3]')
    next_step_btn.click(timeout=1)

    publish_btn = page.ele('xpath://*[@id="react-root"]/div/div/div/div[1]/div[2]/div/div/div/div/button[3]')
    publish_btn.click(timeout=2)

    pass


"""
上传图片/视频
"""


def upload():
    image_btn = page.ele(
        'xpath://*[@id="react-root"]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/button[1]')
    image_btn.click(timeout=1)
    page.wait.load_start()

    using_image_btn = page.ele('xpath:/html/body/div[19]/div/div[2]/div/div[2]/div[3]/div/button[2]')
    using_image_btn.click(timeout=1)

    pass


def main():
    # 登录
    account_login()

    # 退出浏览器
    page.quit()


if __name__ == '__main__':
    # page.quit()
    main()
