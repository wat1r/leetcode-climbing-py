import requests
import re

# 提取ip
API_URL = 'http://webapi.http.zhimacangku.com/getip?neek=321a408a&num=10&type=1&time=4&pro=0&city=0&yys=0&port=1&pack=0&ts=0&ys=0&cs=0&lb=1&sb=&pb=4&mr=3&regions=&cf=0'
resp = requests.get(API_URL)
ip = resp.text

if re.match(r'(?:(?:25[0-5]|2[0-4]\d|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)', ip) is None:
    exit("IP 不正确")

ip_arr = ip.split("\r\n")

print(ip_arr)

for ip_item in ip_arr:
    # 请求地址
    targetUrl = "https://www.baidu.com"

    # 代理服务器
    proxyHost = ip_item.split(":")[0]
    proxyPort = ip_item.split(":")[1]

    proxyMeta = "http://%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
    }

    # pip install -U requests[socks]  socks5
    # proxyMeta = "socks5://%(host)s:%(port)s" % {
    #     "host" : proxyHost,
    #     "port" : proxyPort,
    # }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }

    resp = requests.get(targetUrl, proxies=proxies)
    print(resp.status_code)
    print(resp.text)
