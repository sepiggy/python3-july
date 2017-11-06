# 使用闭包解决问题
origin = 0


def factory(pos):
    def go(step):
        # pos 是环境变量
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


tourist = factory(origin)

print(tourist(2))
print(tourist(3))
print(tourist(5))
