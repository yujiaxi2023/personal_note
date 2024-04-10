### join方法

主进程会等待子进程结束的时候结束，主进程需要回收子进程的资源，接着主进程结束以后回收主进程的资源。主进程创建后会自动创建主线程，主线程也会随着子线程结束之后，主线程结束。因为主线程结束，主进程就结束，因为多线程也是并发，所以如果一个任务需要主线程所有代码要等待子线程全部结束之后执行，要怎么做。

使用join代码：
```python
import time  
from threading import Thread, currentThread  
  
def func():  
    time.sleep(2)  
    # 当前线程对象  
    t = currentThread()  
    print(f'线程{t.getName()}运行了')  
  
if __name__ == '__main__':  
    t = Thread(target=func, name="1号")  
    t.start()  
    print(t.is_alive())  
    t.join()  
    print("主线程运行结束")  
    print(t.is_alive())
```
这就可以让主线程同步阻塞

可以使用enumerate方法和activeCount方法查看运行线程的数量和列表
```python
import time  
from threading import Thread, currentThread, activeCount, enumerate  
  
def func():  
    # 当前线程对象  
    time.sleep(2)  
    t = currentThread()  
    print(f'线程[{t.name}]运行了')  
  
  
if __name__ == '__main__':  
    thread_list = []  
    for i in range(1, 11):  
        t = Thread(target=func, name=f"{i}号")  
        t.start()  
    print(activeCount(), enumerate()) # 11个线程，然后一个主线程，其余子线程  
    # enumerate()列表，等于[所有子线程+主线程]  
    # activeCount() = len(enumerate())
```

守护进程守护线程
作用之一是报活就是发送心跳包
```python
import time  
from threading import Thread  
  
# 守护进程/守护线程，都是用来实现报活，也就是心跳包的发送  
def funcDeamon():  
    """报活程序"""  
    while True:  
        time.sleep(1)  
        print("程序继续运行中")  
  
def func():  
    """线程要运行的代码"""  
    for i in range(30):  
        time.sleep(3)  
        print("任务线程在工作")  
  
if __name__ == '__main__':  
    # 先启动守护线程  
    t = Thread(target=funcDeamon)  
    t.setDaemon(True)  
    t.start()  
  
    # 开启任务程序  
    t = Thread(target=func)  
    t.start()
```
