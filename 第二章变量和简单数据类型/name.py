
# name.py

name = "ada lovelace"
# 首字母大写
print(name.title())
# 全部转化为大写
print(name.upper())
# 全部转换为小写
print(name.lower)
# 合并字符串使用 +
last_name = "Hello"
print(last_name + name)

'''
string.rstrip()删除尾部空白
string.lstrip()删除头部空白
string.strip()删除两头空白
'''
r_blanck = "abc "
l_blanck = " abc"
double_blank= " abc "
print("删除尾部空白" + r_blanck.rstrip())
print("删除头部空白" + r_blanck.lstrip())
print("删除两头空白" + r_blanck.strip())