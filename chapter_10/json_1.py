import json

# json_str 是 str
json_str = '[{"name":"qiyue", "age":18, "flag":false}, {"name":"bayue", "age":20}]'

# student 是 dict 类型
student = json.loads(json_str)
print(type(student))
print(student)
print(student[0]['name'])
print(student[1]['age'])
