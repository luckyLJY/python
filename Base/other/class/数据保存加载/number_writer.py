# 存储数据使用json.dump()

import json

numbers = [2,3,4,5,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    # 存储数据
    json.dump(numbers, f_obj)