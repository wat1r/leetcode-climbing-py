from bs4 import BeautifulSoup
from DrissionPage import ChromiumPage, ChromiumOptions

# co = ChromiumOptions().auto_port()
page = ChromiumPage(timeout=1)


def test1():
    html = 'This is an example: <p>Hello, World!</p>'

    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    print(text)


def test2():
    html_content = """
    <html>
    <head>
        <title>示例页面</title>
    </head>
    <body>
        <p>这是一个段落。</p>
        <img src="image1.jpg" alt="图片描述1">
        <img src="image2.png" alt="图片描述2">
    </body>
    </html>
    """
    text, images = extract_text_and_images(html_content)
    print(text)
    print(images)


def extract_text_and_images(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    text = soup.get_text()
    images = soup.find_all('img')

    image_info = []
    # for img in images:
    #     image_info.append({
    #         'src': img.get('src'),
    #         'alt': img.get('alt')
    #     })

    return text, image_info


def test_drission_page():
    page.get('https://www.baidu.com')

    tab_id = page.find_tabs(url='baidu.com')

    print("----------")


if __name__ == '__main__':
    # test1()
    # test2()
    test_drission_page()
    pass
