import execjs
import requests


def get_rsa_key():
    url = "https://store.steampowered.com/login/getrsakey/"
    data = {
        'donotcache': '1657676365238',
        'username': '123@qq.com'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10 .0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        # 'Cookie': '_ga=GA1.2.348843638.1657674961; _gid=GA1.2.1020255245.1657674961; steamCountry=CN%7C33960e3186121e5f75dabec5faaa1628; browserid=2805196637914686956; sessionid=f1329fbbe889a03c451800ae; timezoneOffset=28800,0; app_impressions=107410@1_4_4__129_1|1216710@1_4_4__139_4|49520:207870:208690:213210:213230:213250:213780:218550:224200:230090@1_4_4__139_4|552500@1_4_4__139_4|1243830@1_4_4__139_3|593600@1_4_4__139_3|513710@1_4_4__139_3|788100@1_4_4__139_2|1030840:1030830:360430@1_4_4__139_2|107410@1_4_4__139_2|628670@1_4_4__43_1',
    }
    resp = requests.post(url=url, headers=headers, data=data).json()
    mod = resp['publickey_mod']
    exp = resp['publickey_exp']
    print(mod, exp)

    node = execjs.get()
    ctx = node.compile(open('./stream_login.js', encoding='utf-8').read())
    funName = 'getPwd("{0}","{1}","{2}")'.format('123456', mod, exp)
    pwd = ctx.eval(funName)
    print("pwd->" + pwd)


def login():
    print()


if __name__ == '__main__':
    # pwd = get_pwd()
    get_rsa_key()
    print()
