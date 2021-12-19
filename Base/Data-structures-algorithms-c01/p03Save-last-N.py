'''
需求：
    在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
实现：
    保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码
在多行上面做简单的文本匹配，并只返回在前 N 行中匹配成功的行：
知识点：
    1.yield 表达式的生成器函数
    2.使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。
    案例
    >>> from collections import deque
>>> q = deque(maxlen = 3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(5)
>>> q
deque([2, 3, 5], maxlen=3)
'''
'''
1.读取文件with open(r'path') as f
2.调用search
    1.从collections中引入deque
    2.通过deque存储包含结果的前n行数据
    3.对文档的内容匹配需要匹配的内容
    4.将匹配后的前n行内容使用yield返回
'''
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
   # print(type(previous_lines))
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
