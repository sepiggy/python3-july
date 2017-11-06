ACCOUNT = 'qiyue'
PASSWORD = '123456'

user_account = input('Please input account:\n')  # 这是一个表达式, 可以包含函数调用, = 是赋值操作符
user_password = input('Please input password:\n')  # 同上

if ACCOUNT == user_account and PASSWORD == user_password:
    print("succ")
else:
    print("fail")
