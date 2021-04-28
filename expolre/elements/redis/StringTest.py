import redis


class StringTest(object):
    def __init__(self):
        try:
            # 本机上没有设置密码
            self.r = redis.Redis(host='localhost', port=6379, db=0)
            #  redis.Redis(host='192.168.192.130',password='no', port=6379, db=0)
            print("connected success.")
        except:
            print("could not connect to redis.")

    def test_set(self):
        ''' set -- 设置值 '''
        rest = self.r.set('name2', 'zhang')
        print(rest)
        return rest

    def test_get(self):
        '''get -- 获取值'''
        rest = self.r.get('name2')
        print(rest)
        return rest


if __name__ == '__main__':
    handler = StringTest()
    handler.test_set()
    handler.test_get()
    print("hello redis")
