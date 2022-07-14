import execjs

if __name__ == '__main__':
    node = execjs.get()
    ctx = node.compile(open('wechat_login.js', encoding='utf-8').read())
    funName = 'getPwd("{0}")'.format('ddadada')
    pwd = ctx.eval(funName)
    print(pwd)
