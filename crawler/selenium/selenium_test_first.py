import json

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service

caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
    },
}

options = webdriver.ChromeOptions()

# options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})
# options.add_argument('--disable-dev-shm-usage')
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
options.set_capability('goog:loggingPrefs', {
    'performance': 'ALL',
})

# options.add_experimental_option("goog:loggingPrefs", {
#     "performance": "ALL",
# })

# options.add_experimental_option("perfLoggingPrefs", {
#     "enableNetwork": True,
#     "enablePage": True,
#     "traceCategories": "devtools.timeline,disabled-by-default-devtools.timeline",
#     "bufferUsageReportingInterval": 100,
# })
# options.add_argument("--enable-logging=stderr")
# options.add_argument("--v=1")
# options.add_argument("--perf-log-trace-startup")
# options.add_argument("--perf-log-file=output.json")
# options.add_argument("--no-sandbox")  # 运行无沙盒模式
# options.add_argument("--disable-dev-shm-usage")  # 禁用dev-shm-usage
# options.add_argument("---ignore-certificate-errors")  # 设置忽略https证书校验
# options.binary_location = r'D:\Dev\Python\Python-3.10.9\chromedriver.exe'
ser = Service()
# ser.executable_path = r'D:\Dev\Python\Python-3.10.9\chromedriver.exe'
ser.executable_path = r'D:\Dev\01install\Python\Python311\chromedriver.exe'
# options.page_load_strategy = 'eager'
# options.page_load_strategy = 'normal'
page = webdriver.Chrome(options=options, service=ser)


def performance():
    page.get('https://partner.oceanengine.com/union/media/login/')
    # 必须等待一定的时间，不然会报错提示获取不到日志信息，因为絮叨等所有请求结束才能获取日志信息
    time.sleep(3)
    request_log = page.get_log('performance')

    print(request_log)


def douban():
    page.get('https://movie.douban.com/top250')  # 访问网址，这行产生的数据包不监听

    # 获取网络日志
    performance_log = page.get_log('performance')

    iterator_performance_log(performance_log)

    # 解析日志以找到 requestId
    # for entry in performance_log:
    #     if 'requestId' in entry:
    #         request_id = entry['requestId']
    #         print(request_id)
    #         break

    for _ in range(5):
        res = page.implicitly_wait(time_to_wait=2)
        response_body = page.execute_cdp_cmd(
            "Network.getResponseBody",
            {
                "requestId": 'ddd'
            }
        )
        print(response_body)


def ant_fortune():
    # https://v.alipay.com/api/graphicManagement/search?ctoken=3GAiYQZyUvozhMVG&_input_charset=utf-8
    sub_url = r'https://s.alipay.com/life/main.htm'
    page.get(sub_url)
    time.sleep(10)
    page.get('https://s.alipay.com/life/web/fortune/publishMng')
    performance_log = page.get_log('performance')
    iterator_performance_log(performance_log)
    pass


def iterator_performance_log(performance_log):
    for packet in performance_log:
        message = json.loads(packet.get('message')).get('message')  # 获取message的数据
        if message.get('method') != 'Network.responseReceived':  # 如果method 不是 responseReceived 类型就不往下执行
            continue
        packet_type = message.get('params').get('response').get('mimeType')  # 获取该请求返回的type
        # if not filter_type(_type=packet_type):  # 过滤type
        #     continue
        requestId = message.get('params').get('requestId')  # 唯一的请求标识符。相当于该请求的身份证
        url = message.get('params').get('response').get('url')  # 获取 该请求  url
        # print(url)
        if str(url).__contains__("top250") or str(url).__contains__("graphicManagement"):
            try:
                print(requestId)
                resp = page.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})  # selenium调用 cdp
                print(f'type: {packet_type} url: {url}')
                print(f'response: {resp}')
                print()
            except WebDriverException:  # 忽略异常
                pass


if __name__ == '__main__':
    # performance()
    # douban()
    ant_fortune()
    pass
