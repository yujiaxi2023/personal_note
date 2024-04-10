## multiprocessing模块

### 常用方法

假设p是multiprocessing.Process(target=任务函数/函数方法) 的返回值，子进程操作对象

|方法名|描述|
|---|---|
|p.start()|启动子进程，并调用该子进程p中的run()方法|
|p.run()|子进程p启动的时候运行的方法，调用start方法的参数target指定的函数。如果要自定义进程类的时候一定要实现或者重写该方法|
|p.join([timeout])|主进程交出CPU资源，并阻塞等待子进程结束（强调：是主进程处于等待的状态，而进程p是出于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程|
|p.terminate()|强制终止子进程p，不会进行任何清理操作，如果子进程p还创建自己的子进程（孙子进程），这个孙子进程就会称为僵尸进程，使用该方法的时候要小心这种情况。如果子进程p还保存了一个锁lock，那么也将不会被释放，进而导致出现死锁现象。|
|p.is_alive()|检测进程是否存货，如果进程p仍在运行中，就返回True|

#### 常用属性
|属性名|描述|
|---|---|
|p.daemon|默认值是False，如果设置为True，代表进程p为后台运行的，当进程p的父进程终止的时候，进程p也随之终止，而且设定为True之后，子进程p不能创建自己的孙子进程的，daemon属性的值必须在p.start()之前设置|
|p.name|进程的名称|
|p.pid|进程的唯一标识符|


### 创建多进程

首先内存空间划分了4个进程，1个主进程，3个子进程
然后我们先执行主进程进入就绪状态
然后主进程执行，执行到对应的子进程代码的时候一个个放入到就绪队列中
然后交给操作系统来执行，使用multilevel-feedback queue来调度
```python
import multiprocessing  
import os  
import time  
  
def watch():  
    for i in range(3):  
        print("watch tv...", os.getpid())  
        time.sleep(1)  
  
def drink(food):  
    for i in range(3):  
        print(f"drink {food}...", os.getpid())  
        time.sleep(1)  
  
def eat(food):  
    for i in range(3):  
        print(f"eat {food}...", os.getpid())  
        time.sleep(1)  
  
if __name__ == "__main__":  
    print("main processing", os.getpid())  
    # create 3 processing  
    watch_process = multiprocessing.Process(target=watch)  
    # if want transfer data from father processing  
    # you can use kwargs,args to transfer data kwargs传递字典，args传递元组  
    # kwargs可以传递一个到多个数据  
    drink_process = multiprocessing.Process(target=drink, kwargs={"food":"sheep soup"}) # 命名实参  
    eat_process = multiprocessing.Process(target=eat, args=("rice",)) # 位置实参  
  
    # 注意，如果这样写的话，因为start是开启进程操作，并不会阻塞，所以是异步操作  
    watch_process.start()  # 启动的时候主进程不会等待执行，调用之后立马到下一步代码，然后这个子进程就新开一个进程运行
    drink_process.start()  
    eat_process.start()  
  
    print("主程序代码运行结束")  
    # 会发现并发异步这里打印的先出现了，说明这些进程是并发异步的进程
```
![[Pasted image 20231226155123.png]]
在操作系统中就执行的并发，显示的动作顺序是随机排列的
