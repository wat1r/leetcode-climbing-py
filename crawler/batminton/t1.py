import requests

headers = {
    'Host': 'api.wesais.com',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b11)XWEB/9193',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdCI6MTcyMzg5OTUwMSwiaWQiOiIxNzIzODk5NTAxMDM3NzUiLCJhaWQiOjEwMTAxLCJtaWQiOjQsInRpZCI6NSwicGFyYW1zIjoie1wiY29tcGFueV9pZFwiOjYxNSxcImFjY291bnRfdHlwZVwiOjMxLFwiYWNjb3VudF9pZFwiOjEwMDk2MTYsXCJtZW1iZXJfaWRcIjoxMTkyMjk4LFwic2FmZV9sXCI6MSxcInBlcnNvbm5lbF9pZFwiOjExOTIyOTh9In0.Xr-canCRc4SsWtEMjCnefSCVyenhF24z4Mq6pJLGriI',
    'Origin': 'https://xcx.wesais.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://xcx.wesais.com/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

time_date = "2024-08-20"

data = {
    'business_id': '10000785',
    'stadium_id': '11501',
    'ground_id': '11501001',
    'time_date': time_date,
    'request_id': 'e0915de185431a17d047d1601e11fac0',
}

response = requests.post('https://api.wesais.com/field/wxFieldBuyPlan/getList', headers=headers, data=data,
                         verify=False)
result = response.json()
sku_list = result['data']['skuList']
for sku in sku_list:
    for sku_item in sku:
        for s in sku_item:
            print(s['sku_name'] + "场次:" + time_date + " " + s['time_str'] + ("已定" if s['is_lock'] else "空闲"))
print(result)
