from DrissionPage import ChromiumPage, ChromiumOptions, SessionPage
from DrissionPage.common import Settings
import time

from utils import read_cookies, save_cookies
from config import read_config_file, Config

Settings.raise_when_ele_not_found = True


# # co = ChromiumOptions().auto_port()
# page = ChromiumPage(timeout=1)
# # co = ChromiumOptions().set_local_port(9111)
# # page = ChromiumPage(co)
# # print("init port:")
#
# ENTRANCE_URL = "https://s.alipay.com/"
# USER_NAME = "mbdly2008@163.com"
# PASSWORD = "mon1day!"


class AlipayBot:

    def __init__(self, cfg: Config):
        self.cfg = cfg
        options = ChromiumOptions()
        options.incognito(True)
        # options.set_argument('--window-size', '640,960')
        options.set_pref(arg='profile.default_content_settings.popups', value='0')
        self.page = ChromiumPage(options)
        options.ignore_certificate_errors(True)
        options.mute(True)
        options.set_user_agent(user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) '
                                          'AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.6261.62 Mobile/15E148'
                                          ' Safari/604.1')
        options.no_imgs(True)
        self.login_url = self.cfg.entrance_url

    def check_login_state(self):
        """
        :return:
        """
        cookies = read_cookies(self.cfg.cookie_filepath)
        if cookies is None:
            return False
        self.page.set.cookies(cookies)

        # 监听cookie的接口 https://collect.alipay.com/dwcookie?biztype=common&eventid=clicked&productid=PC&spmAPos=a710
        self.page.listen.start(self.cfg.entrance_url)
        self.page.get(self.cfg.entrance_url)

        print('检测登录状态中...')
        res = self.page.listen.wait(timeout=5)
        try:
            data = res.response.body['data']
            # nickname = data['nickname']
            # user_id = data['userId']
            # print(f"登录成功,\n\t用户ID: {nickname}\n\t用户昵称:{user_id}\n")
            return True
        except KeyError as _:
            pass
        except TypeError as _:
            pass

        return False

    """
    转换content内容为去html格式的内容
    抠出里面的图片，存储到蚂蚁的服务器，换一个图片地址
    """

    def transform_content(content: str):
        pass

    def account_login(self):
        self.page.get(self.cfg.entrance_url)
        life_btn = self.page('登录生活号(内容)', timeout=2)
        if life_btn:
            life_btn.click()
            self.page.wait.load_start()
        else:
            print("当前的life_btn未找到")

        account_login_entrance = self.page.ele('#J-qrcode-target')
        if account_login_entrance:
            account_login_entrance.click()
            self.page.wait.load_start()
        else:
            print("当前的account_login_entrance button未找到")
        pass
        # 定位到账号文本框并输入账号
        self.page.ele('#J-input-user', timeout=2).input(self.cfg.username)
        # 定位到密码文本框并输入密码
        self.page.ele('#password_rsainput', timeout=2).input(self.cfg.password)
        # 登录的按钮
        login_btn = self.page.ele('#J-login-btn', timeout=2)
        if login_btn:
            # login_btn.click()
            # page.wait.load_start()
            print("------")
        else:
            print("当前的login_btn button未找到")
        # 存储cookie
        # res = self.page.listen.wait()
        # # self.page.ele(f'')
        # # 'data-aspm-click="switchAccount"'
        # nickname = res.response.body['data']['nickname']
        # user_id = res.response.body['data']['userId']
        # print(f"登录成功,\n\t用户ID: {nickname}\n\t用户昵称:{user_id}\n")
        # cookies = self.page.cookies()
        # save_cookies(data=cookies, filepath=self.cfg.cookie_filepath)

    def qr_code_login(self):
        pass

    def write(self, data=""):
        creative_content_btn = self.page.ele('xpath://*[@id="J-sidenav"]/ul/li[2]/ul/li[2]/a')
        if not creative_content_btn:
            print("当前的creative_content_btn未找到")
            return
        creative_content_btn.click()
        self.page.wait.load_start()

        creative_right_now_btn = self.page.ele('xpath://*[@id="react-root"]/div/ul/li[1]/div/div[1]/div[3]/a/button')
        creative_right_now_btn.click(timeout=2)

        self.page.wait.load_start()

        title_input = self.page.ele(
            'xpath://*[@id="react-root"]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[1]/span/input')
        # title_input.input()

        abstract_input = self.page.ele(
            'xpath://*[@id="react-root"]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/textarea')

        # page.to_tab(page.latest_tab)
        # page.wait.load_start()
        content_input = self.page.ele(
            'xpath://*[@id="react-root"]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[2]')

        next_step_btn = self.page.ele('xpath://*[@id="react-root"]/div/div/div/div[1]/div[2]/div/div/div/div/button[3]')
        next_step_btn.click(timeout=1)

        publish_btn = self.page.ele('xpath://*[@id="react-root"]/div/div/div/div[1]/div[2]/div/div/div/div/button[3]')
        publish_btn.click(timeout=2)

        pass

    """
    上传图片/视频
    """

    def upload(self):
        image_btn = self.page.ele(
            'xpath://*[@id="react-root"]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/button[1]')
        image_btn.click(timeout=1)
        self.page.wait.load_start()

        using_image_btn = self.page.ele('xpath:/html/body/div[19]/div/div[2]/div/div[2]/div[3]/div/button[2]')
        using_image_btn.click(timeout=1)

        pass

    def start(self):
        if not self.check_login_state():
            self.account_login()
        self.write()


if __name__ == '__main__':
    conf = read_config_file('.config.yml')
    app = AlipayBot(conf)
    app.start()
    # page.quit()
