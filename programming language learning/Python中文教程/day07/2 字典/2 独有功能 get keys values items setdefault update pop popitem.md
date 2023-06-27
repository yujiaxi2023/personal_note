1. 获取值
```python
info = {
	"age":12,
	"status":True,
	"name":"wu"
}

data1 = info.get("name")
print(data1) # 输出“wu”

data2 = info.get("age")
print(data2) # 输出12

data = info.get("email")
if data == None:
	print("键不存在")
else:
	print(data) # 输出 None

if data:
	print(data)
else:
	print("键不存在")

# 字典的键中是否存在“email”
if "email" in info:
	data = info.get("email")
	print(data)
else:
	print("no exist")


data = info.get("hobby", 123)
print(data) # 输出 123
```
如果键存在就获取对应的值，如果不存在就默认返回none
如果键不存在后边添加一个值，这样打印出来的就是对应的值

```python
# example
user_list = {
	"wu":"123",
	"alex":"uk87"
}

username = input("input your user name:")
password = input("input your password:")
# None user dont exist
# password compare password

pwd = user_list.get(username)

if pwd == None:
	print("user dont exist")
else:
	if password == pwd:
		print("success")
	else:
		print("false")
```
```python
# example
user_list = {
	"wu":"123",
	"alex":"uk87"
}

username = input("input your user name:")
password = input("input your password:")
# None user dont exist
# password compare password

pwd = user_list.get(username)

if pwd:
	if password == pwd:
		print("success")
	else:
		print("false")
else:
	print("user not exist")
```
```python
# example
user_list = {
	"wu":"123",
	"alex":"uk87"
}

username = input("input your user name:")
password = input("input your password:")
# None user dont exist
# password compare password

pwd = user_list.get(username)

if not pwd:
	print("user not exist")

else:
	if password == pwd:
		print("success")
	else:
		print("false")
```

写代码的时候注意，首先进行简单的逻辑处理，然后把复杂的逻辑放后边

2. 获取所有的键
```python
info = {"age":12, "status":True, "name":"wupeiqi", "email":"xx@live.com"}
data = info.keys()
print(data) # 输出 dict_keys(['age','status','name','email'])

result = list(data)
print(result) # ['age','status','name','email']
```
注意：在python2 的字典.keys()直接获取到的是列表，但是python3中获得的是一个类似列表的东西，这个包含一定的列表的能力， 例如循环表示里面的元素，或者if else 做判断
```python
# loop
info = {"age":12, "status":True, "name":"wupeiqi", "email":"xx@live.com"}
for ele in info.keys():
	print(ele)
```
```python
info = {"age":12, "status":True, "name":"wupeiqi", "email":"xx@live.com"}
info.keys() # dict_keys(['age','status','name','email'])
if "age" in info.keys():
	print("age is dict keys")
else:
	print("age not")
```

3. 所有的值
```python
info = {"age":12, "status":True, "name":"wupeiqi", "email":"xx@live.com"}
data = info.values()

print(data) # 输出 dict_values([12, True, 'wupeiqi', 'xx@live.com'])
```
同样在python2中.values()是直接获得列表，python3中获得的是高仿的列表
```python
info = {"age":12, "status":True, "name":"wupeiqi", "email":"xx@live.com"}
for val in info.values():
	print(val)
```
```python
info = {"age":12, "status":True, "name":"wupeiqi", "email":"xx@live.com"}
info.values() # dict_values([12, True, 'wupeiqi', 'xx@live.com'])
if 12 in info.values():
	print("12 is dict values")
else:
	print("12 not")
```

4. 所有的键值
```python
info = {"age":12, "status":True, "name":"wupeiqi", "email":"xx@live.com"}
data = info.items()

print(data) # 输出 dict_items([ ('age', 12), ('status', True), ('name', 'wupeiqi'), ('email', 'xx@live.com') ])
```
```python
for item in info.items():
	print(item) # item 是一个元组(键， 值)
	print(item[0], item[1]) # 每次循环都按照index取出值
```
```python
for key,value in info.items():
	print(key,value) 
	# key 代表键， value代表值，可以直接将键值从元组中拆分，这个就是前边的值对应前边一个变量，后边值对应后边一个变量
```
```python
info = {"age":12, "status":True, "name":"wupeiqi", "email":"xx@live.com"}
data = info.items()

if ('age', 12) in data:
	print("在")
else:
	print("不在")
```
这个高仿列表可以节省一部分的内存

5. 设置值
```python
data = {
	"name":"wupeiqi",
	"email":"xxx@live.com"
}
data.setdefault("age", 18)
print(data) # {'name':'wupeiqi', 'email':'xxx@live.com', 'age':18}

data.setdefault("name", "alex")
print(data) # {'name':'wupeiqi', 'email':'xxx@live.com', 'age':18}
```
如果添加的是原字典没有的就在后边加上，如果是原字典有的或者没有添加值就什么都不更新

6. 批量更新字典的键值对
```python
info = {"age":12, "status":True}

info.updata( {"age":14, "name":"wupeiq"} ) # info 中没有的键直接添加，有的键直接更新值
print(info) # 输出 {"age":14, "status":True, "name":"wupeiqi"}
```

7. 移除键值对
```python
info = {"age":12, "status":True, "name":"wupeiqi"}

data = info.pop("age")
print(info) # {"age":12, "name":"wupeiqi"}
print(data) # 12
```
将字典中按照输入的键移除这一组键值对，然后将这个值赋予到这个新的变量或者储存空间中

8. 按照顺序移除（先进后出）
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
data = info.popitem()

print(info) # {"age":12, "status":True}
print(data) # ("name", "wupeiqi")
```
会移除掉最后一个值，然后将移除的键值对变为一个元组储存赋值data
python3.6之后因为字典有序，所以 .popitem是移除最后一个值
python3.6之前是随机移除键值对

