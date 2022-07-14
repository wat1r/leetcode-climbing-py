import execjs

if __name__ == '__main__':
    node = execjs.get()
    ctx = node.compile(open('./fanke_login.js', encoding='utf-8').read())
    funName = 'md5("{0}")'.format('123456')
    pwd = ctx.eval(funName)
    print(pwd)
