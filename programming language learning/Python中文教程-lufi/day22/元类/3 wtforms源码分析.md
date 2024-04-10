```python
from wtforms import Form  
from wtforms.fields import simple  
  
class FormMeta(type):  
    def __init__(cls, name, bases, attrs):  
        type.__init__(cls, name, bases, attrs)  
        cls._unbound_fields = None  
        cls._wtforms_meta = None  
  
    def __call__(cls, *args, **kwargs):  
        if cls._unbound_fields is None:  
            fields = []  
            for name in dir(cls):  
                if not name.startswith("_"):  
                    unbound_field = getattr(cls, name)  
                    if hasattr(unbound_field, "_formfield"):  
                        fields.append((name, unbound_field))  
            # We keep the name as the second element of the sort  
            # to ensure a stable sort.            fields.sort(key=lambda x: (x[1].creation_counter, x[0]))  
            cls._unbound_fields = fields  
  
        # Create a subclass of the 'class Meta' using all the ancestors.  
        if cls._wtforms_meta is None:  
            bases = []  
            for mro_class in cls.__mro__:  
                if "Meta" in mro_class.__dict__:  
                    bases.append(mro_class.Meta)  
            cls._wtforms_meta = type("Meta", tuple(bases), {})  
        return type.__call__(cls, *args, **kwargs)  
  
def with_metaclass(meta, base=object):  
    # FormMeta("NewBase", (BaseForm,), {}) FormMeta是继承type的类，所以这里创建的一个NewBase的类，然后继承了BaseForm的类，成员为空  
    # type("NewBase", (BaseForm,), {}) 所以上边的意思基于FormMeta创建类  
    return meta("NewBase", (base,), {})  
"""  
class NewBase(BaseForm, metaclass=FormMeta):  
    pass  
class Newbase():  
"""  
# 基于FormMeta创建  
class Form(BaseForm, metaclass=FormMeta):  
    pass  
# 基于FormMeta创建  
class LoginForm(Form):  
    name = simple.StringField(label="用户名", render_kw={'class': 'form-control'})  
    pwd = simple.PasswordField(label="密码", render_kw={'class': 'form-control'})  
  
  
# 直观感受是创建了一个类变量，然后调用的是里面的类变量  
form = LoginForm()  
print(form.name)  
print(form.pwd)  
# 但是我们可以看到继承了一个Form类  
# 问题1： 此时LoginForm是由type or FormMeta创建？  
"""  
类中是metaclass，自己的类是metaclass定义的类创建的  
当继承某个类，如果这个父类由metaclass定义的，那就也是这个创建的  
"""  
# 1. 创建类的时候会执行FormMeta的new和init，在类的内部添加了两个类变量 _unbound_fields 和 _wtforms_meta# 2. 创建类之后创建对象，会执行FormMeta中间的call方法，然后就看这个call方法  
# 3. 这个call方法里面又调用了父类type里面的call方法创建new和init  
# 4. 这里面所有哦基于FormMeta创建的方法，都会调用这里的call方法，所以我们可以在这个call里面进行编辑让所有的基于元类创建的类都使用这个call方法
```

学习了元类之后，在：
- 类创建，自定义功能
- 对象创建前后，定义功能

在自定义的MyType类中，继承type类，可以在init和new和call上面进行拓展
```python
class MyType(type):  
  
    # 创建一个类也是先执行new再执行init  
    def __init__(self, *args, **kwargs): 
	    # 这里可以扩展 
        print("init")  
        super().__init__(*args, **kwargs)  
  
    def __new__(cls, *args, **kwargs):  
        # 创建类  
        # 这里也可以扩展
        print("new")  
        new_cls = super().__new__(cls, *args, **kwargs)  
        print(new_cls)  
        return new_cls  
  
    def __call__(self, *args, **kwargs):  
	    # 这里更加可以扩展
        # 调用自己类的new方法 创建对象  
        empty_object = self.__new__(self)  
        # 调用自己类init进行初始化  
        self.__init__(empty_object, *args, **kwargs)  
  
        return empty_object  
  
# 假设Foo是一个对象，由MyType创建  
# Foo类是MyType的一个对象  
# Foo() -> MyType对象()  
class Foo(object, metaclass=MyType):  
    def __init__(self, name):  
        self.name = name  
  
v1 = Foo("alex")  
print(v1)  
print(v1.name)
```
这些都是批量进行扩展的