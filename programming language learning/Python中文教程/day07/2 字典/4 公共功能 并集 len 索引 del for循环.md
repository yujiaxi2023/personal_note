1. 求并集(python3.9新加入)
```python
v1 = {"k1":1, "k2":2}
v2 = {"k2":22, "k3":33}

v3 = v1 | v2
print(v3) # {'k1':1, 'k2':22, 'k3':33}
```
利用一个管道符,将v1和v2的所有键值对集中一起,如果有相同的键,就用后边的替换掉前边的值
和update不同之处在于这个是重新生成的字典

2. 长度
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
data = len(info)
print(data) # 3
```
判断字典中有多少对键值对

3. 是否包含
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
v1 = "age" in info
print(v1)

v2 = "age" in info.keys()
print(v2)

if "age" in info:
	pass
else:
	pass
```
直接写某一个元素是否在内,是默认判断键是否在字典中,等价于下面的代码
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
v1 = "wupeiqi" in info.values()
print(v1)
```
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
v1 = ("age", 12) in info.items()
print(v1)
```
info.items获取到的是一个列表中的元素,所以可以命名一个元组看是否在这个高仿的列表中

4. 索引(键)
字典不同于元组和列表,字典的索引是键,而列表和元组则是0,1,2的数值
```python
info = {"age":12, "status":True, "name":"wupeiqi"}

print(info['age']) # 12
print(info['status']) # True
print(info['name']) # wupeiqi
print(info['xxxx']) # 如果键不存在回报错

value = info.get("xxxxx") # None
print(value)
```
这种索引方法,如果搜索的键不存在则会报错,所以建议使用get根据键获取值

5. 根据键修改值和添加值和删除键值对
上述示例通过键可以找到字典中的值,通过键也可以对字典进行添加和更新操作
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
info['gender'] = 'boy' # gender key not exist add a new key value
print(info) # {'age':12, "status":True, 'name':"wupeiqi", "gender":"boy"}
```
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
info["age"] = 18 # age在info字典中已经存在,就更新对应的值
print(info) # {"age":18, "status":True, "name":"wupeiqi"}
```
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
del info['age'] # 删除info字典中键为age的键值对(键不存在就报错)
print(info) # {"status":True, "name":"wupeiqi"}
```
setdefault跟这个的区别在于这个是会修改掉之前存在的这个值,setdefault如果原来的键值对中存在,就不会修改原来的值
使用pop功能进行删除也是一样的需要注意不能写不存在的值
删除功能如果避免报错就需要增加if的判断功能
```python
info = {"age":12, "status":True, "name":"wupeiqi"}

if "ages" in info:
	del info['age'] # 删除info字典中键为age的键值对(键不存在就报错)
	print(info) # {"status":True, "name":"wupeiqi"}
else:
	print("no exist")
```

6. for循环
由于字典也是容器,内部也可以包含多个键值对,可以通过循环对其中的:键,值,键值进行循环
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
for item in info.keys():
	print(item)
```
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
for item in info.values():
	print(item)
```
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
for key,value in info.items():
	print(key, value)
```

默认情况下是输出所有的键
```python
info = {"age":12, "status":True, "name":"wupeiqi"}
for item in info():
	print(item)
```
这段代码就是输出的所有的键,跟第一个keys的代码是一个结果

