# curve_pre 和 curve_pre1 虽然返回的函数一样, 但环境变量不同, 因此返回的是两个不同的闭包
def curve_pre():
    a = 25

    def curve(x):
        return a * x * x

    return curve


def curve_pre1():
    a = 30

    def curve(x):
        return a * x * x

    return curve
