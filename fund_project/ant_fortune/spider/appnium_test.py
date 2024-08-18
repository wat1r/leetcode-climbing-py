# -*- coding: utf-8 -*-
# from selenium import webdriver
# import asyncio
# from appium import webdriver

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# {
#   "appium:platformName": "Android",
#   "appium:platformVersion": "9",
#   "appium:deviceName": "HUAWEI P10"
# }

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "HWVTR",
    "noReset": True,
    "appPackage": "com.eg.android.AlipayGphone",
    "appActivity": "com.eg.android.AlipayGphone.AlipayLogin",
    "udid": "SJE0217629001168",
    # "appPackage": "com.tencent.mm",
    # "appActivity": "com.tencent.mm.ui.LauncherUI"
    # "appPackage": "com.taobao.taobao",  # app包名
    # "appActivity": "com.taobao.tao.welcome.Welcome",  # app的启动页面
    # "appPackage": "com.tencent.mm",
    # "appActivity": ".ui.LauncherUI"

# com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin}
}


def run():
    # 连接Appium服务器
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 在这里编写自动化操作代码
    # 例如点击按钮、输入文本等
    # driver.find_element_by_id('com.example.app:id/button').click()
    # driver.find_element_by_id('com.example.app:id/editText').send_keys('your_text')
    # # 获取抓取的数据
    # data = driver.find_element_by_id('com.example.app:id/data').text
    # print(data)
    # # 关闭App
    # driver.quit()
    wait = WebDriverWait(driver, 30)

    finance_ele = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text(\"理财\")')



    print()
    # # 获取登录按钮
    # login_btn = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/drp")))
    # # 点击登录按钮
    # login_btn.click()
    # # 获取手机号文本框
    # phone_text = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/ji")))
    # # 填写手机号文本框
    # phone_text.send_keys("18888888888")


# async def make_driver():
#     url = r"http://127.0.0.1:4723" + "/wd/hub"
#     driver = webdriver.Remote(url, desired_capabilities=desired_caps)
#     driver.implicitly_wait(5)
#     size = driver.get_window_size()
#     print("当前手机：华为，size:", size)
#     return driver


if __name__ == '__main__':
    # tasks = [make_driver()]
    # asyncio.run(asyncio.wait(tasks))
    run()
