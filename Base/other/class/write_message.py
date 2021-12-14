# 写文件
filename = 'programming.txt'
'''
with open(filename,'w') as file_object:
    # 写入文件 可以写入多行以重写方式写入
    file_object.write("I love programming")
    file_object.write("I love creating new games\n")
    # 添加分行字符
    file_object.write("I love creating new games")
'''
# 附加到文件
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")

'''
异常：
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!") 
'''