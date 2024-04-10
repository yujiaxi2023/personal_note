**3. 插入 在原列表指定索引位置插入值**
```python
user_list = ["aoisora","migami","arina"]
#                0         1       2
user_list.insert(0,"marong")

user_list.insert(2,"lixiaolu")
print(user_list)
# "marong", "aoisora", "lixiaolu", "migami", "arina"
```
```python
# example
name_list = []
while True:
	name = input("please input buyer name(Q/q exit):")
	if name.upper() == "Q":
		break
	if name.startwith("diao"):
		name_list.insert(0, name)
	else:
		name_list.append(name)
print(name_list)
```
如果写入的索引有问题，也就是不存在
如果索引小于0，就会自动添加到最前面
如果所以更长，自动添加到最后

**4. 在原列表中根据值删除（从左到右第一个删除）【慎用，如果没有报错】**
```python
user_list = ["wangbaoqiang", "chenyufan", "alex", "jianailiang", "alex"]

while True:
	if "alex" in user_list:
		user_list.remove("alex")
	else:
		break
print(user_list)
# 这样可以保证将所有的值都删除，而且不会报错
```
```python
# 自动抽奖程序案例
import random  
  
data_list = ["iphone12", "girlfriend", "masaji", "travel to thailand", "condom"]  
  
while data_list:  
    name = input("auto lottery game, please input your name:")  
    # 随机从data_list中抽取一个值出来  
    value = random.choice(data_list)  
    print(f"congratulation{name}, you win the{value}")  
    data_list.remove(value)
```

**5. 在原列表中根据索引剔除某个元素**
```python
user_list = ["wangbaoqiang", "chenyufan", "alex", "jianailiang", "alex"]

user_list.pop(1)
print(user_list) # "wangbaoqiang", "alex", "jianailiang", "alex"

user_list.pop()
print(user_list) # "wangbaoqiang", "alex", "jianailiang"

item = user_list.pop(1)
print(item) # "alex"
print(user_list) # "wangbaoqiang", "jianailiang"

ele = user_list.pop() # 在user_list中删除最后一个，并且赋值给ele
item = user_list.pop(2) # 在user_list中删除索引为2的值，并且将删除值赋值给itme
```
```python
# 排队买火车票
user_queue = []

while True:
	name = input("peking-shanghai train tickets, please input buyers name and wait(Q exit):")
	if name == "Q":
		break
	user_queue.append(name)

ticket_cout = 3
for i in range(ticket_count):
	username = user_queue.pop(0)
	message = f"congratulation{username}, buy tickets successfully."
	print(message)

user_queue = ["wupeiqi","laoyao","gandan"]
faild_user = ",".join(user_queue)
faild_message = "sorry, tickets have been sold out, please choose another way, name list:{faild_user}."
print(faild_message)
```

**6. 清空原列表**
```python
user_list = ["wangbaoqiang"]
user_list.clear()
print(user_list) # []
```

**7. 根据值获取索引（从左到右找到第一个）【慎用，找不到报错】**
```python
user_list = ["wangbaoqiang", "chenyufan", "alex", "jainailiang", "alex"]

if "alex" in user_list:
	index = user_list.index("alex")
	print(index)
else:
	print("no exist")
```