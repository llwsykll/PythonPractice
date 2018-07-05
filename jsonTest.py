import json
d = dict(name = 'Bob', age = 20, score = 88)
print(json.dumps(d))

json_str = '{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str))

obj = dict(name= '小明',age=20)
print(json.dumps(obj,ensure_ascii=True))