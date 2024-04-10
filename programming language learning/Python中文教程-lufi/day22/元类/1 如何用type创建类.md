## 元类

- 用模块，框架实现业务功能，没必要学习元类
- 元类 + 案例

在python中基于类可以创建对象
```python
class Foo(object):
	def __init__(self, name):
		self.name = name
	def __new__(cls,*args,**kwargs):
		data = object.__new__(cls)
		return data

# 根据类创建对象
obj = Foo("吴佩琦")
```

创建对象的时候分两步：
1. 执行类的new方法，用来创建对象（空的，啥也没有）【构造方法】{}
2. 执行类的init方法，初始化对象 【初始化方法】

对象是基于类创建出来的

问题：类是谁创建的？
**类默认是type创建的**
```python
# 传统方式创建类
class Foo(object):
	v1 = 123
	def func(self):
		return 666


# 非传统方式创建类
# - 类名 - 继承关系 - 成员
fa = type("Foo", (object), {"v1":123, "func":lambda self:666})
# 根据类创建对象
obj = fa()
# 调用对象中的v1变量（是类变量不是实例变量）
print(obj.v1)
# 执行对象的func方法
result = obj.func()
print(result)
```
两种方式都可以实现创建类
但是上边这种很直观，下面的很抽象
