import requests

# import  cgitb


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}  # 定义头文件，伪装成浏览器


# 获取百度链接的真实源地址
# href = {str} 'https://www.baidu.com/link?url=gCQcWkErExKXSzK_LW_hVotcyJfh3qvF282lT00V3-plCGVMuVdqcaM5PBHm_1udhw2Kk6MVXdV-oDq3EZPvrK&amp;wd=&amp;eqid=af674e0d0000476c000000045fb51ddc'
# real_url = {str} 'https://www.zhihu.com/question/21122897'
def get_real_source_url():
    href = "https://www.baidu.com/link?url=gCQcWkErExKXSzK_LW_hVotcyJfh3qvF282lT00V3-plCGVMuVdqcaM5PBHm_1udhw2Kk6MVXdV-oDq3EZPvrK&amp;wd=&amp;eqid=af674e0d0000476c000000045fb51ddc"
    baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
    real_url = baidu_url.headers['Location']  # 得到网页原始地址
    if real_url.startswith('http'):
        print("dd")





print("end")

if __name__ == '__main__':
    print("start")
    get_real_source_url()
