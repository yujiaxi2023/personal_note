对于python面向对象的继承
- 继承存在的意义:公共的方法提取到父类中,有利于增加代码重用性
- 继承的编写方式
```python
# 继承
class Base(object):
	pass
class Foo(Base):
	pass
```
```python
# 多继承
class Base(object):
	pass
class Bar(object):
	pass
class Foo(Base,Bar):
	pass
```
- 调用类中的成员的时候 ,遵循:
	- 优先在自己类中找,没有在父类中找
	- 如果多继承,就从左到右

如果遇到的情况是下列的继承关系

![[Pasted image 20231031215739.png]]
实例化A,在A类中没有,会在B中找,B没有,到底是去D还是C
![[Pasted image 20231031215815.png]]
![[Pasted image 20231031215834.png]]

## mro和c3算法

如果类中存在继承关系,可以通过`mro()`获取对当前类的继承关系(找成员的顺序)
![[Pasted image 20231031220208.png]]
```python
class C(object):  
    pass  
  
class B():  
    pass  
  
class A(B,C):  
    pass  
  
print(A.mro()) # [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]  
print(A.__mro__) #[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
```
列表中获得的就是继承关系,也就是找成员的顺序
c3算法有几个推演规范
```python
mro(A) = [A] + [B,C]
mro(A) = [A,B,C]
```
```python
mro(A) = [A] + merge(mro[B],mro[C],[B,C])
mro(B) = [B] + merge(object)
mro(C) = [C] + merge(object)
```
merge当作一个函数,需要接收几个参数,就是从左往右的对象的继承关系,然后和B,C也要传入参数
```python

```
merge函数的计算规则
拿第一个参数的第一个值,和其他的除了第一个值进行比较
看B存不存在这些里面,如果不存在,就提取出来B,然后剔除掉所有的B
![[Pasted image 20231031221506.png]]
比较B是否存在在第二个列表的后两个
![[Pasted image 20231031221541.png]]
剔除掉了所有的B
然后继续拿第一个值,比较,如果存在,就进行跳过
![[Pasted image 20231031221625.png]]
这里就是object存在,进行跳过到下一步
![[Pasted image 20231031221653.png]]
然后用第二个参数的第一个值进行同样的比较,如果不存在,就拿出来
然后就剩object然后拿出来
![[Pasted image 20231031221732.png]]
最后就是
![[Pasted image 20231031221740.png]]



![[Pasted image 20231031220221.png]]
```python
class B:  
    pass  
  
class D:  
    pass  
  
class C(D):  
    pass  
  
class A(B,C):  
    pass  
  
print(A.mro()) # [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>]  
print(A.__mro__) # [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>]
```
无论如何,调用mro就行了

![[Pasted image 20231031220414.png]]
打印mro得到的是先A 再B 再D 再C

![[Pasted image 20231031220459.png]]
先A 再B 再C 再D

![[Pasted image 20231031220519.png]]
A B D G H K C E F M N P这个顺序
就是左边直接挖最深去然后找最近的右边,然后继续挖
无法继续挖就到最浅层回去找右边一个


## 一句话搞定继承关系

**从左到右,深度优先,大小钻石,留住顶端**
遇到钻石型的继承就留住顶端,跳过
![[Pasted image 20231031222826.png]]
这样就是钻石继承,小钻石


![[Pasted image 20231031222917.png]]
这中间加一个也就是大钻石

## py2和py3的区别

py2.2之前继承关系是不留顶端,直接一竿子通到底继承
![[Pasted image 20231031223050.png]]
- 在python2.2之前，只支持经典类【从左到右，深度优先，大小钻石，不留顶端】
    
- 后来，Python想让类默认继承object（其他语言的面向对象基本上也都是默认都继承object），此时发现原来的经典类不能直接集成集成这个功能，有Bug。
    
- 所以，Python决定不再原来的经典类上进行修改了，而是再创建一个新式类来支持这个功能。【从左到右，深度优先，大小钻石，留住顶端。】
    
    - 经典类，不继承object类型
        
    - 新式类，直接或间接继承object
        
- 这样，python2.2之后 中就出现了经典类和新式类共存。（正式支持是2.3）
    
- 最终，python3中丢弃经典类，只保留新式类。
- 
```
原文档 https://www.python.org/dev/peps/pep-0253/#mro-method-resolution-order-the-lookup-rule

In classic Python, the rule is given by the following recursive function, also known as the left-to-right depth-first rule.

def classic_lookup(cls, name):
    if cls.__dict__.has_key(name):
        return cls.__dict__[name]
    for base in cls.__bases__:
        try:
            return classic_lookup(base, name)
        except AttributeError:
            pass
    raise AttributeError, name
    
The problem with this becomes apparent when we consider a "diamond diagram":

      class A:
        ^ ^  def save(self): ...
       /   \
      /     \
     /       \
    /         \
class B     class C:
    ^         ^  def save(self): ...
     \       /
      \     /
       \   /
        \ /
      class D
      

Arrows point from a subtype to its base type(s). This particular diagram means B and C derive from A, and D derives from B and C (and hence also, indirectly, from A).

Assume that C overrides the method save(), which is defined in the base A. (C.save() probably calls A.save() and then saves some of its own state.) B and D don't override save(). When we invoke save() on a D instance, which method is called? According to the classic lookup rule, A.save() is called, ignoring C.save()!

This is not good. It probably breaks C (its state doesn't get saved), defeating the whole purpose of inheriting from C in the first place.

Why was this not a problem in classic Python? Diamond diagrams are rarely found in classic Python class hierarchies. Most class hierarchies use single inheritance, and multiple inheritance is usually confined to mix-in classes. In fact, the problem shown here is probably the reason why multiple inheritance is unpopular in classic Python.

Why will this be a problem in the new system? The 'object' type at the top of the type hierarchy defines a number of methods that can usefully be extended by subtypes, for example __getattr__().

(Aside: in classic Python, the __getattr__() method is not really the implementation for the get-attribute operation; it is a hook that only gets invoked when an attribute cannot be found by normal means. This has often been cited as a shortcoming -- some class designs have a legitimate need for a __getattr__() method that gets called for all attribute references. But then of course this method has to be able to invoke the default implementation directly. The most natural way is to make the default implementation available as object.__getattr__(self, name).)

Thus, a classic class hierarchy like this:

class B     class C:
    ^         ^  def __getattr__(self, name): ...
     \       /
      \     /
       \   /
        \ /
      class D
      

will change into a diamond diagram under the new system:

      object:
        ^ ^  __getattr__()
       /   \
      /     \
     /       \
    /         \
class B     class C:
    ^         ^  def __getattr__(self, name): ...
     \       /
      \     /
       \   /
        \ /
      class D


and while in the original diagram C.__getattr__() is invoked, under the new system with the classic lookup rule, object.__getattr__() would be invoked!

Fortunately, there's a lookup rule that's better. It's a bit difficult to explain, but it does the right thing in the diamond diagram, and it is the same as the classic lookup rule when there are no diamonds in the inheritance graph (when it is a tree).
```

总结：Python2和Python3在关于面向对象的区别。

- Py2：
    
    - 经典类，未继承object类型。【从左到右，深度优先，大小钻石，不留顶端】
        
    - 新式类，直接获取间接继承object类型。【从左到右，深度优先，大小钻石，留住顶端 -- C3算法】
        
- Py3
    
    - 新式类，丢弃了经典类只保留了新式类。【从左到右，深度优先，大小钻石，留住顶端 -- C3算法】
        