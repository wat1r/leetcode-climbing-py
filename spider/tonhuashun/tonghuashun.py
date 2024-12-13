import json

import requests
from lxml import etree
from loguru import logger
import execjs

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    # "Cache-Control": "no-cache",
    # "Connection": "keep-alive",
    # "Pragma": "no-cache",
    # "Referer": "https://q.10jqka.com.cn/",
    # "Sec-Fetch-Dest": "script",
    # "Sec-Fetch-Mode": "no-cors",
    # "Sec-Fetch-Site": "same-site",
    # "X-Requested-With": "XMLHttpRequest",
    # "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\""
}
# cookies = {
#     "v": "A_iLrOkS6xJd0AeW2MESvy5Zya2PYV28vsQweDJpQTfnDZaT2nEsew7VAMiB"
# }

with open("./tonghuashun.js", 'r', encoding='utf-8') as f:
    hexin_js = f.read()

cookie = execjs.compile(hexin_js).call("get_cookie")
logger.info("cookie:{}", cookie)
cookies = {"v": cookie}
url = "http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/"
resp = requests.get(url, headers=headers, cookies=cookies)
# json.dumps("xx", separators=(',', ':')) + ''  ==== JSON.stringify(res)

# print(response.text)
# print(response)
logger.info(resp.status_code)
html = etree.HTML(resp.text)
for tr in html.xpath("//table//tr")[1:]:
    tds = [td.xpath('string(.)') for td in tr.xpath("./td")]
    logger.success(tds)
