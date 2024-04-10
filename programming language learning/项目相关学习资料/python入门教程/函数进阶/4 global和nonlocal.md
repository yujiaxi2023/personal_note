```python
a = 10  
  
def func():  
    a = 20  
  
func()  
print(a) # 此时打印的还是20,因为func中是创建一个局部变量,并没有改变全局变量
```
正常来说，函数内部定义的变量，如果要改变全局变量
需要将全局变量使用global函数弄到函数里面

```python
# 如果需要在函数内部修改全局变量  
def func():  
    global a # 将外边的全局变量引入到局部  
    a = 20  
  
func()  
print(a)
```

global: 在局部引入全局变量

如果我是需要在局部变量中进行修改，直接使用global是没有用的
```python
def function():  
    a = 10  
    def func2():  
        global a  
        a = 20  
    func2()  
    print(a)  
  
function()  
# 此时涉及到的是局部变量的更改,使用global就没有作用
```

nonlocal：在局部引入外层的局部变量，向外找一层有没有该变量，如果有就引入，如果没有就继续往外找一层，指导最外层的函数
```python
def function():  
    a = 10  
    def func2():  
        nonlocal a  
        a = 20  
    func2()  
    print(a)  
  
function()  
# 此时涉及到的是局部变量的更改,使用global就没有作用
```

