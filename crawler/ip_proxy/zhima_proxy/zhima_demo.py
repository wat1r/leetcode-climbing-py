import requests
import re


def ip_proxy():
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
        print(resp.status_code, proxyHost, checkip(proxyHost))
        # print(resp.text)


def checkip(ip):
    r = requests.get('https://ip.taobao.com//outGetIpInfo?ip=%s' % ip)
    if r.json()['code'] == 0:
        i = r.json()['data']
        city = i['city']
        print(city)
    else:
        print('未查到归属地')


# def checkip2(ip):
#     url = f'http://ip.17mon.cn/api/getip.php?ip={ip}&type=1'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print('查询失败')

def checkip3(ip):
    URL = 'http://freeipapi.17mon.cn/' + ip
    try:
        r = requests.get(URL, timeout=3)
    except requests.RequestException as e:
        print(e)
    json_data = r.json()
    print('所在国家：' + json_data[0].encode('utf-8'))
    print('所在省份：' + json_data[1].encode('utf-8'))
    print('所在城市：' + json_data[2].encode('utf-8'))
    return (ip)


if __name__ == '__main__':
    ip_proxy()
