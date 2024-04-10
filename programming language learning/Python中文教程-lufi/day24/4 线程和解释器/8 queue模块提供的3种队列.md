## 队列

前面的进程学习种，学习了multiprocessing进程模块提供的Queue队列模块，这个模块可以实现进程的IPC通信

队列（queue），就是一种先进先出（FIFO， First In First Out）的数据结构，是保存1组数据的容器。
叫做数据结构，实际上就是给计算机储存数据用的一种结构体。队列的概念跟生活上类似。队列是有序数据集合，队列的特点，删除数据项再头部，成为前端（front），添加数据是在尾部，称为后端（Rear）
![[Pasted image 20240214154149.png]]

#### 简单实现
```python
class MyQueue(object):  
    """  
    自定义队列  
    """    def __init__(self, size=None):  
        self.maxsize = size  
        self.items = [] # 类似于python的list，PHP的Array数组，Java的动态数组，go的列表，都可以实现一些基本的队列结构  
  
    def is_empty(self):  
        """判断队列是否是空，也就是队列的长度是否为0"""  
        return self.items == []  
  
    def size(self):  
        """获取队列长度"""  
        return len(self.items)  
  
    def enqueue(self, item):  
        """进队，在列表的头部添加成员"""  
        if self.maxsize > self.size() or self.maxsize is None:  
            self.items.insert(0, item)  
        else:  
            raise Exception("队列已满！")  
  
    def dequeue(self):  
        """出队"""  
        if not self.is_empty():  
            return self.items.pop()  
        else:  
            raise Exception("队列为空！")  
  
    def size(self):  
        """获取队列长度"""  
        return len(self.items)  
  
if __name__ == '__main__':  
    q = MyQueue(3)  
    q.enqueue("hello")  
    q.enqueue("world")  
    q.enqueue("python")  
  
    print(q.size())  
    print(q.dequeue())  
    print(q.dequeue())  
    print(q.dequeue())  
    print(q.is_empty())
```
这就是使用python的list来实现queue的方式

除了multiprocessing提供的Queue可以实现进程队列之外，python还提供了Queue内置模块，可以让我们在开发中实现同步的线程安全的队列效果，让多线程实现同步通信，器用法和进程Queue一样，python内置的Queue模块。一共提供了3种不同的队列：

python内置的Queue模块，不仅提供了先进先出队列，还提供了后进先出队列（LIFO，Last In First Out）和优先级队列（FILO，First In, Largest Out)，当然这三种队列都可以在多线程中实现同步通信，保证线程安全，有锁机制
#### 先进先出队列（First-in-First-out)FIFO队列

```python
from multiprocessing import Queue # 此处是进程的队列  
import queue # 这是python实现队列数据结果的另一个队列模块  
  
from collections import Sequence # 这是另一种队列  
  
# 初始化的时候可以指定队列对象的长度，如果不添加参数，就是无限长度  
q = queue.Queue(3)  
  
print(q.empty()) # 判断队列是否为空，但是并不可靠，在并发情况下  
q.put(1)  
q.put(2)  
q.put(3) # put次数不可以超过队列长度，否则会出现阻塞，linux会出现报错  
print(q.qsize()) # 获取当前对象的长度，并不可靠，在并发情况下  
print(q.get())  
print(q.get())  
print(q.get()) # 同样get也不可以超过put的长度，否则同样出现阻塞，linux出现报错  
"""  
只有get和put方法是可靠的  
在并发情况下  
"""  
print(q.qsize()) # 0  
print(q.empty()) # True
```

先进先出队列一般可以用于餐厅的排号系统，或者抢票系统等地方
有时候也称之为链表结构

#### 后进先出队列Last In First Out
和普通队列提供的操作一样，只是后进的队列成员，最先出队
```python
import queue  
  
# 主要是栈在使用  
# 栈是一种数据结构  
# 栈只有一个出入口  
q = queue.LifoQueue(3)  
  
q.put("hello")  
q.put(1)  
q.put([1,2,3])  
print(q.qsize()) # 3  
print(q.empty()) # False  
# 如果多添加成员就会阻塞或者报错  
print(q.get())  
print(q.get())  
print(q.get()) # 同样，多提取成员也会出错  
"""  
3  
False  
[1, 2, 3]  
1  
hello  
可以看到get到的东西是最后put进入的  
"""
```
这个一般跟栈相关
栈是一种数据结构
队列一般是一个队列有两个端口，一个进口一个出口
![[Pasted image 20240214162334.png]]
栈只有一个出口
![[Pasted image 20240214162355.png]]
使用后进先出队列可以实现栈的效果

后进先出队列可以使用在软件的历史记录回滚的任务中

#### 优先级队列First In Largest Out

优先级队列会给每一个成员设置一个优先级的数字，优先级数字最小的最先出队，当优先级一样的时候，按照先进先出的原则

```python
import queue  
  
q = queue.PriorityQueue(3)  
"""  
优先级队列的成员是一个元组(优先级，成员值）  
  
在元组中设置一个优先值，优先级数字小的最先出列  
可以是数字，也可以是支持排序的非数字字符  
"""  
q.put((20, "hello"))  
q.put((1, [1,2,3]))  
q.put((3, 1))  
print(q.empty())  
print(q.qsize())  
print(q.get())  
print(q.get())  
print(q.get())
```

这个一般会实现游戏中的VIP会员和普通用户的之中
但是VIP和普通会员是统一线程中进入，但是总是VIP先排队登录，后边普通用户排队登录

**注意put中的输入一定是元组**

游戏场景爆满的时候，VIP用户和普通用户排队的算法需要任务调度