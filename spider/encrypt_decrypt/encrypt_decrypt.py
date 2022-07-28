import base64
import unittest
import hmac
import hashlib


def sha1_test():
    _str = "大数据"
    res = hashlib.sha1(_str.encode("utf-8")).hexdigest()
    print('MD5 before encrypt:' + _str)
    print('MD5 after  encrypt ：' + res)

    """
    MD5 before encrypt:大数据
    MD5 after  encrypt ：de064aec70efbe8ade4502dbbf4fcb7374a21412
    """


def hmac_test():
    hm = hmac.new('大数据'.encode(encoding='utf-8'), b'abcd')
    print(hm.digest())
    print(hm.hexdigest())

    """
    b'\xc8;\x0c\x0b\xd42\xc37\xd0X\xbc\xfbf=RP'
    c83b0c0bd432c337d058bcfb663d5250
    """


def hash_test():
    _str = '12345'
    ctx = hashlib.md5()
    ctx.update(_str.encode(encoding='utf-8'))
    print('MD5 before encrypt:' + _str)
    print('MD5 after  encrypt ：' + ctx.hexdigest())

    """
    MD5 before encrypt:12345
    MD5 after  encrypt ：827ccb0eea8a706c4c34a16891f84e7b
    """

    hl = hashlib.md5(bytes('abd', encoding='utf-8'))
    ''' 
    如果没有参数，所以md5遵守一个规则，生成同一个对应关系，如果加了参数，
    就是在原先加密的基础上再加密一层，这样的话参数只有自己知道，防止被撞库，
    因为别人永远拿不到这个参数
    '''
    hl.update(bytes("admin", encoding="utf-8"))
    print(hl.hexdigest())  # 9aea3c0a6c51555c1a4d0a5e9b689ded


def base64_test():
    a = base64.b64encode(b"12345")
    print(a)  # b'MTIzNDU='
    b = base64.b64decode(a)
    print(b)  # b'12345'


# base64_test()
# hash_test()
# hmac_test()
sha1_test()
