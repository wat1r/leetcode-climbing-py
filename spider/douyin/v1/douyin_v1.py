import execjs
import requests


def get_mstoken():
    node = execjs.get()
    ctx = node.compile(open('./douyin_v1.js', encoding='utf-8').read())
    # funName = 'getPwd("{0}","{1}","{2}")'.format('123456', mod, exp)
    # pwd = ctx.eval(funName)
    # print("pwd->" + pwd)
