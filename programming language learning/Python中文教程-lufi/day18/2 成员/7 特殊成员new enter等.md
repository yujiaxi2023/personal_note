在python的类中存在一些特殊的方法,这些方法都是`__方法__`格式,这种方法在内部均有特殊的含义,接下来我们来讲一些常见的特殊成员:

常见的有以下的十二种

- `__init__`初始化方法
```python
# __init__ 初始化方法  
class Foo(object):  
    def __init__(self,name):  
        self.name = name  
  
obj = Foo('wupeiqi')
```
实例化对象的时候会自动触发,并且参数会自动传入到init函数中

- `__new__` 构造方法
```python
# __new__ 构造方法  
class Foo(object):  
    def __init__(self,name):  
        print("第二步:初始化对象,在空对象中创建数据")  
        self.name = name  
  
    def __new__(cls, *args, **kwargs):  
        print("第一步:先创建空对象并写返回")  
        return object.__new__(cls)  
  
obj = Foo("eupeiqi")
```
new方法在初始化init方法之前触发的
作用是实例化,创建对象
其实实例化对象的时候,第一步不是执行init,而是执行new方法
会调用`object.new`创建一个空对象
如果执行上边这个代码的时候,会先触发new方法
一般写代码的时候会省略,但是会自动执行new方法
因为py3默认每个函数创建的时候会继承一个父类的object
而object中有new方法会被执行


- `__call__`
```python
# __call__  
class Foo(object):  
    def __call__(self, *args, **kwargs):  
        print("执行call方法")  
  
obj = Foo()  # init和new方法执行
obj() # call方法执行
```
call方法
如果一个类(),这就是执行new和init方法
如果是实例化对象(),这就是执行类里面的call方法


- `__str__`
```python
# __str__  
class Foo(object):  
    def __str__(self):  
        return "hahahha"  
  
obj = Foo()  
data = str(obj)  
print(data)  
  
"""  
class Student(object):  
  
    def __init__(self, name, age):        self.name = name        self.age = age  
  
s1 = Student('吴佩琦', 19)  
s2 = Student('alex', 19)  
s3 = Student('日天', 19)  
  
  
print(s1) # <__main__.Student object at 0x0000022A660866D0>  
print(s2) # <__main__.Student object at 0x0000022A66203550>  
print(s3) # <__main__.Student object at 0x0000022A66203700>  
# 这样显示并不友好,因为这无法了解内容究竟是什么  
"""  
  
class Student(object):  
    """学生类"""  
  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
    def __str__(self):  
        return f"{self.name}-{self.age}"  
  
s1 = Student('吴佩琦', 19)  
s2 = Student('alex', 19)  
s3 = Student('日天', 19)  
  
data = str(s1)  
  
print(s1) # 吴佩琦-19  
print(s2) # alex-19  
print(s3) # 日天-19  
print(data) # 吴佩琦-19  
# 这样执行,得到的结果自动会执行str方法,所以就会展示字符串  
# 因为print内部就会自动执行str的方法
```
当有一个类,之中定义str方法的时候,必须要返回一个字符串
如果我希望转换对象为字符串类型的数据
就可以在对象外边套一个str,但是这个数据就是str这个方法执行的返回值
这个可以很好的做数据展示

- `__dict__`
```python
# __dict__  
class Foo(object):  
    def __init__(self,name,age):  
        self.name = name  
        self.age = age  
  
obj = Foo("wupeiqi",19)  
obj1 = Foo('五哦额',120)  
print(obj.__dict__) # {'name': 'wupeiqi', 'age': 19}  
print(obj1.__dict__) # {'name': '五哦额', 'age': 120}
```
一个字典
如果有上述的对象
dict方法就是获得这个类的所有的实例变量,搞成一个字典返回
注意是只有实例对象中的所有实例变量
前后端分离的时候会用这个内容

`__getitem__, __setitem__, __delitem__`
```python
# __getitem__, __setitem__, __delitem__  
info = dict()  
info['k1'] = 123 # 创建键值对  
info['k2'] = 145  
print(info)  
  
print(info['k1']) # 根据索引获得值  
del info['k1'] # 根据索引删除键值对  
# 字典的对象支持 对象[""] 这种语法  
# 我们自己创建的类,自己实例化的对象,希望也可以支持这种操作  
# 这时候就需要我们使用这三个方法  
  
class Foo(object):  
  
    def __getitem__(self, item):  
        print(item)  
  
    def __setitem__(self, key, value):  
        print(key, value)  
  
    def __delitem__(self, key):  
        print(key)  
  
obj = Foo()  
  
obj['xxx'] = 123 # 自动触发类中__setitem__方法  
obj['ooo'] # 自动会触发类中__getitem__方法  
del obj['ooo'] # 自动触发类中__delitem__方法  
# 这个方法内部具体干什么随便写,主要是直到这个方法和这种语法是对应的  
# 自定义一些对象的时候可以基于这个方法来做
```

- `__enter__ __exit__`
```python
# __enter__ __exit__ 这两种方法是成对出现的  
class Foo(object):  
  
    def __enter__(self):  
        print("进入了")  
        return 666  
  
    def __exit__(self, exc_type, exc_val, exc_tb):  
        print("出去了")  
  
  
obj = Foo()  
# with 对象 as f     在内部执行__enter__方法 返回值就是as 后边的f接收  
# 当with缩进中的代码执行完毕,就自动会执行__exit__方法  
with obj as data:  
    print(data)  
  
# 也可以写成  
with Foo() as f:  
    print(f)  
  
# 超前知识:数据连接,每次对远程的数据进行操作的时候都必须经历  
# 1. 连接 = 连接数据库  
# 2. 操作数据库  
# 3. 关闭数据  
  
"""  
class SqlHelper(object):  
  
    def __enter__(self):        self.连接 = 连接数据库  
        return 连接  
  
    def __exit__(self, exc_type, exc_val, exc_tb):        self.连接.关闭  
  
with SqlHelper as 连接:  
    连接.操作  
"""
```
操作之前想要做一些操作,操作之后想要做一些事情
那就可以使用这些方法

将连接和断开连接的算法写在enter 和 exit方法中

with这个语法代表,类中一定有enter和exit

```python
# 补充代码,实现如下内容  
class Context:  
  
    def __enter__(self):  
        return self  
  
    def __exit__(self, exc_type, exc_val, exc_tb):  
        pass  
  
    def do_something(self):  
        print("内部执行")  
  
with Context() as ctx:  
    print("内部执行")  
    ctx.do_something()
```

with语法一般称为上下文管理语法

- `__add__`等
```python
# __add__  
v1 = int(1)  
v2 = int(5)  
# 创建两个整形的对象  
v3 = v1 + v2  
print(v3)  
  
# class Foo(object):  
#     pass  
  
# class Foo(object):  
#  
#     def __add__(self, other):  
#         return 999  
  
class Foo(object):  
    def __init__(self,name):  
        self.name = name  
  
    def __add__(self, other):  
        return f"{self.name}-{other.name}"  
        # 所以这里是调用了self和other构成一串字符  
  
    def __mul__(self, other):  
        return 1  
  
    def __sub__(self, other):  
        return  
  
    def __divmod__(self, other):  
        return  
      
  
v1 = Foo('wupeiqi')  
v2 = Foo("sb")  
v3 = v1 + v2 # 直接实例化对象是不支持+操作  
print(v3) # wupeiqi-sb  
# 对象 + 值 的时候,内部会执行对象.__add__方法  
# 会将 + 后边的值当作参数传递过去  
# 所以这里self 代指v1,other代表v2  
# 如果要做的更有意义
```
加减乘除平方都有相关的写法
