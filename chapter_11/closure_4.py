def f1():
    a = 10

    def f2():
        # 此处的 a 是局部变量, 并没有引用外部环境变量, 因此不存在闭包
        a = 20
        return a

    return f2

f = f1()
print(f)
print(f.__closure__)