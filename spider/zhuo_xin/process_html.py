from html.parser import HTMLParser
from bs4 import BeautifulSoup
from lxml import etree


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Encountered a start tag:", tag)
#
#     def handle_endtag(self, tag):
#         print("Encountered an end tag :", tag)
#
#     def handle_data(self, data):
#         print("Encountered some data  :", data)

def process_html_file(start=1, end=1):
    output = open('field_detail_20240115_e.txt', mode='w', encoding='utf-8')
    for i in range(start, end):
        with open('new_page_data/%d.html' % i, 'r', encoding='utf-8') as f:
            print('------>%d.html' % i)
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            tbodys = soup.find_all('tbody')
            trs = soup.find_all('tbody')[2].find_all('tr')
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
                        print("error:--->" + str(i))


if __name__ == '__main__':
    process_html_file(1, 2)
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
