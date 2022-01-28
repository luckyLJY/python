import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',8888))
print('服务器启动。。。')

data,client_adress = s.recvfrom(1024)
print('从客户端接受消息:{0}'.format(data.decode()))
s.sendto('您好'.encode(),client_adress)

s.close()