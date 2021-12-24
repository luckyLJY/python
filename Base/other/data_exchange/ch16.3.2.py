import json

# 准备数据
# 创建字典对象
py_dict = {'name':'tony','age':30, 'sex':True}
# 创建列表对象
py_list = [1,3]
# 创建元组对象
py_tuple = ('A','B','C')

# 添加列表到字典中
py_dict['a'] = py_list
# 添加元组到字典中
py_dict['b'] = py_tuple

# 编码过程
json_obj = json.dumps(py_dict)
print("编码过程{0}".format(json_obj))
print("json_obj的类型为{0}".format(type(json_obj)))

# 编码过程
json_obj = json.dumps(py_dict,indent=4)
# 输出格式化后的字符串
print("格式化后的字符串{0}".format(json_obj))

# 写入json数据到data1.json文件
with open('data/data1.json','w') as f:
    json.dump(py_dict,f)

# 格式化写入json数据到data2.json文件
with open('data/data2.json','w') as f:
    json.dump(py_dict,f,indent=4)