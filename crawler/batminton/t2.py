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

response = requests.post('https://api.wesais.com/field/wxFieldBuyPlan/getList', headers=headers, data=data, verify=False)

print(f"response:{response}")
