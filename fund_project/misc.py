import json
import re


def get_cookies():
    # COOKIES = {
    #     "qlskey": "v0ba8297022661f7bb284ce375c48e06",
    #     "qluin": "085e9858e75b0fbbd34d78fbf@wx.tenpay.com",
    # }
    data = r"MultiDictView[['c_route', '3253'], ['lct_appid', 'wxc92ca6e258e3f1eb'], ['ori_appid', 'wxc92ca6e258e3f1eb'], ['qlappid', 'wxc92ca6e258e3f1eb'], ['qlskey', 'v0b93ce392466559bd76ade4ecf30fea'], ['qluin', '085e9858e8dbb5726fe0d3ab4@wx.tenpay.com'], ['user_id', 'U223111477765603253'], ['wx_session_time', '1716886488051']]"
    # 使用正则表达式匹配所需的键值对
    # 使用正则表达式匹配所需的键值对
    pattern = r"\['qlskey',\s*'([^']+)'\]|\['qluin',\s*'([^']+)'\]"

    # 搜索匹配项
    matches = re.finditer(pattern, data)

    # 存储匹配结果
    results = {}

    # 遍历所有匹配项
    for match in matches:
        if match.group(1):
            # 如果匹配到qlskey
            results['qlskey'] = match.group(1)
        elif match.group(2):
            # 如果匹配到qluin
            results['qluin'] = match.group(2)

    # 将提取的数据转换为JSON格式的字符串
    result_json = json.dumps(results, ensure_ascii=False)
    print(result_json)


if __name__ == '__main__':
    get_cookies()
