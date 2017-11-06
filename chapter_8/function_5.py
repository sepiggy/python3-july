def demo(param1, *param, param2=2):
    print(param1)
    print(param)
    print(param2)


def demo2(param1, param2=2, *param):
    print(param1)
    print(param)
    print(param2)


demo('a', 1, 2, 3, 4, 5, 'param', param2=2)
# demo2('a', param2=1, 2, 3, 4, 5, 'param')
