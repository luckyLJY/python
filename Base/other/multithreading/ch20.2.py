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
