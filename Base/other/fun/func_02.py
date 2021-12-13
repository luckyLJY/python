#测试形参、实参的基本用法

def printMax(a,b):
    '''用于比较两个数的大小，打印大的值'''
    if a > b:
        print(a,"较大值")
    else:
        print(b,"较大值")

printMax(10,20)
#打印文档字符串
help(printMax.__doc__)