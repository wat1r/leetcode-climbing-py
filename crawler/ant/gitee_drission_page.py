from DrissionPage import ChromiumPage
from DrissionPage._functions.by import By
from DrissionPage import ChromiumOptions, ChromiumPage
from requests import request


def gitee():
    page = ChromiumPage()
    page.get('https://gitee.com/explore/all')  # 访问网址，这行产生的数据包不监听
    page.listen.start('gitee.com/explore')  # 开始监听，指定获取包含该文本的数据包
    for _ in range(5):
        next_page_ele = page.ele((By.XPATH, '//a[@rel="next"]'))
        next_page_ele.click(timeout=2, by_js=True)  # 点击下一页
        res = page.listen.wait()  # 等待并获取一个数据包
        print(res.url)  # 打印数据包url


co = ChromiumOptions().set_load_mode('none')
page = ChromiumPage(co)


def douban():
    #
    page.get('https://movie.douban.com/top250')  # 访问网址，这行产生的数据包不监听
    page.listen.start('movie.douban.com')  # 开始监听，指定获取包含该文本的数据包
    for _ in range(5):
        next_page_ele = page.ele((By.XPATH, '//span[@class="next"]'))
        next_page_ele.click(timeout=2, by_js=True)  # 点击下一页
        res = page.listen.wait()  # 等待并获取一个数据包
        print(res.url)  # 打印数据包url
        requestId = res.response.extra_info.all_info['requestId']
        # 39764.994
        # storage = page.session_storage()
        # page.get
        cdp = page.run_cdp('Network.getResponseBody', **{"requestId": requestId})

        print(cdp)
        # r = request('GET', url=res.url)
        # print(r)


if __name__ == '__main__':
    # gitee()
    douban()
