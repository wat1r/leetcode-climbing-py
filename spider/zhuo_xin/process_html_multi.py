from html.parser import HTMLParser
from bs4 import BeautifulSoup
from lxml import etree

import threading

output = open('field_detail_20240115_multi.txt', mode='a+', encoding='utf-8')


def process_html_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        trs = soup.find_all('tbody')[2].find_all('tr')
        print('--------in:', file)
        for tr in trs:
            line_data = []
            tds = tr.find_all('td')
            for td in tds:
                final_text = td.text.replace("\t", " ").replace("\n", " ")
                line_data.append(final_text)
            # print(str('\t'.join(line_data)))
            if line_data:
                try:
                    output.write(str('\t'.join(line_data)) + "\n")
                except:
                    print("ddd")


def entrance(start=1, end=1):
    file_list = []
    for i in range(start, end + 1):
        file_list.append('new_page_data/%d.html' % i)
    for file in file_list:
        print('------------>:', file)
        thread = threading.Thread(target=process_html_file, args=([file]))
        thread.start()


if __name__ == '__main__':
    entrance(701, 2948)

    # process_html_file(701, 2948)
###


# with open('page_data/1.html', 'r', encoding='utf-8') as file:
#       content = file.read()
#       #     result = etree.parse(content)
#       #     print(result)
#       soup = BeautifulSoup(content, 'html.parser')
#
#       tbodys = soup.find_all('tbody')
#
#       trs = soup.find_all('tbody')[2].find_all('tr')
#
#       for tr in trs:
#           line_data = []
#           tds = tr.find_all('td')
#           for td in tds:
#               final_text = td.text.replace("\t", " ").replace("\n", " ")
#               line_data.append(final_text)
#           print(str('\t'.join(line_data)))

# trs = soup.find_all('tr', class_='el-table__row')
# el_table = soup.find('div', class_='el-table__body-wrapper is-scrolling-left')
# trs = el_table.find_all('tr', class_='el-table__row')
# for tr in trs:
#     print(tr.text)
# parser.feed(content)

# print()

# for line in f.readlines():
#     print(str(line))
####
