import http.client
import requests
import requests as requests
import json


def process():
    url = "http://101.42.242.196"
    # conn = http.client.HTTPSConnection("101.42.242.196")
    conn = http.client.HTTPSConnection(url)
    # conn = http.client.HTTPSConnection("www.baidu.com")
    payload = {
        'keyword': "小杨哥"
    }
    headers = {
        'token': '348PUQOMjUhqzOUT'
    }
    conn.request("GET", url + "/dy/search/video/app/", payload, headers)
    # conn.request("GET", None, None, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def process_1():
    # url = "/dy/search/video/app/"
    #
    # payload = {}
    # headers = {
    #     'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)'
    # }
    # response = requests.request("GET", url, headers=headers, data=payload)

    url = "http://101.42.242.196/dy/search/video/app?keyword='小杨哥'"
    # payload = {
    #     'keyword': "小杨哥"
    # }
    params = {
        'token': '348PUQOMjUhqzOUT',
        'user_id': 'MS4wLjABAAAAZc6_2IqC89BH7xNjZ_6NO5_pQc0qUl32XSnezm5nsLE'
    }

    response = requests.request("GET", url, params=params)

    # print(json.dumps(response.content.decode('unicode-escape'), indent=4))
    print(response.content.decode('unicode-escape'))

    # print(response.text)


if __name__ == '__main__':
    # process()
    process_1()
