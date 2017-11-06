def f1():
    a = 10

    def f2():
        # 此处的 a 是局部变量
        a = 20
        print(a)

    print(a)
    f2()
    print(a)


f1()
