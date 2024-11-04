

def test1():
    import requests

    cookies = {
        'JSESSIONID': '69A2167C1604B6C39D72905C68455764',
        'csROn0dvxDHwO': '60dlGuVVRDDyXFLT.9y1Lsk7vCZdnBQrdq5flodc1afqeixpqUIzc80eglw8iZx3Vr42o5ZNBwsHHPwGioMOgwga',
        'csROn0dvxDHwP': '0hdHEtwkKCoevsw7aIklw27TCa81Ek5tMQNQgWIYVq.z4Ifa9J1VsRdZz8k6kNpmBuNIzMwrmeSbuS258o93g_2SOoJNTCrq1umum7Xv_bIapFYMVezO3CgwUc4vR2KMNc7UmhqVqZJFBm8aYh7c0rKMi0xiYp_uvCCnYjGsDU1UbDX7mVohoy3xolNZcOAxydks60DlIQN6OKJzbwnAVub2x_pjBJOxWca8fyYBrGhGgSLyNbTfwZ1EJnxLJBYkck3rTcLV2A3YctxzahXxjpb.tqQr54T1ZUS5qUHmOiJL.DVR1GGhEs3VYkRzhGei_a7NeZyx7ZagByLbe1haPd09YizKW2LZZItg9qCQ95rhtZrZy65bnuu.2HNyoPVrjo9sPQ0U3EaJhZYPwR14WdTX1hfuQ_drtASSoEqnM.FBuNVNDeqOEecHvjy5LzNb4h3sstc2TcEoFrVuv5oza64_lYBOn85fzlBgr9qQWPUA',
    }

    headers = {
        'Host': 'sport.js118114.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'timestamp': '1730689018472',
        'nonceStr': 'nth723h96v0-3t1t-4v40-9v1n-92tenhe67hh0',
        'uuidCode': '102b606588084794a31479f564ae7057',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090c11) XWEB/11275 Flue',
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwaG9uZSI6IjEzNDAxNDYyMjkwIiwiZXhwIjoxNzMxNTc3ODM0LCJ1c2VySWQiOiIxMTQ1NDYyIn0.hbLyQ6RJy6RpW-j9GTVUiZANwZ2PDDt5SxdezvkQkOM',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://sport.js118114.com/venuesSport/venuesStatus?type=0&venuesId=1558&sportId=1002&venuesName=%%E5%%AE%%89%%E5%%BE%%B7%%E7%%90%%83%%E9%%A6%%86&selectedDate=2024-11-06',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'JSESSIONID=69A2167C1604B6C39D72905C68455764; csROn0dvxDHwO=60dlGuVVRDDyXFLT.9y1Lsk7vCZdnBQrdq5flodc1afqeixpqUIzc80eglw8iZx3Vr42o5ZNBwsHHPwGioMOgwga; csROn0dvxDHwP=0hdHEtwkKCoevsw7aIklw27TCa81Ek5tMQNQgWIYVq.z4Ifa9J1VsRdZz8k6kNpmBuNIzMwrmeSbuS258o93g_2SOoJNTCrq1umum7Xv_bIapFYMVezO3CgwUc4vR2KMNc7UmhqVqZJFBm8aYh7c0rKMi0xiYp_uvCCnYjGsDU1UbDX7mVohoy3xolNZcOAxydks60DlIQN6OKJzbwnAVub2x_pjBJOxWca8fyYBrGhGgSLyNbTfwZ1EJnxLJBYkck3rTcLV2A3YctxzahXxjpb.tqQr54T1ZUS5qUHmOiJL.DVR1GGhEs3VYkRzhGei_a7NeZyx7ZagByLbe1haPd09YizKW2LZZItg9qCQ95rhtZrZy65bnuu.2HNyoPVrjo9sPQ0U3EaJhZYPwR14WdTX1hfuQ_drtASSoEqnM.FBuNVNDeqOEecHvjy5LzNb4h3sstc2TcEoFrVuv5oza64_lYBOn85fzlBgr9qQWPUA',
    }

    params = {
        '3gprRWDg': '0UwQXzalqWxWG9p6R3xZW5mDRUMV0Od9fEXVwuPEZSxVYPXqpNlune0gbcnvyL6H.Gy2uvbvy73cq55EQfjlhIvRkAtkoanPns7PjBHF7l71ib_qTMwOoOmOHdsDUkisCnQU9KXrveDaJAcZt_VeQ7..ItOpObGygKMhw4HIBuzE2dntMhae1DA95TwrLMBrjR0QBUnHWidXTjd3SE.Wqpw9XVyBEH2rqvkB5PGxXB8sBksM4.tMPmY7',
    }
    # 3gprRWDg=0DrkRcalqWcf8h5wkx2brJCqa0_CW2Cce1XZirb50R7Qjnuc0r5ULyZp77umwVQ0FAy2lthfp_EcqW4MqJ9ARlVLxvWGha3iWxg3sRRZwgw7N7j9kJDEN0oqYdIvxOo4r3soaGA.wkKfnZda0v31Z3.1TnvaLMLmi.b7rjDV7zLVpVqMkb8UAN6wtYHtoxSz.zn05VgUEhvOfn4s7D9C_UxAMfImk0_ilv3fIVLC_yL8SppDK28QWD1g

    response = requests.get(
        'https://sport.js118114.com/venuessport/venues/queryVenuesStatus',
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
    )

    with open('01.dat', 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    test1()
