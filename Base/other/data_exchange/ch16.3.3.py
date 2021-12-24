# coding=utf-8
import json

# 数据准备
js_obj = r'{"name":"tony","age":30,"sex":true,"a":[1,3],"b":["A","B","C"]}'


py_dict = json.loads(js_obj)
print(type(py_dict))
print("py_dict的类型{0}".format(type(py_dict)))

print("name:{0}".format(py_dict['name']))
print("age:{0},sex:{1}".format(py_dict['age'],py_dict['sex']))

# 取出列表对象
py_lista = py_dict['a']
print("lista:{0},listb:{1}".format(py_lista,py_dict['b']))

# 读取json数据到data2.json文件
with open('data/data2.json','r') as f:
    data = json.load(f)
    print("data2的json串{0}",data)
    print("data的类型:{0}".format(type(data)))