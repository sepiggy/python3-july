# a = 25


def curve_pre():
    a = 25

    def curve(x):
        return a * x * x

    return curve


a = 10
f = curve_pre()
# 打印闭包
print(f.__closure__)
# 打印环境变量
print(f.__closure__[0].cell_contents)
print(f(2))
