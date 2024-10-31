def test1():
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11177',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'api.wesais.com',
        'Access-Control-Request-Method': 'POST',
        'Access-Control-Request-Headers': 'authorization,authrouter',
        'Origin': 'https://xcx.wesais.com',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://xcx.wesais.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'business_id': '10000785',
        'stadium_id': '11501',
        'ground_id': '11501001',
        'time_date': '2024-08-30',
        'request_id': 'e1adddd79c5843d4919be2be807b5cce',
    }

    response = requests.post('https://api.wesais.com/field/wxFieldBuyPlan/getList', headers=headers, data=data,
                             verify=False)

    print(f"response:{response}")


def test2():
    import requests

    headers = {
        'Host': 'api.wesais.com',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11275',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdCI6MTcyOTQ5NDIyMSwiaWQiOiIxNzI5NDk0MjIxMDQzNzIiLCJhaWQiOjEwMTAxLCJtaWQiOjQsInRpZCI6NSwicGFyYW1zIjoie1wiY29tcGFueV9pZFwiOjYxNSxcImFjY291bnRfdHlwZVwiOjMxLFwiYWNjb3VudF9pZFwiOjEwMDk2MTYsXCJtZW1iZXJfaWRcIjoxMTkyMjk4LFwic2FmZV9sXCI6MSxcInBlcnNvbm5lbF9pZFwiOjExOTIyOTh9In0._U2zpW1MBQVa0ZrhFlBoxH8TlNCDqWvn5BH-WitFO6Y',
        'Origin': 'https://xcx.wesais.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://xcx.wesais.com/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    # data = (
    #     'business_id=10000785&stadium_id=11501&sys_id=13&sku_slice=131150100100226120241023%%3A1&business_type=1301&order_from=2&'
    #     'handle_info=%%7B%%22date_str%%22%%3A%%22%%22%%7D&sales_id=0&request_id=08901e286ae0dcdc0966f4272f49f666')

    # 131150100100232120241024
    # 131150100100234120241024
    # # %3A1 %2C
    # 131150100100116120241024
    # candidates = ["131150100100234120241024", "131150100100236120241024"]
    # build_sku_slice(candidates)
    # data = {
    #     'business_id': '10000785',
    #     'stadium_id': '11501',
    #     'sys_id': '13',
    #     'sku_slice': '',
    #     'business_type': '1301',
    #     'order_from': '2',
    #     'handle_info': '%7B%22date_str%22%3A%22%22%7D',
    #     'sales_id': '0',
    #     'request_id': '73da8fcbc5516259791c6754854f0403',  # 待替换
    # }
    candidates = ["131150100100226120241024", "131150100100242120241024"]
    sku_body = build_sku_slice(candidates)
    data = f"business_id=10000785&stadium_id=11501&sys_id=13&sku_slice={sku_body}&business_type=1301&order_from=2&handle_info=%7B%22date_str%22%3A%22%22%7D&sales_id=0&request_id=73da8fcbc5516259791c6754854f0403"

    response = requests.post('https://api.wesais.com/shop/order/create', headers=headers, data=data, verify=False)

    with open('2.txt', 'wb') as f:
        f.write(response.content)


def build_sku_slice(candidates: list):
    if not candidates or len(candidates) == 0:
        return
    sku_slice = ""
    for i in range(0, len(candidates)):
        sku_slice += candidates[i] + "%3A1"
        if i != len(candidates) - 1:
            sku_slice += "%2C"
    print("sku_slice:", sku_slice)
    return sku_slice


def test3():
    import requests

    headers = {
        'Host': 'api.wesais.com',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11275',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdCI6MTcyOTU2NDQxOCwiaWQiOiIxNzI5NTY0NDE4MDEwMDEiLCJhaWQiOjEwMTAxLCJtaWQiOjQsInRpZCI6NSwicGFyYW1zIjoie1wiY29tcGFueV9pZFwiOjYxNSxcImFjY291bnRfdHlwZVwiOjMxLFwiYWNjb3VudF9pZFwiOjEwMDk2MTYsXCJtZW1iZXJfaWRcIjoxMTkyMjk4LFwic2FmZV9sXCI6MSxcInBlcnNvbm5lbF9pZFwiOjExOTIyOTh9In0.K27Fh3XXrqWA6Mqg3bAtWTfSRGJ8iZAhLW7LR1Z-Bq4',
        'Origin': 'https://xcx.wesais.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://xcx.wesais.com/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = {
        'business_id': '10000785',
        'stadium_id': '11501',
        'ground_id': '11501001',
        'time_date': '2024-10-24',
        'request_id': '8a681fd0f8d19f5cb9580ef018dc9814',
    }

    response = requests.post('https://api.wesais.com/field/wxFieldBuyPlan/getList', headers=headers, data=data,
                             verify=False)

    with open('0.dat', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    # candidates = ["131150100100234120241024", "131150100100236120241024"]
    # build_sku_slice(candidates)
    # test2()
    test3()