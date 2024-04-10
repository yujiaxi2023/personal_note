**sorted**：排序
![[Pasted image 20230918234159.png]]
可以看到这个是需要一个可迭代的数据在第一个，然后是reverse与否
```python
lst = [16, 22, 68, 1, 147, 256, 49]  
  
s = sorted(lst)  
s1 = sorted(lst, reverse=True)  
print(s) # [1, 16, 22, 49, 68, 147, 256]  
print(s1) # [256, 147, 68, 49, 22, 16, 1]
```

可以看到数字来说，排序翻转是很容易的
但是对于一些不是数字的变量
```python
lst = ["a", "b", "c", "d", "e"]  
# 如果需要使用sorted,对于这些非数字的应该如何排序?  
  
sorted(lst, key=排序函数, reverse=False)
```
这里是函数接受了一个lst，然后传入给key是一个排序函数
```python
lst = ["a", "b", "c", "d", "e"]  
# 如果需要使用sorted,对于这些非数字的应该如何排序?  
  
def func(item): # 此时item对应的是列表中的每一项数据  
    return len(item)  
      
s = sorted(lst, key=func, reverse=False)
```
这样就可以按照长度进行排序，但是这里是一样长度，输出结果是一样的
但是可以进行lambda简化
```python
lst = ["b", "a", "c", "d", "e"]  
# 如果需要使用sorted,对于这些非数字的应该如何排序?  
  
# def func(item): # 此时item对应的是列表中的每一项数据  
#     return len(item)  
  
func = lambda x: len(x)  
  
s = sorted(lst, key=func, reverse=False)  
print(s) # ['b', 'a', 'c', 'd', 'e']
```
这个时候再看，这里func函数只有这里调用
所以我们可以直接在key后边写lambda函数
```python
lst = ["b", "a", "c", "d", "e"]  
# 如果需要使用sorted,对于这些非数字的应该如何排序?  
  
# def func(item): # 此时item对应的是列表中的每一项数据  
#     return len(item)  
s = sorted(lst, key=lambda x: len(x)  , reverse=False)  
print(s) # ['b', 'a', 'c', 'd', 'e']
```

**练习题**
```python
lst = [  
    {"id":1, "name":"alex", "age":18, "salary":39399},  
    {"id":2, "name":"tom", "age":19, "salary":9299},  
    {"id":3, "name":"wang", "age":32, "salary":9399},  
    {"id":4, "name":"song", "age":41, "salary":3399},  
    {"id":5, "name":"wei", "age":18, "salary":32399},  
    {"id":6, "name":"tony", "age":38, "salary":13399},  
    {"id":7, "name":"salina", "age":68, "salary":139399}  
]  
  
# 1.根据每个人年龄排序  
s = sorted(lst, key=lambda  d: d["age"])  
print(s)  
  
# 2.根据工资排序,从大到小  
s1 = sorted(lst, key=lambda d: d["salary"], reverse=True)  
print(s1)
```
