import socket

HOST = '127.0.0.1'
PORT = 8888

f_name = 'test_write.txt'

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind((HOST,PORT))
    print('服务器启动.....')

    buffer = []
    while True:
        data,_ = s.recvfrom(1024)
        if data:
            flag = data.decode()
            if flag == 'byte':
                break
            buffer.append(data)
        else:
            continue
    b = bytes().join(buffer)
    with open(f_name,'w') as f:
        f.write(b.decode())

    print('服务器接受完成.')