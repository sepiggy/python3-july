import time


def decorator(func):
    # 可变参数
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function named ' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)


@decorator
def f3(func_name, **kw):
    print('This is a function named ' + func_name)
    print(kw)
    print(type(kw))


f1('sss')
f2('xxx', 'yyy')
f3('zzz', a=1, b=2, c='123')
