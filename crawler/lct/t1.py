def test1():
    import requests

    headers = {
        'Host': 'www.tencentwm.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'xweb_xhr': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'cookie': 'qlappid=wxcc8a51267886fec4; qlskey=v098e6d6d21670e47fd0d9dd1d4feb52; qluin=085e9858e75b0fbbd34d78fbf@wx.tenpay.com; c_route=4188; user_id=U201803145112744188; login_expire=1730285181; time=1728989181170;',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11275',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxcc8a51267886fec4/613/page-frame.html',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = {
        'report_platform': 'mp',
        '_': '58030911',
    }
    user_name = "债市晴天小助手"
    data = (
            '{"OutPutType":"JSON","s_key_word":"%s","i_finish":1,"i_filter_not_sale":0,"s_uin":"085e9858e75b0fbbd34d78fbf@wx.tenpay.com","i_account_type":2,"s_seq_no":"085e9858e75b0fbbd34d78fbf_1729577638447","st_search_comm_extend_req":{"s_abt_traffic_distributed_info":"","s_manual_traffic_distributed_info":"","s_scene_arguments":[]},"s_scene_type":"9","i_channel":1,"b_record_history":true,"s_page_size":"10","g_tk":"1009537508"}' % user_name).encode()

    response = requests.post(
        'https://www.tencentwm.com/fbp/fund/v1/fund.fuapl_search_ao.FuaplSearchAo.FsaSearchResultV3',
        params=params,
        headers=headers,
        data=data,
        verify=False,
    )

    with open('0.dat', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    test1()
