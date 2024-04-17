# 如果只要控制浏览器，导入ChromiumPage。
from DrissionPage import ChromiumPage
# 如果只要收发数据包，导入SessionPage。
from DrissionPage import SessionPage
# WebPage是功能最全面的页面类，既可控制浏览器，也可收发数据包。
from DrissionPage import WebPage
from mitmproxy import ctx




def test1():
    # 创建对象
    page = ChromiumPage()
    # 访问网页
    page.get('https://www.baidu.com')
    # 输入文本
    page('#kw').input('DrissionPage')
    # 点击按钮
    page('#su').click()
    # 等待页面跳转
    page.wait.load_start()
    # 获取所有结果
    links = page.eles('tag:h3')
    # 遍历并打印结果
    for link in links:
        print(link.text)


def mitm_dump_test():
    print("")


# def request(flow):
#     flow.request.headers['User-Agent'] ＝'mitmProxy'
#     ctx.log.info(str(flow.request.headers))
#     ctx.log.warn(str(flow.request.headers))
#     ctx.log.error(str(flow.request.headers))


if __name__ == '__main__':
    test1()