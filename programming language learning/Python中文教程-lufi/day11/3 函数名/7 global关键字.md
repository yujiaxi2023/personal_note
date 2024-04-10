## global关键字

![[Pasted image 20231019130319.png]]

默认情况下，局部作用域对全局变量只能进行：读取和修改内部元素（可变类型），无法对全局变量进行重新赋值

- 读取
```python
# READ  
COUNTRY = "CHINA"  
CITY_LIST = ["BEIJING","SHANGHAI","SHENZHEN"]  
  
def download():  
    url = "https://www.xx.com"  
    print(COUNTRY)  
    print(CITY_LIST)  
  
download()
```

- 修改内部元素（可变类型）
```python
# CHANGE ELEMENT  
  
COUNTRY = "CHINA"  
CITY_LIST = ["BEIJING","SHANGHAI","SHENZHEN"]  
  
def download():  
    url = "https://www.xx.com"  
    print(CITY_LIST)  
  
    CITY_LIST.append("GUANGZHOU")  
    CITY_LIST[0] = "NANJING"  
    print(CITY_LIST)  
  
download()
```

- 无法对全局变量重新赋值
```python
# CAN NOT RE DEFINE  
  
COUNTRY = "CHINA"  
CITY_LIST = ["BEIJING", "SHANGHAI", "SHENZHEN"]  
  
  
def download():  
    url = "https://www.xx.com"  
    # 不是对全部变量赋值，而是在局部作用域中又创建了一个局部变量CITY_LIST  
    CITY_LIST = ["HENAN", "HEBEI", "SHANXI"]  
    print(CITY_LIST)  
  
def upload():  
    file_name = "rose.zip"  
    print(COUNTRY)  
    print(CITY_LIST)  
  
download()  
upload()
```


如果想要在局部作用域中对全局变量进行重新赋值，可以基于 global 关键字实现，例如

```python
# global keyword  
COUNTRY = "CHINA"  
CITY_LIST = ["BEIJING", "SHANGHAI", "SHENZHEN"]  
  
def download():  
    url = "https://www.xx.com"  
    global CITY_LIST  
    CITY_LIST = ["HENAN", "HEBEI", "SHANXI"]  
    print(CITY_LIST)  
      
    global COUNTRY  
    COUNTRY = "PCR"  
  
def upload():  
    file_name = "rose.zip"  
    print(COUNTRY) # 这时候已经变成修改之后的变量了  
    print(CITY_LIST)  
  
download()  
upload()
```
