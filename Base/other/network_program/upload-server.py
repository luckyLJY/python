import socket

HOST = ''
PORT = 8888

f_name = "2021-09-29_09544.png"

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(10)
    print('服务启动...')

    while True:
        with s.accept()[0] as conn:
            buffer = []
            while True:
                data = conn.recv(1024)
                if data:
                    buffer.append(data)
                else:
                    break
            b =bytes().join(buffer)
            with open(f_name,'wb') as f:
                f.write(b)
            print('服务器接受完毕')