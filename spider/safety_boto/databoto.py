import time

from DrissionPage._functions.by import By
from bs4 import BeautifulSoup
from DrissionPage import ChromiumPage, ChromiumOptions

# co = ChromiumOptions().auto_port()
page = ChromiumPage(timeout=1)


def test1():
    html = 'This is an example: <p>Hello, World!</p>'

    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    print(text)


def init():
    options = ChromiumOptions()
    options.incognito(True)
    # options.set_argument('--window-size', '640,960')
    options.set_pref(arg='profile.default_content_settings.popups', value='0')
    global page
    page = ChromiumPage(options)
    options.ignore_certificate_errors(True)
    options.mute(True)
    options.set_user_agent(user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) '
                                      'AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.6261.62 Mobile/15E148'
                                      ' Safari/604.1')
    options.no_imgs(True)


def study():
    init()
    # https://shengquacademy.yunxuetang.cn/o2o/#/playinfo?projectid=1864143447147012097
    page.get(
        'https://shengquacademy.yunxuetang.cn/o2o/#/playinfo?projectid=1864143447147012097')
    print("请在30s的时间内完成登录")
    time.sleep(50)
    yxt_scrollbar_view = page.ele((By.XPATH, '//div[@class="yxt-scrollbar__view"]'))
    for child_index in range(1, 3):
        current_step_div = yxt_scrollbar_view.children()[child_index]
        course_eles = current_step_div.children((By.XPATH, '//div'))
        size = len(course_eles)
        for i in range(1, size):
            current_course = course_eles[i].ele((By.XPATH, '//div[@class="layout-flex flex-space-between"]'))
            course_title = current_course.text
            try:
                _path_html = current_course.children()[1].children()[0].html
                # #BFBFBF
                if _path_html and "#52C41A" in _path_html:
                    print(f"当前学习->{course_title} 已经学习过，无需学习")
                    continue
            except Exception as ex:
                print(f"1---------ex->{ex}")

            current_course.click(timeout=2, by_js=False)
            time.sleep(5)
            start_time = int(time.time())
            duration_text = page.ele((By.XPATH, '//span[@class="jw-text jw-reset jw-text-duration"]')).text
            print(f"当前学习->{course_title}，学习时长->{duration_text}")
            duration = cal_duration(duration_text=duration_text, offset=7 * 60)
            while (int(time.time()) - start_time) < duration:
                try:
                    _stop_button = page.ele(
                        (By.XPATH, '//button[@class="yxtf-button yxtf-button--primary yxtf-button--large"]'))
                    if _stop_button:
                        print("防挂机验证，清除中...")
                        _stop_button.click(timeout=2, by_js=False)
                        _stop_button = None
                except Exception as ex:
                    print(f"[_stop_button] ex->{ex}")
                print(f"学习中...,{course_title}")
                time.sleep(1 * 60)


def cal_duration(duration_text: str, offset: int = None):
    duration = None
    try:
        parts = duration_text.split(':')
        hours, minutes, seconds = int(parts[-3].strip() if len(parts) > 2 else '0'), int(parts[-2].strip()), int(
            parts[-1].strip())
        duration = hours * 60 * 60 + minutes * 60 + seconds + offset if offset else 5 * 60
    except  Exception as ex:
        print(f"[cal_duration] except:{ex}")
    return duration if duration else 60 * 60


if __name__ == '__main__':
    # test1()
    # test2()
    study()
    pass
