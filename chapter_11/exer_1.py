# 使用全局变量解决问题
origin = 0


def go(step):
    # 声明一个全局变量
    global origin
    new_pos = origin + step
    origin = new_pos
    return new_pos


print(go(2))
print(go(3))
print(go(6))
