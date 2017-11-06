c = 1


# Python 中函数可以嵌套定义
def func1():
    # c = 2

    def func2():
        # c = 3
        print(c)

    func2()


func1()
