 d:wq
t1 = threading.Thread(target=a, args=(3,))
t2 = caw
.:wq
(target=a, args=(5,))
d

d:wq
t1 = threading.Thread(target=a, args=(3,))
t2 = caw
.:wq
(target=a, args=(5,))
d

：

    print('a thread %d' % x)
    b(x)


):
nt('b thread %d' % x)



d:q
ef b
    p



ding
t2.start()
t2.join()
https://blog.csdn.net/qq_21294095/article/details/85209523
import threading


          # def a():
          #     print('a thread %d' % x)
import thr#     b()
          #
x = 0     #
          # def b():
t1.start()#     print('b thread %d' % x)
t1.join() #

t1 = threading.Thread(target=a)
t2 = threading.Thread(target=a)

t1.start()
t1.join()
t2.start()
t2.join()

import threading

dict = {}


def a(x):
    dict[threading.current_thread()] = x
    print('a thread %d' % x)
    b()


def b():
    print('b thread %d' % dict[threading.current_thread()])


t1 = threading.Thread(target=a, args=(3,))
t2 = threading.Thread(target=a, args=(5,))

t1.start()
t1.join()
t2.start()
t2.join()


port threading

ct = threading.local()


f a(x):
  dict.x = x
  print('a thread %d' % dict.x)
  b()


f b():
  print('b thread %d' % dict.x)


 = threading.Thread(target=a, args=(3,))
 = threading.Thread(target=a, args=(5,))

.start()
.join()
.start()
.join()



