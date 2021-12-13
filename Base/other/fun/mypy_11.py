# 测试参数的类型：位置参数、默认值参数、命名参数

def test01(a,b,c,d):
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))

# 默认参数值
def test02(a,b,c = 1,d = 1):
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))


test01(10,20,30,40) #位置参数

test01(d = 20,b = 40, c = 10, a = 30)#命名参数

test02(2,3)