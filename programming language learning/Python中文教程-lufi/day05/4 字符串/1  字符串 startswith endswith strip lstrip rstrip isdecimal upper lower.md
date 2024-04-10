字符串，平时会用他表示文本信息，例如 姓名 地址 自我介绍等
**3.1 定义**
```python
v1 = "包治百病"
v2 = 'baozhibaibing'
v3 = "bao'zhibaibing"
v4 = 'bao"zhibaibing'
v5 = """
doushiwodecuo
yinweidabuguo
"""
# 三个引号，可以支持多行/换行表示一个字符串，其他的都只能在一行中表示一个字符串
```

**3.2 独有功能(18/48)**
```python
"xxxx".功能()
"xxxx".功能(...)

v1 = "xxxx"
v1.功能(...)
```
总共有48个独有功能

1.判断字符串是否以XX开头？得到一个布尔值
```python
v1 = "say that again"
# True
result = v1.startswith("say")

print(result) # 值为True
```
```python
v1 = input("please input:")

if v1.startswith("beijing"):
	print("beijing population")
else:
	print("all population")
```

2.判断字符串是否以XX结尾？得到一个布尔值
```python
v1 = "say that again"
# True
result = v1.endswith("again")

print(result) # 值为True
```
```python
v1 = input("please input:")

if v1.endswith("village"):
	print("agricultural population")
else:
	print("not agricultural population")
```

3.判断字符串是否是一个整数？得到一个布尔值
```python
v1 = "12354312"

result = v1.isdecimal()

print(result) # True
```
```python
# example

v1 = input("please input:") # 666
v2 = input("please input:") # 888
if v1.isdecimal() and v2.isdecimal():
	data = int(v1) + int(v2)
	print(data)
else:
	print("please input right number!")
```
```python
# mistake

v1 = "1234"  
  
print(v1.isdecimal())  # True  
  
v2 = "①"  
  
print(v2.isdecimal())  # False  
  
v3 = "1234"  
  
print(v1.isdigit())  # True  
  
v4 = "①"  
  
print(v2.isdigit())  # True

# isdigit 会把字符①也认作True
```

4.去除字符串 两边的空格，换行符，制表符，得到一个新的字符串
```python
data = input("please input:") # wupeiqi wupeiqi   后边的有空格
print(data)
```
```python
msg = "He ll o ,tree,bro ther"
data = msg.strip()
print(data) # 将msg两边的空白去掉
```
```python
msg = "He ll o ,tree,bro ther"
data = msg.lstrip()
print(data) # 将msg左边的空白去掉
```
```python
msg = "He ll o ,tree,bro ther"
data = msg.rstrip()
print(data) # 将msg右边的空白去掉
```
补充：去除空格，换行符，制表符
```
换行符 \n ，每次回车的时候中间就会增加一个换行符、\n
制表符 就是tab键，实际上内置了一个\t的内容
```
```python
# example
code = input("please input 4 identify number:")
data = code.strip()
if data == "FB87":
	print('code correct')
else:
	print("code wrong")
```
补充：去除字符串两边指定的内容
```python
msg = "broHe ll o ,tree,bro ther"
data = msg.strip("bro")

print(data) # 将msg两边的字符 去掉
```
```python
msg = "broHe ll o ,tree,bro ther"
data = msg.lstrip("bro")

print(data) # 将msg左边的字符 去掉
```
```python
msg = "broHe ll o ,tree,bro ther"
data = msg.rstrip("bro")

print(data) # 将msg右边的字符 去掉
```

**5. 字符串变大写，得到一个新字符串**
```python
msg = "my name is oliver queen"
data = msg.upper()
print(msg) # my name is oliver queen
pring(data)  # MY NAME IS OLIVER QUEEN
```
```python
# example
code = input("input 4 code:") # FB88 fb88
value = code.upper() # FB88
data = value.strip() #FB88
if data == "FB88":
	print('code correct')
else:
	print("code wrong")

# tips
"""
code的值"fb88 "
value的值"FB88 "
data的值"FB88"
```

**6. 字符串变小写，得到一个新字符串**
```python
msg = "my name is oliver queen"
data = msg.lower()
print(msg) # my name is oliver queen
pring(data)  # MY NAME IS OLIVER QUEEN
```
```python
# example
code = input("input 4 code:") # FB88 fb88
value = code.lower() # FB88
data = value.strip() #FB88
if data == "FB88":
	print('code correct')
else:
	pring("code wrong")

# tips
"""
code的值"fb88 "
value的值"FB88 "
data的值"FB88"
```

