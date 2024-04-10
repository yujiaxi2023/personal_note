本次讲解的内置函数有8中,都跟面向对象的知识有关
- classmethod,staticmethod,property
确定方法是调用类方法,还是绑定方法,还是静态方法
其实就是看需要传入什么参数

- callable,是否可以在后边加括号执行
- 函数
```python
def func():
	pass

print(callable(func)) # True
```


- 类
```python
class Foo(object):
	pass
print(callable(Foo)) # True
```


- 类中具有`__call__`方法的对象
```python
class Foo(object):
	pass

obj = Foo()
print(callable(obj)) # False
```
```python
class Foo(object):
	def __call__(self, *args,**kwargs):
		pass
obj = Foo()
print(callable(obj)) # True
```


所以以后见到下面的情况,首先就要想到的handler可以是:函数,类,具有call方法的对象这三种,具体是什么要根据代码调用来看
```python
def do_something(handler):
	handler()
```

- super,按照mro继承关系向上找成员
```python
class Base(object):
	def message(self, num):
		print("Base.message", num)

class Foo(Base):
	def message(self, num):
		print("Foo.message",num)
		super().message(num+100)

obj = Foo()
obj.message(1)

>>> Foo.message 1
>>> Base.message 101
```
开始执行Foo这个类的方法
super,就去上游中寻找message方法,如果没有,就去上上级找,直到找到没有就报错
这里就是找到上级Base

这里如果super变为self,那就会一直在Foo中寻找,而不是跳过我这个类找上游的类,这是为了在子类父类重名的时候,明确调用关系使用的

```python
class Base(object):
	def message(self, num):
		print("Base.message", num)
		super().message(1000)

class Bar(object):
	def message(self, num):
		print("Bar.message", num)

class Foo(Base, Bar):
	pass

obj = Foo()
obj.message(1)

>>> Base.message 1
>>> Bar.message 1000
```

super也取决于谁来调用的
因为在这里,obj是Foo的实例化对象
所以这里Base中间传入message的self是obj这个对象
在这里遇到了super,是根据self所在的mro找上面的类
先找Base,再找Bar的关系
但是找到Base的时候,执行了一个super,这时候就会跳过了Base,就去找Bar了
![[Pasted image 20231031232530.png]]

如果改一下
```python
class Base(object):
	def message(self, num):
		print("Base.message", num)
		super().message(1000)

class Bar(object):
	def message(self, num):
		print("Bar.message", num)

class Foo(Base, Bar):
	pass

obj = Base() # 创建Base实例化对象
obj.message(1)

>>> 报错
```
这时候调用super的时候就有问题了,object中找message会找不到就报错

## 应用场景

假设有一个类,原来已经实现了某些功能,但是我们希望再他的基础上扩展
这个时候我们可以使用super
```python
info = dict()
info['name'] = 'wupeiqi'
info['age'] = 19
value = info.get('age')
print(value)
```
```python
cladd MyDict(dict):

	def get(self, k):
		print("自定义功能")
		return super().get(k)

info = MyDict()
info['name'] = 'wupeiqi' # __setitem__方法自动触发 但是这里会调用父类的功能,所以不用写了
info['age'] = 19
print(info)

value = info.get('age') # 这里的get方法因为是我定义了,所以本来会优先使用我的功能,但是还要接着使用原来的功能,所以就可以super一下,就可以获得之前的功能,同时自己的功能也执行了
print(value)
```
我可以自己创建一个类,继承dict
这样我写的就有dict所有的功能
这里的get方法因为是我定义了,所以本来会优先使用我的功能,但是还要接着使用原来的功能,所以就可以super一下,就可以获得之前的功能,同时自己的功能也执行了

![[Pasted image 20231031233421.png]]
再BaseModelForm这个函数中做了一些工作,然后我希望同时执行BaseForm的init,所以就加了一个super函数


- type,获取一个对象的类型
```python
v1 = "æ­¦æ²é½"
result = type(v1)
print(result) # <class 'str'>

v2 = "æ­¦æ²é½"
print( type(v2) == str )  # True

v3 = [11, 22, 33] # list(...)
print( type(v3) == list )  # True

class Foo(object):
    pass

v4 = Foo()

print( type(v4) == Foo )  # True
```
主要是比较类是不是同一个类

在列表中有很多不同类型的数据,这时候可以使用逻辑代码提取出相同type的数据进行处理


- isinstance 判断对象是否是某个类或者某个子类的实例
```python
class Top(object):
    pass


class Base(Top):
    pass


class Foo(Base):
    pass


v1 = Foo()

print( isinstance(v1, Foo) )   # True对象v1是Foo类的实例
print( isinstance(v1, Base) )  # True对象v1是Base的子类的实例
print( isinstance(v1, Top) )   # True对象v1是Top子类的实例
```



```python
class Animal(object):
    def run(self):
        pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

data_list = [
    "alex",
    Dog(),
    Cat(),
	"root"
]

for item in data_list:
    if type(item) == Cat:
        item.run()
    elif type(item) == Dog:
        item.run()
    else:
        pass
    
for item in data_list:
    if isinstance(item, Animal):
        item.run()
    else:
        pass
```
列表中有4个值,判断每个元素,如果是Animal子类的就使用run函数
传统就是一个个比较type是不是的,但是这个比较没有效率
如果使用isinstance就更加简单了
前者是后者的子类,这个是用来检查对象的

- issubclass，判断类是否是某个类的子孙类。
```python
class Top(object):
    pass


class Base(Top):
    pass


class Foo(Base):
    pass


print(issubclass(Foo, Base))  # True
print(issubclass(Foo, Top))   # True
```
前者是后者的子孙类
这个是用来检查类的