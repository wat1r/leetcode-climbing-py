import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.dingxiang-inc.com",
    "Pragma": "no-cache",
    "Referer": "https://www.dingxiang-inc.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "i",
    "referer": "https://www.dingxiang-inc.com/",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "If-None-Match": "674e5926VlR29p2ioq6AxkjFAyG45P82KFno3aS1",
    "Param": "4577#X8XI6rVvmuoLh8V+uRI4Xrm8xgpEMpRJBve7AqzFBxpEy+i8bviyc+hTbWsMyikPBowBwFwneWKetFLFKoLbwHBFKIGNcB1DgOFtyiE4BgwV2ih6bWFt2l+abvJyyii/en5jXX0CCcf1maH1upuLVr8XIAS6XEXQj3bM+cT+Ht9DaPcKZX3OJco4Jh3ZPPVv1rfCjEI/jPMDFDZqihocv93I1PcXm8XeTY2UjAAosVTPT3kAv2WzvE21MrJ1wiM1LYMomNfzmA+1siMo7ytAvgwITX==",
    "Access-Control-Request-Headers": "if-none-match,param",
    "Access-Control-Request-Method": "GET",
    "Referer;": "",
    "origin": "https://www.dingxiang-inc.com",
    "Content-type": "application/x-www-form-urlencoded"
}
cookies = {
    "dx_referer": "https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dhs97weznma9FT6ufJ-NFxEuILjaAuEzOlGVd4IEQbpb8pYO75Coi7XeXWSCXpnnb%26wd%3D%26eqid%3Dfe7651950007c89e00000004674e58d8",
    "dx_referer.sig": "qGO3Gy-h7DXUmAZno7ZyYXI4DSY",
    "dx_from": "www.baidu.com",
    "dx_from.sig": "OQYRMwkhM7zIJZ4zN6jrj45QrQ4",
    "_yunkefu_uni_id": "2diht0bxdngms",
    "Hm_lvt_b9293d65b5ad0bb605ce58738f8f4beb": "1733187806",
    "HMACCOUNT": "962211B5633F91BE",
    "openid": "ouh821t0RHaF5nzyyk__i9Vy-ga0",
    "openid.sig": "NjsyfSaW8sbj2kHKyprO2JU7gWI",
    "_ct_tmp": "00769992960ae92b3bb263d8deff44a2",
    "_ct_un": "F1BB0E10A9C648A38432015231FD84EC",
    "Qs_lvt_483191": "1733187807%2C1733187994",
    "Hm_lpvt_b9293d65b5ad0bb605ce58738f8f4beb": "1733188113",
    "_uetsid": "672be1c0b11211efaf3bedbd519c7112",
    "_uetvid": "672c1d60b11211efa5dab748cba7549d",
    "Qs_pv_483191": "1723952919229142000%2C1616248161836457500%2C1980182698677368000%2C76021797277127970%2C4444423078417824300"
}
url = "https://ykf-webchat.7moor.com/chat"
data = {
    "data": "{\"action\":\"getWebchatGlobleConfig\",\"accessId\":\"41c001f0-8cc1-11e9-ba10-29eb030bc564\"}ac=4644#XrXnUjOAbUWSYDWTXX4XR37yWP7Bm2XtFZi8AshIA9kH/tgk99noCkqk2nDCyobmNTvG8rIROWFtE8pusxykP9gHpTM/PqYZ/F2FXXlPvh/LjN33W9Imj8XmTr3XmvKHz7gvXXRkQADtYrXEOyTQvRQ8aaMH/r3t46X3Xu5ZDcuAJAxDmcSU/c/9419Ta2/XuX66i/7lurP66u+WeCx6bR1Yury6mrXzh1vQS37ikZZnH2ywu23IUw2mmhSDj8Ipi253iYIbXLVQ3X3lIR9JmrXzh1n083qDk44nH2ywu23IUw2mmhSDj8Ipi253iYIbXLVQ3X3lIR9JmrXch1npV3tIk3QnJ8ywu23IUw2mmhSDX83Ei2y+vjS1IEICuC5/HX5Xv0HdoStv0k9S+1CwuNg2/wvYZc/bDXZrj1/1kTx9mNIgaj9vUAaTj8XmTrfXv/CEiymZf6NchPyvIMWmjjogX8/lu23mnEov1E8qmLnLnTfJuP2UXYkdbGjKKBz7uMWDj1r8RtMZF/yl8EZgPdI+JTvcYzrW8tQYZy/+srVXX/fUXYkdbGgrvUFL3T3TYA56hhxsUVgoTYaq1D/WHMTLjP5+Th93I3IWiX5Xv0Hd0OpHT3hXrnYkB5HfpblldedaQUpn7ndpCHi4G50/0Z6CVSN7mrXch1nzy3VLkOOnJ8ywu23IUw2mmhSDX83Ei2y+vjS1IEICuC5/HXrXYnKFte1M8VIYYXXnL5Bn/9URygynXXEFLgWyvi1CB2rXYnKFM+qpZwWPjXiYhsaI+3uJFcch+XgakdXUkd81kdWmkdXFkdW1kd81kdXUkdTNk29VkdXFkdTMk2V1kdXXkd8Pk2V1k2WPOMXuJCmtHmXUWMm9YMmtWCXFJTm9jCmtHmXUHTmNJCmtHmXFHCXUjmmtWMmNYMXFYTmtWCmNjmXFJNShj2IhYPWhW28hj2XhWz8hY2Vhj2IhWzWhYPfhj2XhWdWhYPXhj22hYd8hWzfhj2VhYdIhWr8hjdIhYP3hY2Whj2XhWrXhWz3hj2VhYX3hYX2hj23hYP3hW2faOC4WsVMXv/4RUTWZ+mmtHmm9YmXUJMmtHMXFYMmNWCmtHmXFYmm9YTmtHMXUYmm9jMmtWMmNYMXFYTmtWCmNjmXFJMmtHTmNJCXFJMXuYTmtHmm9YmXUJMmtHMXUjCXUHTWk+uuhUaOunVajn9xO+XgakdXYkdWFkdTtkdXYk29Nkd8UkdXYkdTtkd8ukdXmk2VFkdWXkdXFkd4Mk2M9kdXFkd81k29VkdXjkd4Nkd4NkdXmk2MVkd4NkdXUkd83k29tkdXUk22Ukd8U+myaFuMhF/afU33aWmWPk24Vn9QJFcM6vCraOC4avauUmcmOs/uH+Xg1J2VuJ82k+u9hi9uGs9Q8FcVaWXWPWrImJTyaIya6FcVaWmWfnyu+vCxavauUOauJF15uJNraOC4TUuT8v9mOFCWZ+mX3YauJFmXuJcOkiVO3k2Owk2WuF/46UyahUmC+i9MOk2Wuk2Otk2OVscMmk2WPiac6U/fhJD3hJX4XUuTPUcmuk2WPF/46UyahUmCHs9TRsVWhJXaTnV9hsCXuJmX3jMX3YauJFmXuJcOkiVO3k2Owk2WuiT4i",
    "ak": "279891a0684fe2dac839034aec7b59ff",
    "c": "674e5926VlR29p2ioq6AxkjFAyG45P82KFno3aS1",
    "jsv": "5.1.49",
    "sid": "79bd72b19b8172a9873b36de81c554b8",
    "aid": "dx-1733188162175-24438942-4",
    "uid": "",
    "type": "1",
    "w": "380",
    "h": "165"
}
response = requests.options(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)