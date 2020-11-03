import json, xlwt
import random


def read_score(jsonfile):
    book = xlwt.Workbook()  # 创建excel文件
    sheet = book.add_sheet('sheet1')  # 创建一个表
    title = ['商品', '价格', '收货', '店铺', '地址', '是否天猫店', '链接', '评论']
    en_title = ['name', 'price', 'deal-cnt', 'shop_name', 'location', 'is_tmall', 'url', 'comment']
    for col in range(len(title)):  # 存入第一行标题
        sheet.write(0, col, title[col])
    row = 1  # 定义行
    with open(jsonfile, encoding='gb2312') as f:  # 将json文件转化为字典
        while True:
            score_all = f.readline()
            if not score_all:  # 到 EOF，返回空字符串，则终止循环
                break
            js = json.loads(score_all)
            is_need = True
            for index in range(len(en_title)):
                # 依次写入每一行
                if (en_title[2] == 'deal-cnt'):
                    deal_cnt = js[en_title[2]].replace("人付款", "")
                    if (str(deal_cnt).__contains__("万")):
                        is_need = False
                        break
                    deal_cnt_tmp = str(deal_cnt).replace("+", "")
                    if (int(deal_cnt_tmp) < 50 or int(deal_cnt_tmp) > 1000):
                        is_need = False
                        break
                    js[en_title[2]] = deal_cnt
                if (is_need):
                    sheet.write(row, index, js[en_title[index]])
            if is_need: row += 1
    book.save('电子美容仪.xls')


def read_score_5118(jsonfile):
    book = xlwt.Workbook()  # 创建excel文件
    sheet = book.add_sheet('sheet1')  # 创建一个表
    title = ['关键词', '收录量', '竞价公司数量', '长尾词数量']
    en_title = ['word', 'src', 'company_cnt', 'long_tail']
    for col in range(len(title)):  # 存入第一行标题
        sheet.write(0, col, title[col])
    row = 1  # 定义行
    with open(jsonfile, encoding='gb2312') as f:  # 将json文件转化为字典
        while True:
            score_all = f.readline()
            if not score_all:  # 到 EOF，返回空字符串，则终止循环
                break
            score_all = score_all.replace("\n", "")
            js = json.loads(score_all)
            is_need = True
            print(score_all)
            if js[en_title[0]] == "瓷肌祛斑":
                print("eddd")
            for index in range(len(en_title)):
                # 依次写入每一行
                sheet.write(row, index, js[en_title[index]])
            row += 1
    book.save('祛斑.xls')


if __name__ == '__main__':
    # read_score('../_5518/祛斑_origin.txt')
    read_score_5118('祛斑_origin_edit.txt')
    # print("ed")
