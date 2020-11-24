import xlrd, xlwt
import json
import re
from collections import defaultdict

file = open('./data/refrigerator_search_result' + '.txt', mode='r', encoding='utf-8')


def process_excel():
    question_dict = defaultdict(list)
    article_dict = defaultdict(list)
    for line in file.readlines():
        result = json.loads(line)
        title = result['title']
        score = result['score']
        keyword = result['keyword']
        real_url = result['real_url']
        if str(title).__contains__("知乎") and not str(real_url).__contains__("zhihu.com"):
            print(line)
        if str(real_url).__contains__("zhihu.com"):
            if re.match(".*/question/.*", real_url):
                question_id = None
                match = re.match(".*/question/([0-9]+)/answer/([0-9]+)", real_url)
                if match: question_id = match.group(1)
                match = re.match(".*/question/([0-9]+)/.*sort=created", real_url)
                if match and not question_id:
                    question_id = match.group(1)
                match = re.match(".*/question/([0-9]+)", real_url)
                if match and not question_id:
                    question_id = match.group(1)
                merge(question_dict, question_id, real_url, score)

            elif re.match(".*/p/.*", real_url):
                article_id = None
                match = re.match(".*/p/([0-9]+)", real_url)
                if match: article_id = match.group(1)
                merge(article_dict, article_id, real_url, score)
            if not question_id and not article_id:
                print(real_url)

    write_question_excel(list(question_dict.values()))
    write_article_excel(list(article_dict.values()))


def merge(dict, question_id, real_url, score):
    """
    merge the score
    :param dict:
    :param question_id:
    :param real_url:
    :param score:
    :return:
    """
    if dict[real_url]:
        dict[real_url][2] = dict[real_url][2] + score
        dict[real_url][3] = dict[real_url][3] + 1
    else:
        dict[real_url].append(real_url)
        dict[real_url].append(question_id)
        dict[real_url].append(score)
        dict[real_url].append(1)


def write_question_excel(datas):
    # title = ["question_url", "question_id", "score", "covered_keyword_num"]
    title = ["问题链接", "问题ID", "预估流量值", "覆盖词数"]
    data_write("./data/question.xls", datas, title)


def write_article_excel(datas):
    # title = ["article_url", "article_id", "score", "covered_keyword_num"]
    title = ["文章链接", "文章ID", "预估流量值", "覆盖词数"]
    data_write("./data/article.xls", datas, title)


def data_write(file_path, datas, title):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    datas.insert(0, title)  # 写入表头
    style = xlwt.XFStyle()  # 创建样式
    align = xlwt.Alignment()  # 创建对齐方式
    align.horz = 1  # 1-->左对齐，2-->居中，3-->右对齐
    style.alignment = align
    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i, j, data[j], style=style)
        i = i + 1
    f.save(file_path)  # 保存文件


def test_dict():
    dict = defaultdict(list)
    # l = ['a', 'b', 'c']
    # dict['k'].append(l)
    dict['k'].append("1")
    dict['k'].append(2.5)
    dict['k'].append("ddd")
    dict['k'][1] = dict['k'][1] + 0.4

    for l in dict.values():
        print(l)

    print()


if __name__ == '__main__':
    process_excel()
    # datas = []
    # title = ["A", "B", "C"]
    # datas.append([1, 2, 3])
    # data_write("./data/1.xls", datas, title)
    # print("")
    # d = defaultdict(set)
    # s = [("001", "A"), ("001", "C"), ("002", "B")]
    # for k, v in s:
    #     d[k].add(v)
    # test_dict()
    # print(sorted(d.items()))
