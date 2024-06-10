# gcount = 0
#
# def global_test():
#     gcount+=1
#     print (gcount)
# global_test()


# gcount = 0
#
#
# def global_test():
#     global gcount
#     gcount += 1
#     print(gcount)
#
# global_test()

# gcount = 0
#
#
# def global_test():
#     print(gcount)
#
#
# global_test()

# def make_counter():
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#
#     return counter
#
#
# def make_counter_test():
#     mc = make_counter()
#     print(mc())
#     print(mc())
#     print(mc())
#
#
# make_counter_test()

def scope_test():
    def do_local():
        spam = "local spam"  # 此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错

    def do_nonlocal():
        nonlocal spam  # 使用外层的spam变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
