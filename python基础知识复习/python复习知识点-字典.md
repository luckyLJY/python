## 元组
#### 字典元素的添加  
1. 给字典新增“键值对”。如果“键”已经存在，则覆盖旧的键值对；如果“键”不存在，则新增“键值对”。

   ```python
   >>> a = {'name':'gaoqi','age':18,'job':'programmer'}
   >>> a['address'] = '西三期1号院'
   >>> a['age'] = 16
   >>> a
   {'name': 'gaoqi', 'age': 16, 'job': 'programmer', 'address': '西三期1号院'}
   ```
2. 使用update()将新字典中所有键值对全部添加到旧字典对象上。如果key相同会直接覆盖。

   ```python
   >>> a = {'name':'zhangsan','age':18,'job':'programmer'}
   >>> b = {'name':'lisi','money':1000,'sex':'男'}
   >>> a.update(b)
   >>> a
   {'name': 'lisi', 'age': 18, 'job': 'programmer', 'money': 1000, 'sex': '男'}
   ```
#### 字典的删除
1. 字典中元素的删除，可以使用del()方法；或者clear()删除所有键值对；pop()删除指定键值对，并返回对应的值对象

   ```python
   >>> a = {'name':'gaoqi','age':18,'job':'programmer'}
   >>> del(a['name'])
   >>> a
   {'age': 18, 'job': 'programmer'}
   >>> b = a.pop('age')
   >>> b
   18
   ```
2. popitem():随机删除和返回该键值对。字典是“无序可变列”，因此没有第一个元素、最后一个元素的概念；popitem弹出随机的项，因为字典并没有“最后的元素”或者其他有关顺序的概念。若想一个接一个地移除并处理项，这个方法非常有效.

   ```python
   
   >>> a = {'name':'gaoqi','age':18,'job':'programmer'}
   >>> a.popitem()
   ('job', 'programmer')
   >>> a
   {'name': 'gaoqi', 'age': 18}
   >>> a.popitem()
   ('age', 18)
   >>> a
   {'name': 'gaoqi'}
   ```
#### 赋值(序列解包)
序列解包可以用于元组、列表、字典。序列解包可以让我们方便的对多个变量赋值

```python
>>> x,y,z=(20,30,10)
>>> x
20
>>> y
30
>>> z
10
>>> (a,b,c) = (9,8,10)
>>> a
9
>>> [a,b,c] = [10,20,30]
>>> a
10
>>> b
20
```
序列解包用于字典时，默认是对“键”进行操作；如果需要对键值对操作，则需要使用items();如果需要对“值”进行操作，则需要使用values();  
```python
>>> s = {'name':'gaoqi','age':18,'job':'programmer'}
>>> name,age,job = s	#默认对键进行操作
>>> name
'name'
>>> name,age,job = s.items() #对键值进行操作
>>> name
('name', 'gaoqi')
>>> name,age,job = s.values() #对值进行操作
>>> name
'gaoqi'
``` 
### 字典底层原理

```python
字典对象的核心是散列表。散列表是一个稀疏的数组，数组的每个单元叫做bucket。每个bucket有两个分：一个是键对象的引用，一个是值对象的引用。
所有的bucket大小和结构一致，可以通过偏移量来读取指定的bucket
```

用法总结：

1. 键必须可散列
   1. 数字、字符串、元组都是可散列的。
   2. 自定义对象需要支持下面三点
      1. 支持hash()函数
      2. 支持通过__eq __()方法检测相等性
      3. 若a==b为真，则hash(a)==hash(b)也为真。
2. 字典在内存中开销巨大，典型的时间换空间
3. 键查询速度很快
4. 往字典里面添加新建可能导致扩容，导致散列表中键的次序变化。因此，不要在遍历字典的同时进行字典的修改