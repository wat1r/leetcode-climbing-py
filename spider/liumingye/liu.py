import execjs

if __name__ == '__main__':
    node = execjs.get()
    ctx = node.compile(open('./liu_dst.js', encoding='utf-8').read())
    funName = 'encode("text=陈奕迅&page=1&type=migu")'
    res = ctx.eval(funName)
    print(res)
