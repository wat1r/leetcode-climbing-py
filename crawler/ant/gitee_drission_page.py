import json
import time
import urllib.request

from DrissionPage import ChromiumPage
from DrissionPage._functions.by import By
from DrissionPage import ChromiumOptions, ChromiumPage
from requests import request
import ssl

co = ChromiumOptions().set_load_mode('none')
co.set_argument('--start-maximized')
co.set_argument('--ignore-certificate-errors')
co.set_argument('--lang=zh-CN')
# co.set_argument('goog:loggingPrefs', {'performance': 'ALL'})
#  options.add_argument('disable-infobars')
co.set_argument('--hide-crash-restore-bubble')
co.set_pref(arg='profile.default_content_settings.popups', value='0')
# co.ignore_certificate_errors(True)
co.mute(True)
co.set_user_agent(user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) '
                             'AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.6261.62 Mobile/15E148'
                             ' Safari/604.1')
# co.no_imgs(True)
page = ChromiumPage(co)


def gitee():
    page = ChromiumPage()
    page.get('https://gitee.com/explore/all')  # 访问网址，这行产生的数据包不监听
    page.listen.start('gitee.com/explore')  # 开始监听，指定获取包含该文本的数据包
    for _ in range(5):
        next_page_ele = page.ele((By.XPATH, '//a[@rel="next"]'))
        next_page_ele.click(timeout=2, by_js=True)  # 点击下一页
        res = page.listen.wait()  # 等待并获取一个数据包
        print(res.url)  # 打印数据包url


def douban():
    #
    page.get('https://movie.douban.com/top250')  # 访问网址，这行产生的数据包不监听
    page.listen.start('movie.douban.com')  # 开始监听，指定获取包含该文本的数据包
    for _ in range(5):
        res = page.listen.wait()  #
        requestId = res.response.extra_info.all_info['requestId']
        cdp = page.run_cdp('Network.getResponseBody', **{"requestId": requestId})
        next_page_ele = page.ele((By.XPATH, '//span[@class="next"]'))
        next_page_ele.click(timeout=2, by_js=True)  # 点击下一页
        res = page.listen.wait()  # 等待并获取一个数据包
        print(res.url)  # 打印数据包url
        requestId = res.response.extra_info.all_info['requestId']
        print(requestId)
        # 39764.994
        # storage = page.session_storage()
        # page.get
        # cdp = page.run_cdp('Network.getResponseBody', **{"requestId": requestId})
        cdp = page.run_cdp_loaded('Network.getResponseBody', **{"requestId": requestId})

        print(cdp)
        # r = request('GET', url=res.url)
        # print(r)


def ant_fortune():
    sub_url = r'https://s.alipay.com/life/main.htm'
    page.get(sub_url)
    # time.sleep(10)
    page.listen.start('graphicManagement')
    page.get('https://s.alipay.com/life/web/fortune/publishMng')
    packet = page.listen.wait()  # 等待数据包
    page.stop_loading()  # 主动停止加载
    body = packet.response.body
    print(body)  # 打印数据包正文
    # res = json.loads(body)
    # json.loads(json.dumps(packet.response.body))['success']
    if 'success' in body:
        if body['success']:
            if len(body['value']) > 1:
                t = body['value'][0]
                pu = AntFortuneResult(t['contentId'], t['title'], t['showAuditStatus'], t['userId'],
                                      t['publishDate'])
                # print(json.dumps(obj=pu, default=serialize()))
                print(pu)
    print("")
    pass


def download_file(src_url, file_save_path):
    """
    下载文件到本地工作目录[图片|视频]
    :param src_url: 图床url
    :param file_save_path: 存储的目录
    :return:
    """
    try:
        context = ssl._create_unverified_context()  # 创建一个不验证SSL证书的上下文
        # 创建一个不验证证书的opener
        opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
        # 安装opener
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(src_url, file_save_path)
    except Exception as e:
        print(f"download_file##Exception->：{e}")
        return None
    return file_save_path


# 自定义序列化函数
def serialize(obj):
    if isinstance(obj, AntFortuneResult):
        return {'contentId': obj.contentId, 'title': obj.title, 'showAuditStatus': obj.showAuditStatus,
                'userId': obj.userId, 'publishDate': obj.publishDate}
    raise TypeError("Type not serializable")


class AntFortuneResult:

    def __init__(self, contentId, title, showAuditStatus, userId, publishDate):
        self.contentId = contentId
        self.title = title
        self.showAuditStatus = showAuditStatus
        self.userId = userId
        self.publishDate = publishDate

    def __str__(self):
        """
        定义对象的字符串表示形式
        :return:
        """
        return f"AntFortuneResult(contentId={self.contentId}, title={self.title}, showAuditStatus={self.showAuditStatus}, userId={self.userId}, publishDate={self.publishDate})"

    def __repr__(self):
        """
        定义对象的官方字符串表示形式
        :return:
        """
        return f"AntFortuneResult(contentId={self.contentId!r}, title={self.title!r}, showAuditStatus={self.showAuditStatus!r}, userId={self.userId!r}, publishDate={self.publishDate!r})"


def format_test():
    url_body = "https://s.alipay.com/life/web/fortune/content-details?contentId=%s&source=newSee"
    url = url_body % "2021004143654415DG1c4753c2f9064f45bd39e374ddf27276"
    print(url)


if __name__ == '__main__':
    # gitee()
    # douban()
    # ant_fortune()
    # download_file()
    format_test()
    pass
