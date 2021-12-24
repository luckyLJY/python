import os.path
from datetime import datetime

f_name = 'test.txt'
af_name = r'C:/test.txt'

# 返回路径中基础名部分
basename = os.path.basename(af_name)
print(basename)

# 返回路径中目录部分
dirname = os.path.dirname(af_name)
print(dirname)

# 返回文件的绝对路径
print(os.path.abspath(af_name))

# 返回文件大小
print(os.path.getsize(af_name))
# 返回最近访问时间
atime = datetime.fromtimestamp(os.path.getatime(af_name))
print(atime)

# 返回创建时间
ctime = datetime.fromtimestamp(os.path.getctime(af_name))
print(ctime)

# 返回修改时间
mtime = datetime.fromtimestamp(os.path.getmtime(af_name))
print(mtime)

print(os.path.isfile(dirname))
print(os.path.isdir(dirname))
print(os.path.isfile(f_name))
print(os.path.isdir(f_name))
print(os.path.exists(f_name))