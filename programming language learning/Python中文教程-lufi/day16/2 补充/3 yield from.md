函数中有yield关键字就是生成器函数
```python
def foo():  
    yield 2  
    yield 2  
    yield 2  
  
def func():  
    yield 1  
    yield 1  
    yield 1  
    yield from foo() # 遇到yield from就到指定的生成器继续进行执行生成  
    yield 1  
    yield 1  
  
for item in func():  
    print(item)  
  
"""  
1  
1  
1  
2  
2  
2  
1  
1  
"""  
  
def func1():  
    yield 1  
    yield 1  
    yield 1  
    yield foo() # 输出生成器对象  
    yield 1  
    yield 1  
  
for item in func1():  
    print(item)  
      
"""  
1  
1  
1  
<generator object foo at 0x000002E16F463DD0>  
1  
1  
"""
```

