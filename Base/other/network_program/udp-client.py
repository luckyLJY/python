import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(b'hello',('127.0.0.1',8888))

data,_ = s.recvfrom(1024)
print('从服务端接受消息:{0}'.format(data.decode()))

s.close()