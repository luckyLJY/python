f_name = '2021-09-29_095447.png'

with open(f_name,'rb') as f:
    b = f.read()
    copy_f_name = 'copy.png'
    with open(copy_f_name,'wb')as copy_f:
        copy_f.write(b)
        print('文件复制成功')