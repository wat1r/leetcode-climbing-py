# https://blog.csdn.net/qq_21294095/article/details/85209523
# import threading
#
#
# def a(x):
#     print('a thread %d' % x)
#     b(x)
#
#
# def b(x):
#     print('b thread %d' % x)
#
#
# t1 = threading.Thread(target=a, args=(3,))
# t2 = threading.Thread(target=a, args=(5,))
#
# t1.start()
# t1.join()
# t2.start()
# t2.join()

# import threading
#
# x = 0
#
#
# def a():
#     print('a thread %d' % x)
#     b()
#
#
# def b():
#     print('b thread %d' % x)
#
#
# t1 = threading.Thread(target=a)
# t2 = threading.Thread(target=a)
#
# t1.start()
# t1.join()
# t2.start()
# t2.join()

# import threading
#
# dict = {}
#
#
# def a(x):
#     dict[threading.current_thread()] = x
#     print('a thread %d' % x)
#     b()
#
#
# def b():
#     print('b thread %d' % dict[threading.current_thread()])
#
#
# t1 = threading.Thread(target=a, args=(3,))
# t2 = threading.Thread(target=a, args=(5,))
#
# t1.start()
# t1.join()
# t2.start()
# t2.join()


import threading

dict = threading.local()


def a(x):
    dict.x = x
    print('a thread %d' % dict.x)
    b()


def b():
    print('b thread %d' % dict.x)


t1 = threading.Thread(target=a, args=(3,))
t2 = threading.Thread(target=a, args=(5,))

t1.start()
t1.join()
t2.start()
t2.join()



