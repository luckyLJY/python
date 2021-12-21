'''
问题：
    怎样在数据字典中执行一些计算操作 (比如求最小值、最大值、排序等等)？
解决方案：
    prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }
    1.通过zip()将键和值反转
    2.使用min、max、sorted等方法实现
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))
prices_sorted = sorted(zip(prices.values(),prices.keys()))

print(min_price)
print(max_price)
print(prices_sorted)
'''
拓展：
    1.运算作用于键--得到键
        min(prices) # Returns 'AAPL'
        max(prices) # Returns 'IBM'
    2.运算作用于值--得到值
        min(prices.values()) # Returns 10.75
        max(prices.values()) # Returns 612.78
    3.上述方法解决，既要键又要值

'''