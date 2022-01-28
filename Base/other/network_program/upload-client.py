import socket

HOST = '127.0.0.1'
PORT = 8888
f_name = '2021-09-29_095447.png'

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

    with open(f_name,'rb') as f:
        b = f.read()
        s.sendall(b)
        print('客户端上传数据完成')