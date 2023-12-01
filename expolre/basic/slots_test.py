import weakref

"""
理解 Python 类属性 __slots__
https://zhuanlan.zhihu.com/p/294027322
"""


class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Y:
    # __slots__ = ('a', 'b')
    __slots__ = ('a', 'b', '__dict__', '__weakref__')

    def __init__(self, a, b):
        """
        此时如果你声明一个 __slots__ 中没有的属性，如
        self.c = 1
        pylint 等就会提示错误：
        [pylint] [Error] Assigning to attribute 'c' not defined in class slots
        当然如果你执意要写的话，初始化实例的时候会引发 AttributeError：
        AttributeError: 'Y' object has no attribute 'c'
        """
        self.a = a
        self.b = b


x = X(7, 8)
print(x.a)
x.c = 9
print(x.__dict__)

rx = weakref.ref(x)
print(rx)

y = Y(7, 8)
print(y.a)
# y.c = 9
# AttributeError: 'Y' object has no attribute 'c'
# print(y.__dict__)
# AttributeError: 'Y' object has no attribute '__dict__'
ry = weakref.ref(y)
# print(ry)
# TypeError: cannot create weak reference to 'Y' object
