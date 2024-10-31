import json

import mitmproxy.http as http
from mitmproxy import ctx


class HTTPRecordModifier:

    def __init__(self, flow: http.HTTPFlow):
        self.flow = flow

    # 设置请求头信息
    def set_request_header(self, headers):
        for header_key, header_value in headers.items():
            self.flow.request.headers[header_key] = header_value

    # 设置请求 body 参数
    def set_request_body(self, body):
        self.flow.request.content = bytes(body, "utf-8")

    # 设置请求方法
    def set_request_method(self, method):
        self.flow.request.method = method

    # 设置请求 query 参数
    def set_request_query(self, key, value):
        self.flow.request.query[key] = value

    # 设置响应状态码
    def set_response_status_code(self, code):
        self.flow.response.status_code = code

    # 设置响应头信息
    def set_response_header(self, headers):
        for header_key, header_value in headers.items():
            self.flow.response.headers[header_key] = header_value

    # 设置响应体内容
    def set_response_body(self, body):
        self.flow.response.content = bytes(body, "utf-8")

    # 构造响应报文
    def create_mocked_response(self, code=200, header={}, body=""):
        self.flow.response = http.HTTPResponse.make(code, bytes(body, "utf-8"), header)


class Test:

    def response(self, flow: http.HTTPFlow):
        """
        Event for handling response before sending it back to the client
        """
        # 这里编写我们的 mock 逻辑代码
        breakpoint_url1 = "alipayobjects.com"
        breakpoint_url2 = "alipay.com"
        url = flow.request.pretty_url
        print("================url->", url)
        if str(url).__contains__(breakpoint_url1) or str(url).__contains__(breakpoint_url2):
            response_data = flow.response
            response_header = response_data.headers
            content_type = response_header['Content-Type']
            if 'image' in content_type:
                print('这里返回的是图片')
            else:
                print('content_type---------------->', content_type)
                print('code------------>', response_data.status_code)
                print('res_data-------------------->', response_data.text)
            # response_content = json.loads(flow.response.content.decode("utf-8"))
            # print("=========response_content", response_content)
            # response_content['total'] = 20
            # resp = json.loads(flow.response.text)
            # print("=========resp:", flow.response.text)
            # new_response = HTTPRecordModifier(flow)
            # print("=========new_response:", new_response)
            userinfo = {
                # 这里放置上面抓包获取的用户信息格式
            }

            # for i in range(response_content['total']):
            #     response_content['users'].append(userinfo)
            # new_response.set_response_body(json.dumps(response_content))


addons = [
    Test()
]
