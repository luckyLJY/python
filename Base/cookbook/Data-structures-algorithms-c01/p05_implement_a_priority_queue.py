'''
需求：
    实现一个优先级队列，每次pop操作返回优先级最高的那个元素
方案：
    heapq实现简单优先级队列
实现：
    1.创建PriorityQueue的类
    2.设置队列_queue\下标_index
    3.定义push方法：参数self,item,priority
         我们使用元组(-priority, self._index, item)的原因是：为了更加方便的做比较，如果有相同优先级的priority，
         则按插入顺序index进行比较，因为index永远不会重复（一定会比较出结果），所以即使后面的item为不可以比较的元素也无妨。
    4.定义pop方法：使用pop弹出元素
    5.item类的定义：属性name,__repr__():输出实例化对象

'''

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    # priority 为优先级，相同优先级选用index
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self,name):
        self.name = name

    # 打印对象
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()

q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())