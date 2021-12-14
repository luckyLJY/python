# 读取文件
'''
文件路径
linux:with open('text_files\filename.txt') as file_object:
window:with open('text_files/filename.txt') as file_object:
'''
with open('pi_digits.txt') as file_object:
    # 文件列表
    lines = file_object.readlines()
    '''逐行读取'''
    pi_string = ''
    for line in lines:
        print(line.rstrip())
        # 使用文件内容
        pi_string += line.strip()

birthday = input("Enter your birthday,in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first millions digits of pi")
else:
    print("Your birthday does not appear in the first million digits of pi")

'''
    # 读取文件
    contents = file_object.read()
    print(contents)
    # 删除右边的空白
    print(contents.rstrip())

print(pi_string)
print(len(pi_string))
'''