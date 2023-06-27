**6.步长 跳着取字符串的内容**
```python
name = "life is not liking a movie, it even worse."

print( name[ 0:5:2 ] ) # 输出 lf 【有空格】
print( name[ :8:2 ] ) # 输出 lf s
print( name[ 2::3 ] ) # 输出 fin kg v,tv r.
print( name[ ::2 ] ) # 输出 lf sntlkn  oi,i vnwre
print( name[ 8:1:-1 ] ) # 输出 n si ef
```
步长的前面两个取值代表范围，最后一个值代表步长
如果不写就是1作为步长
要注意前取后不取，不管是正着步长还是倒着步长

将字符串反转
```python
name = "life is not liking a movie, it even worse."
value = name[ -1::-1]
print(value) # 生成新的字符串 反转的字符串
```

**7.循环**
- while 循环
```python
message = "make a deal"
index = 0 
while index < len(message):
	value = message[index]
	print(value)
	index += 1
```
- for循环
```python
message = "make a deal"
# 循环字符串中每一个字符
for char in message:
	print(char)
# for in 是固定语法 后面填写字符串 char获取每循环一次的字符
# 例如第一次循环的时候获得m，char就是m，第二次循环变为a
```
for循环比while构造一个索引然后判断布尔值来的简单

- range 帮助我们创建一系列的数字
```python
range(10) # [0,1,2,3,4,5,6,7,8,9]
range(1,10) # [1,2,3,4,5,6,7,8,9]
range(1,10,2) # [1,3,5,7,9]
range(10,1,-2) # [10,8,6,4,2]
```
创造的数据形式是列表

- for + range
```python
for i in range(10):
	print(i) #0123456789
```

```python
message = "make a deal"
for i in range(5):
	print(message[i]) # 拿出message里面的值
```
我们可以再把代码写灵活一点
```python
message = "make a deal"
for i in range(len(message))
	print(message[i])
# 这样可以直接把所有的字符输出
```

char的方式是直接循环字符串里面的元素
利用range的方式就是利用索引的方式打印字符串

for循环更简单一点

**应用场景**
- while循环，一般做无限制（未知）循环的时候使用，不知道达到什么条件结束
```python
while True:
	···
```
```python
# 用户输入一个值，必须是整数，不是整数就一直输入，一直到输入整数，此时不知道几次结束循环
num = 0 
while True:
	input("please input:")
	if data.isdecimal():
		num = int(data)
		break
	else:
		print("wrong please input again:")
```

- for循环，一般用作已知的循环数量的场景
```python
message = "make a deal"
# 循环字符串中每一个字符
for char in message:
	print(char)
```
```python
message = "make a deal"
for i in range(len(message))
	print(message[i])
# 这样可以直接把所有的字符输出
```
这些都是已知的循环数量

- break 和 continue 关键字
```python
message = "make some deal"
for char in message:
	if char == "s":
		continue
	print(char)
# 输出结果 跳过了s
m
a
k
e

o
m
e

d
e
a
l
```
```python
message = "make some deal"
for char in message:
	if char == "s":
		break
	print(char)
# 输出结果 s之后就不会输出
m
a
k
e


```
```python
for i in range(5):
	print(i)
	for j in range(3):
		print(j)

# 结果是循环5次012 前面都会跟上01234
0
0
1
2
1
0
1
2
2
0
1
2
3
0
1
2
4
0
1
2
```