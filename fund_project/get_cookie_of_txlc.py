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
        breakpoint_url = "https://www.tencentwm.com/"
        url = flow.request.pretty_url
        # print("================url->", url)
        if str(url).__contains__(breakpoint_url):
            cookies = flow.request.cookies
            print("cookies:", cookies)
            self.append_data("./20240529_cookies", str(cookies)+"\n")
            response_content = json.loads(flow.response.content.decode("utf-8"))
            print("=========response_content", response_content)
            response_content['total'] = 20
            new_response = HTTPRecordModifier(flow)
            print("new_response", new_response)
            userinfo = {
                # 这里放置上面抓包获取的用户信息格式
            }

            # for i in range(response_content['total']):
            #     response_content['users'].append(userinfo)
            # new_response.set_response_body(json.dumps(response_content))

    def append_data(self, file_path, data):
        try:
            with open(file_path, 'a') as file:
                file.write(data)
        except IOError as e:
            print(f"An error occurred while appending to the file: {e}")

    

addons = [
    Test()
]
