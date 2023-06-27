python中为所有的列表类型的数据提供了一批独有的功能
在开始学习列表的独有功能之前，先做一个字符串和列表的对比：
- 字符串，不可以变化，创建之后无法修改，【其独有功能是创建一个新的数据】
```python
name = "alex"
data = name.upper()
print(name)
print(data)
```
- 列表，可变，创建后可以修改内部元素【独有功能基本都是直接操作列表内部，不会创建一份新的数据】
```python
user_list = ["car","girl"]
user_list.append("sister")

print(user_list) # "car" "girl" "sister"
```

列表中的常见独有功能如下：
**1. 追加，在原列表尾部追加值**
```python
data_list = []

v1 = input("please input your name")
data_list.append(v1)

v1 = input("please input your name")
data_list.append(v1)

print(data_list) # ["alex","eric"]
```

```python
# example 1
user_list = []

while True:
	user = input("please input your name(Q out):")
	if user == "Q":
		break
	user_list.append(user)

print(user_list)
```

```python
# example 2
welcome = "welcome user NB game".center(30, '*')
print(welcome)

user_count = 0
while True:
	count = input("please input game people")
	if count.isdecimal():
		user_count = int(count)
		break
	else:
		print("input form wrong, please input number")
# 死循环 让用户输入人数数量必须是数字

message = f."{user_count}attend this game"
print(message)

user_name_list = []
for i in range(1, user_count + 1):
# 这里从1开始因为默认是从0开始，所以需要先定义，range是前取后不取所以需要最后+1
	tips = f."please input player names ({i}/{user.count})"
	name = input(tips)
	user_name_list.append(name)

print(user_name_list)
```

**2. 批量追加 将一个列表中的元素逐一添加另外一个列表**
```python
tools = ["banzhuan", "cadao", "langtou"]

tools.extend( [11,22,33] ) # 列表中的值逐一添加到tools中
print(tools) # ["banzhuan", "caidao", "langtou", 11, 22, 33]
```
```python
tools = ["banzhuan", "cadao", "langtou"]
weapon = [11,22,33]
tools.extend(weapon) 
print(tools) # ["banzhuan", "caidao", "langtou", 11, 22, 33]
# extend 中什么在前什么在后得到的东西是不同的
```
```python
# 等价于
tools = ["banzhuan", "caidao", "langtou"]
weapon = ["ak47", "m4"]
for item in weapon:
	tools.append(item)
print(tools)
```

