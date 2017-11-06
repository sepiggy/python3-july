# 序列化
import json

student = [
    {'name': 'qiyue', 'age': 18, 'flag': False},
    {'name': 'qiyue', 'age': 19}
]

json_str = json.dumps(student)
print(json_str)
