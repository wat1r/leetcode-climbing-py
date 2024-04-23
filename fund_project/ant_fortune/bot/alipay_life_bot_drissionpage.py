from DrissionPage import ChromiumPage,ChromiumOptions

# co = ChromiumOptions().auto_port()
page = ChromiumPage()
# co = ChromiumOptions().set_local_port(9111)
# page = ChromiumPage(co)
# print("init port:")

ENTRANCE_URL = "https://s.alipay.com/"
USER_NAME = "mbdly2008@163.com"
PASSWORD = ""

"""
转换content内容为去html格式的内容
抠出里面的图片，存储到蚂蚁的服务器，换一个图片地址
"""


def transform_content(content: str):
    pass


def login():
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
    login_btn = page.ele('#J-login-life_btn', timeout=2)
    if login_btn:
        # login_btn.click()
        # page.wait.load_start()
        print("------")
    else:
        print("当前的login_btn button未找到")


def main():
    # 登录
    login()

    # 退出浏览器
    page.quit()

if __name__ == '__main__':
    # page.quit()
    main()
