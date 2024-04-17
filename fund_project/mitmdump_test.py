import mitmproxy.http
from mitmproxy import ctx


class Interceptor:
    def __init__(self):
        ctx.log.info("init")

    def request(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("request() called")

    def response(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("response() called")


addons = [
    Interceptor()
]

# class Demo:
#     def request(self, flow: mitmproxy.http.HTTPFlow):
#         request = flow.request
#         # https://www.baidu.com/s?ie=utf-8
#         if 'https://www.baidu.com/s?ie=utf-8' in request.url:
#             print('我输入的搜索关键词：', request.query.get('wd'))
#
#             request.query.set_all('wd', ['华为Mate60'])
#             print('修改后的搜索关键词：', request.query.get('wd'))
#
#
# addons = [
#     Demo()
# ]
