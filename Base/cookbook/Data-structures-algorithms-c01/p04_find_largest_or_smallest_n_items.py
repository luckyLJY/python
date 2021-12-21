''''''
"""
需求：
    查找最大或最小的N个元素
方案：
    使用heapq模块中的nlargest()和nsmallest()解决
知识点：
    1.heapq模块中的nlargest()和nsmallest()方法底层：是将集合数据进行堆排序后放入一个列表中
    例：
    >>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    >>> import heapq
    >>> heap = list(nums)
    >>> heapq.heapify(heap)
    >>> heap
    [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
    2.使用场景
        1.求最大、最小使用min()和max()
        2.N接近集合大小：使用 sorted(items)[:N] 或者是 sorted(items)[-N:]
        3.N的大小大于1远小于N使用该heapq模块中的nlargest()和nsmallest()

"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print("最大3个值：",heapq.nlargest(3,nums))
print("最小3个值：",heapq.nsmallest(3,nums))