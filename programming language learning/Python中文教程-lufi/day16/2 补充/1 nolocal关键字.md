之前的课程中有global关键字

```python
name = "root"  
  
def outer():  
    name = "wupeiqi"  
  
    def inner():  
        global name  
        name = 123  
        # root 改成 123  
    inner()  
    print(name)  
  
outer()  
print(name) # 这里是全局变量，并且改成了123  
  
  
# nolocal关键字用的比较少  
  
name = 'root'  
  
def outer():  
    name = "wupeiqi"  
  
    def inner():  
        nonlocal name # 将修改上级作用域的变量name = wupeiqi  
        name = 123  
  
    inner()  
    print(name) # 123  
  
outer()  
print(name) # root  
  
  
# nonlocal只是针对上级作用域，不会更改更上层的内容  
  
name = 'root'  
  
def outer():  
    name = "alex"  
  
    def func():  
        name = "wupeiqi"  
  
        def inner():  
            nonlocal name  
            name = 123  
  
        inner()  
        print(name) # 123  
  
    func()  
    print(name) # alex  
  
outer()  
print(name) # root  
  
  
# nonlocal还可以加多个，一层层反上去  
  
name = 'root'  
  
def outer():  
    name = "alex"  
  
    def func():  
        nonlocal name # 指向alex内存地址，转换为wupeiqi  
        name = "wupeiqi"  
  
        def inner():  
            nonlocal name # 指向上一级的wupeiqi内存地址，同时也是alex的内存地址  
            name = 123  
  
        inner()  
        print(name) # 123  
  
    func()  
    print(name) # 123  
  
outer()  
print(name) # root
```

