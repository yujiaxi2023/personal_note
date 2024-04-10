对于初学者，分不清print和return
例如：
```python
def add(n1,n2):  
    print(n1+n2)  

v1 = add(1,3) # 这里默认返回none，所以v1是none
print(v1)
# 输出4和none

def plus(a1,a2):  
    return a1 + a2

v2 = plus(1,3) # 内部返回4所以虽然显示是一样的结果，但是过程不一样
print(v2) 
```
两个函数完全不一样
- 函数中使用print，只是用于在某个位置输出内容
- 在函数中使用return，是为了将函数的执行结果返回给调用者，便于后续的其他操作

在调用和执行函数的时候，要学会分析函数的执行步骤
```python
def f1():  
    print(123)  
  
def f2(arg):  
    ret = arg()  
    return ret  
  
v1 = f2(f1)  
print(v1)
```
分析这个过程：
- 第一是f1传参到f2中
- 执行f1函数并赋值给ret
- f1函数返回值None，ret赋值None
- f2返回值ret，也就是None
- v1 赋值f2返回值，None
- 打印None

```python
def f1():  
    print(123)  
  
def f2(arg):  
    ret = arg()  
    return f1  
  
v1 = f2(f1)  # f1函数
  
v2 = v1()   
print(v2)
```
这个过程：
- 首先是执行f1，打印123
- 赋值ret
- 是f2的返回值一定是f1
- v1赋值f1
- 执行v1也就是f1，打印123
- 返回值None
- v2赋值None
