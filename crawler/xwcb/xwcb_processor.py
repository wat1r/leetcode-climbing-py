import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)


def getCookies():
    # get login taobao cookies
    url = "https://www.kjjxjy.com/center/myStudy/goods/detail?year=2019"
    brower.get("https://www.kjjxjy.com/index/")
    while True:
        print("Please login in")
        time.sleep(3)
        # if login in successfully,
        while brower.current_url == url:
            Cookies = brower.get_cookies()
            brower.quit()
            cookies = {}
            for item in Cookies:
                cookies[item['name']] = item['value']
            outputPath = open('jxjycookies.pickle', 'wb')
            pickle.dump(cookies, outputPath)
            outputPath.close()
            return cookies


def readCookies():
    # if hava cookies file ,use it
    # if not , getTaobaoCookies()
    if os.path.exists('jxjycookies.pickle'):
        readPath = open('jxjycookies.pickle', 'rb')
        Cookies = pickle.load(readPath)
    else:
        Cookies = getCookies()
    return Cookies


if __name__ == '__main__':
    Cookies = readCookies()

    brower.get("https://www.kjjxjy.com/center/myStudy/goods/detail?year=2019")
    for cookie in Cookies:
        brower.add_cookie({
            "domain": ".kjjxjy.com",
            "name": cookie,
            "value": Cookies[cookie],
            "path": '/',
            "expires": None
        })
    brower.implicitly_wait(10)
    course_list = brower.find_elements_by_css_selector("tr[ng-click='events.goCourseDetail(item)']")
    course_num = len(course_list)
    print(course_num)
    for i in range(1, course_num + 1):
        # 进入每个课程

        lesson_xpath = "/html/body/div[3]/div/div[2]/div/div/div[4]/div[3]/table/tbody/tr[" + str(i) + "]/td[2]/a[1]"
        # brower.implicitly_wait(10000000)
        while (1):
            try:
                brower.find_element_by_xpath(lesson_xpath).click()
                break
            except:
                continue
        window = brower.window_handles
        brower.switch_to_window(window[-1])

        brower.implicitly_wait(5)

        # 检查目录列表
        context_list = []
        context_list = brower.find_elements_by_css_selector("li[ng-init='firstMedia = courseWare.mediaList[0]']")
        sector_num = len(context_list)
        print(sector_num)
        for j in range(sector_num):

            print("current_lesson=%d" % (j))
            ans = 0
            while (1):
                try:
                    brower.find_element_by_css_selector(".vjs-big-play-button").click()
                    brower.find_element_by_css_selector("button[title='静音']").click()
                except:
                    time.sleep(1)
                try:
                    print("ans=%d" % (ans))
                    ans = (ans + 1) % 2
                    brower.find_elements_by_css_selector(".ui-label")[ans].click()
                    time.sleep(1)
                    brower.find_element_by_css_selector("button[data-action='answer']").click()
                    time.sleep(1)
                    brower.find_element_by_css_selector("button[data-action='close']").click()
                    time.sleep(1)
                    print("answer success")
                except:
                    print("cannot find")
                print("still running")
                try:
                    if (context_list[j].text.find("100%") != -1):
                        if (j < sector_num - 1):
                            context_list[j + 1].click()
                        break
                except:
                    context_list = brower.find_elements_by_css_selector(
                        "li[ng-init='firstMedia = courseWare.mediaList[0]']")
                    continue
                time.sleep(3)
        # 关闭当前窗口B
        brower.close()
        # 切换回窗口A
        window = brower.window_handles
        brower.switch_to_window(window[0])
        time.sleep(3)
    brower.quit()