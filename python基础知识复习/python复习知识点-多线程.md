## 多线程编程
#### threading模块
- thread.active_count():返回当前处于活动状态的线程个数
- thread.current_thread():返回当前的Thread对象
- thread.main_thread():返回主线程对象，主线程Python解释器启动的线程 

    ```python
    import threading

    # 当前线程对象
    t = threading.current_thread()
    # 当前线程名
    print(t.name)

    # 返回当前处于活跃状态的线程个数
    print(threading.active_count())

    # 当前线程对象
    t = threading.main_thread()
    # 主线程名称
    print(t.name)
    ```
#### 创建线程
- 线程对象：线程对象是threading模块线程类Thread所创建的对象。   
- 线程体：线程执行函数。  

提供线程体的两种方式：    
- 自定义函数作为线程体
- 继承Thread类重写run()方法，run()方法作为线程体。  
1. 自定义函数作为线程体  
threading.Thread(target=None,name=None,args=())  
    ```python
    import threading
    import time

    # 线程体函数
    def thread_body():
        # 当前线程对象
        t = threading.current_thread()
        for n in range(5):
            # 当前线程名
            print('第{0}次执行线程{1}'.format(n,t.name))
            # 线程休眠
            time.sleep(1)
        print('线程{0}执行完成！'.format(t.name))

    def main():
        # 创建线程对象t1
        t1 = threading.Thread(target=thread_body)
        # 启动线程t1
        t1.start()

        # 创建线程t2
        t2 = threading.Thread(target=thread_body,name='MyThread')
        # 启动线程t2
        t2.start()

    if __name__ == '__main__':
        main()
    ```

2. 继承Thread线程类实现线程体  
    ```python
    import threading
    import time

    class MyThread(threading.Thread):
        def __init__(self,name=None):
            super().__init__(name=name)

        # 线程体函数
        def run(self):
            # 当前线程对象
            t = threading.current_thread()
            for n in range(5):
                # 当前线程名
                print('第{0}次执行线程{1}'.format(n,t.name))
                # 线程休眠
                time.sleep(1)
            print('线程{0}执行完成！'.format(t.name))

    def main():
        # 创建线程对象t1
        t1 = MyThread()
        t1.start()

        t2 = MyThread(name='MyThread')
        t2.start()

    if __name__ == "__main__":
        main()
    ```
#### 线程管理  
1. 等待线程结束  
join()方法：当前线程调用t1线程的join()方法时则阻塞当前线程，等待t1线程结束，如果t1线程结束或等待超时，则当前回到活动状态继续执行。语法如下：   
join(timout=None)   
    ```python
    import threading
    import time

    # 共享变量
    value = 0

    # 线程体函数
    def thread_body():
        global value
        # 当前线程对象
        print('ThreadA开始...')
        for n in range(2):
            print('ThreadA执行....')
            value += 1
            # 线程休眠
            time.sleep(1)
            print('ThreadA 结束....')

    def main():
        print('主线程开始....')
        # 创建线程对象t1
        t1 = threading.Thread(target=thread_body,name='ThreadA')
        # 启动线程t1
        t1.start()
        # 主线程阻塞，等待t1线程结束
        t1.join()
        print('value = {0}'.format(value))
        print('主线程 结束...')

    if __name__ == '__main__':
        main()
    ```
2. 线程停止  
    ```python
    import threading
    import time

    # 线程停止变量
    isrunning = True

    # 线程体函数
    def thread_body():
        while isrunning:
            # 线程开始工作
            print('下载中.....')
            # 线程休眠
            time.sleep(5)
        print('执行完成')

    def main():
        # 创建线程对象t1
        t1 = threading.Thread(target=thread_body)
        # 启动线程t1
        t1.start()
        # 从键盘输入停止指令
        command = input('请输入停止指令：')
        if command == 'exit':
            global isrunning
            isrunning = False
    if __name__ == '__main__':
        main()
    ```

#### 线程安全
1. 临界资源问题  
    售票问题；  
2. 多线程同步  
    Lock对象：锁定和非锁定状态，默认是未锁定状态。Lock对象有acquire()和release()实现锁定和解锁。   
    ```python
    import threading
    import time

    class TicketDB:
        def __init__(self):
            # 机票的数量
            self.ticket_count = 5

        # 获得当前机票的数量
        def get_ticket_count(self):
            return self.ticket_count

        # 销售机票
        def sell_ticket(self):
            # TODO 等与用户付款
            # 线程休眠，阻塞当前线程，模拟等待用户付款
            time.sleep(1)
            print("第{0}号票，已经售出".format(self.ticket_count))
            self.ticket_count -= 1

    # 创建TicketDB对象
    db = TicketDB()
    # 创建Lock对象
    lock = threading.Lock()

    # 线程体1函数
    def thread1_body():
        global db,lock # 声明为全局变量
        while True:
            lock.acquire()
            curr_ticket_count = db.get_ticket_count()
            # 查询是否有票
            if curr_ticket_count > 0:
                db.sell_ticket()
            else:
                lock.release()
                # 无票退出
                break
            lock.release()
            time.sleep(1)

    # 线程体1函数
    def thread2_body():
        global db,lock # 声明为全局变量
        while True:
            lock.acquire()
            curr_ticket_count = db.get_ticket_count()
            # 查询是否有票
            if curr_ticket_count > 0:
                db.sell_ticket()
            else:
                lock.release()
                # 无票退出
                break
            lock.release()
            time.sleep(1)

    # 主函数
    def main():
        # 创建线程对象t1
        t1 = threading.Thread(target=thread1_body)
        t1.start()
        t2 = threading.Thread(target=thread2_body)
        t2.start()


    if __name__ == '__main__':
        main()
    ```

#### 线程间通信
1. Condition   
Condition被称为条件变量，提供了对复杂线程同步问题的支持，除了提供Lock类似的acquire()和release()方法外，还提供了wait()、notify()和notify_all()方法；   
    - wait(timout=None):使当前线程释放锁，然后当前线程处于阻塞状态，等待相同条件变量中其他线程唤醒或超时，timeout是设置超时时间；  
    - notify():唤醒相同条件变量中的一个线程；  
    - notify_all():唤醒相同条件变量中的所有线程。   
    
    堆栈类代码：  
        ```python
        import threading
        import time

        # 创建条件变量对象
        condition = threading.Condition()


        class Stack:
            def __init__(self):
                # 堆栈指针初始值为0
                self.pointer = 0
                # 堆栈有5个数字的空间
                self.data = [-1, -1, -1, -1, -1]

            # 压栈方法
            def push(self, c):
                global condition
                condition.acquire()
                # 堆栈已满，不能压栈
                while self.pointer == len(self.data):
                    # 等待其它线程把数据出栈
                    condition.wait()
                # 通知其他线程把数据出栈
                condition.notify()
                # 数据压栈
                self.data[self.pointer] = c
                # 指针向上移动
                self.pointer += 1
                condition.release()

            # 出栈方法
            def pop(self):
                global condition
                condition.acquire()
                # 堆栈无数据，不能出栈
                while self.pointer == 0:
                    # 等待其他线程把数据压栈
                    condition.wait()
                # 通知其他线程压栈
                condition.notify()
                # 指针向下移动
                self.pointer -= 1
                data = self.data[self.pointer]
                condition.release()
                # 数据出栈
                return data


        # 创建堆栈Stack对象
        stack = Stack()


        # 生产者线程体函数
        def producer_thread_body():
            global stack  # 声明为全局变量
            # 产生10个数字
            for i in range(0, 10):
                # 把数字压栈
                stack.push(i)
                # 打印数字
                print('生产：{0}'.format(i))
                # 每产生一个数字线程就睡眠
                time.sleep(1)


        # 消费者线程体函数
        def consumer_thread_body():
            global stack  # 声明为全局变量
            # 从堆栈中读取数字
            for i in range(0, 10):
                # 从堆栈中读取数字
                x = stack.pop()
                # 打印数字
                print('消费：{0}'.format(x))
                # 每消费一个数字线程就睡眠
                time.sleep(1)


        # 主函数
        def main():
            # 创建生产者线程对象producer
            producer = threading.Thread(target=producer_thread_body)
            # 启动生产者线程
            producer.start()
            # 创建消费者线程对象consumer
            consumer = threading.Thread(target=consumer_thread_body)
            # 启动消费者线程
            consumer.start()


        if __name__ == '__main__':
            main()
        ```
    第1行创建了条件变量对象。代码第2行定义了Stack堆栈类，该堆栈有最多5个元素的空间，代码第3行定义并初始化了堆栈指针，堆栈指针是记录栈顶位置的变量。代码第4行是堆栈空间，-1表示没有数据。   
    代码第5行定义了压栈方法push(),该方法中的代码需要同步，因此在该方法开始时通过condition.acquire()语句加锁，在该方法结束时通过condition.release()语句解锁。另外，在该等待状态中，如果堆栈未满，程序会往下运行调用condition.notify()唤醒一个线程。     
       
2. Event 
Event对象调用wait(timeout=None)方法会阻塞当前线程，使线程进入等待状态，直到另一个线程该Event对象的set()方法，通知所有等待状态的线程恢复运行。  
    ```python
            import threading
            import time

            event = threading.Event()

            class Stack:
                def __init__(self):
                    # 堆栈指针初始值为0
                    self.pointer = 0
                    # 堆栈有5个数字的空间
                    self.data = [-1,-1,-1,-1,-1]

                # 压栈方法
                def push(self,c):
                    global event
                    # 堆栈已满，不能压栈
                    while self.pointer == len(self.data):
                        # 等待其他线程把数据出栈
                        event.wait()
                    # 通知其他线程把数据出栈
                    event.set()
                    # 数据压栈
                    self.data[self.pointer] = c
                    # 指针向上移动
                    self.pointer += 1

                # 出栈方法
                def pop(self):
                    global event
                    # 堆栈无数据，不嫩出栈
                    while self.pointer == 0:
                        # 等待其他线程把数据压栈
                        event.wait()
                    # 指针向下移动
                    self.pointer -= 1
                    # 数据出栈
                    data = self.data[self.pointer]
                    return data


            # 创建堆栈Stack对象
            stack = Stack()


            # 生产者线程体函数
            def producer_thread_body():
                global stack  # 声明为全局变量
                # 产生10个数字
                for i in range(0, 10):
                    # 把数字压栈
                    stack.push(i)
                    # 打印数字
                    print('生产：{0}'.format(i))
                    # 每产生一个数字线程就睡眠
                    time.sleep(1)


            # 消费者线程体函数
            def consumer_thread_body():
                global stack  # 声明为全局变量
                # 从堆栈中读取数字
                for i in range(0, 10):
                    # 从堆栈中读取数字
                    x = stack.pop()
                    # 打印数字
                    print('消费：{0}'.format(x))
                    # 每消费一个数字线程就睡眠
                    time.sleep(1)


            # 主函数
            def main():
                # 创建生产者线程对象producer
                producer = threading.Thread(target=producer_thread_body)
                # 启动生产者线程
                producer.start()
                # 创建消费者线程对象consumer
                consumer = threading.Thread(target=consumer_thread_body)
                # 启动消费者线程
                consumer.start()


            if __name__ == '__main__':
                main()
            ```
