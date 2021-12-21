'''
需求：
    一个键对应多个值的字典(multidict)
设计：
    1.需要将多个值放到另外的容器中
    2.想保持元素的插入顺序就应该使用列表
    3.想去掉重复元素就使用集合（并且不关心元素的顺序问题）。
实现：
    1.采用collections模块中的defaultdict来构造字典
    2.defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值
'''
from collections import defaultdict

#列表--保证插入按原来顺序
d = defaultdict(list)
d['a'].append(2)
d['a'].append(1)
d['b'].append(4)
print(d)
#集合--有序
d = defaultdict(set)
d['a'].add(2)
d['a'].add(1)
d['b'].add(4)
print(d)

'''
defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。 如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。比如：

d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
'''

#一键多值实现

'''
自己实现
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
'''

'''
通过defaultdict实现
d = defaultdict(list)
for key,value in pairs:
    d[key].append(value)
'''
