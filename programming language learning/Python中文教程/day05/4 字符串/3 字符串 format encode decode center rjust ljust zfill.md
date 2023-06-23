**10. 格式化字符串，得到新的字符串**
```python
name = "{0}的喜欢干很多行业，例如有：{1}，{2}等"
data = name.format("laowang","nurse","model")
print(data) # laowang的喜欢干很多行业，例如有：nurse，model等
print(name) # {0}的喜欢干很多行业，例如有：{1}，{2}等
```
```python
name = "{} likes many industries, for example:{},{},etc."
data = name.format("laowang","nurse","model")
print(data) # "laowang likes many industries, for example:nurse,model,etc."
```
```python
name = "{name} likes many works, like: {h1},{h2},etc."
data = name.format(*name="laowang",h1="nurse",h2="model")
print(data) # laowang likes many works, like: nurse,model,etc.
```
```python
h0 = "laowang"
h1 = "nurse"
h2 = "model"
name = f"{h0} likes many works, e.g. {h1},{h2},etc."
print(name)
```

**11. 字符串转换为字节类型**
```python
data = "sister" # unicode 进行存储的 需要转换为utf-8的格式
v1 = data.encode("utf-8") # utf-8 字节类型
v2 = data.encode("ascii") # ASCII 字节类型
```
```python
data = "嫂子"  # unicode 进行存储的 需要转换为utf-8的格式  
v1 = data.encode("utf-8")  # utf-8 字节类型  
v2 = data.encode("gbk")  # gbk 字节类型  
  
print(v1)  # b'\xe5\xab\x82\xe5\xad\x90' 前三个字节是代表嫂字 后三个字节代表子字 x代表16进制  
print(v2)  # b'\xc9\xa9\xd7\xd3' 前两个字节代表嫂字 后两个字节代表子字
```
```python
s1 = v1.decode("utf-8") # 嫂子
s2 = v2.decode("gbk") # 嫂子
print(s1)
print(s2)
```

**12.字符串内容居中，居左，居右展示**
```python
v1 = "王老汉"

data = v1.center(20,"*")
print(data) # ********王老汉*********
```
```python
v1 = "王老汉"  
data = v1.rjust(21, "_")  
print(data)  # __________________王老汉
```
```python
v1 = "王老汉"  
data = v1.ljust(21, "_")  
print(data) # 王老汉__________________
```

**13. zfill帮助你填充0的**
```python
data = "alex"  
v1 = data.zfill(10)  
print(v1) # 000000alex
```
应用场景，处理二进制数据
```python
data = "101" # "00000101"
v1 = data.zfill(8)
print(v1) # 00000101 可以让你data凑够一个字节
```

这些只是字符串的功能的一部分，想要查找其他的字符串独有功能，可以在pycharm 中打str，然后摁住ctrl键点击str，就会跳转到python源码中，就可以看到def之后的各种分类
![[Pasted image 20230428155533.png]]
![[Pasted image 20230428155827.png]]
就可以定位到任意一个独有功能中去