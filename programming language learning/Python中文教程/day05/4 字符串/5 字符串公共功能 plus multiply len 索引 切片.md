**3.3 公共功能**
1. 相加 字符串加字符串
2. 相乘 字符串乘以一个整数

```python
v1 = "alex" + "sb"

data = "ss" * 3
```

3. 求长度
```python
data = "sis has man"
value = len(data)
print(value) # 11 包含两个空格

data = "余嘉夕"  
value = len(data)  
print(value) # 3 只有3个字符
```

4. 获取字符串中的字符 基于索引
```python
message = "make some deal"
#          012345678910111213

print(message[0]) # 第一个字符 m
print(message[1]) # 第二个字符 a
print(message[13]) # 第三个字符 l
```
还可以倒着取数字
```python
message = "make some deal"

print(message[-1]) # 第一个字符 l
print(message[-2]) # 第二个字符 a
print(message[-3]) # 第三个字符 e
```
注意事项：字符串中只能通过索引取值，无法修改值
python中不支持索引进行字符串修改，【字符串在内部储存时不允许对内部元素修改，想修改只能重新创建】

```python
message = "make some deal"
index = 0
while index <= len(message): # 如果直接写长度，就是程序写死了，len更灵活
	value = message[index] # 这里的index一旦超出字符串长度就会报错
	print(value)
	index += 1
```
上面是正序一个个字符展示，下面倒序一个个字符展示
```python
message = "make some deal"
index = len(message) - 1
while index >= 0: # 这是从最长的开始减去1，因为第一个字符是0开始
	value = message[index] # 这里就是取message中的index数字对应的字符
	print(value)
	index -= 1
```

5. 切片 获取字符串中的子序列
```python
message = "make some deal"

message[0:2] # 前边第一个0对应的包含，第三个2对应的不包含 结果就是ma
message[3:] # 从第四个3对应的一直到最后 结果 e some deal
message[:5] # 从第六个5对应的一直到最前面的字符，但是5对应的还是不取 结果make s
```
切片也可以加负值
```python
message = "make some deal"

print(message[4:-1]) # 从4对应的字符一直到最后一个字符不包含 结果  some dea
print(message[7:-2]) # 结果me de
```
切片还可以跟len结合
```python
message = "make some deal"
print(message[6:len(message)])# 这个就把len转换为数字看 可以一直到最后 结果是 ome deal
```
注意事项：同样字符串切片只能读取数据，无法修改数据
例如
```python
message[4:8] = "come on" # 就会报错
```
【字符串创建后无法操作，原子操作】

如果要修改
```python
message = "make some deal"

value = message[0:3] + "python" + message[5:]
print(value)
```