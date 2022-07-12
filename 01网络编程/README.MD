## 网络通信概述
#### udp
1. socket简介
    - 创建udp套接字
        ```python
            # 创建tcp的套接字
            import socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # 关闭套接字
            s.close()
        ```
    - 创建TCP套接字
        ```python
            import socket
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.close()
        ```
    - 操作流程
        1. 创建套接字
        2. 使用套接字收/发数据
2. demo