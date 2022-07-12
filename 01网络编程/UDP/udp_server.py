import socket

def main():

    udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_server_socket.bind(('',8888))
    while True:
        recv_data = udp_server_socket.recvfrom(1024)
        recv_msg = recv_data[0] # 存储接受的数据
        send_addr = recv_data[1] # 存储发送方的地址信息
        print("%s:%s"% (str(send_addr),recv_msg.decode("utf-8")))
    udp_server_socket.close()
if __name__ =="__main__":
    main()
