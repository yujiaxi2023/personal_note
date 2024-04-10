**8. 列表元素排序**
```python
# 数字排序
num_list = [11, 22, 4, 5, 11, 99, 88]
print(num_list)

num_list.sort() # 让列表从小到大排序

print(num_list)

num_list.sort(reverse=True) # 让列表从大到小排序
num_list.sort(key=) # 使用函数排序
```
sort如果是两个一样的元素，则顺序不变
reverse 的情况下两个一样的元素 将颠倒顺序

```python
user_list = ['wangbaoqiang', 'adchenyufan', 'alex', 'jianailiang', 'jianai', '1']
print(user_list)
"""
sort 排序的原理
如果输入的字符串，首先每个字符会转换为Unicode utf-16的码点
['x x x', 'x x x x x']
从第一个字符的数字开始比较，如果一样就比较第二个字符的数字，依此类推之后，如果后边一个字符串更长，代表更短的字符串是更小
"""

user_list.sort()
print(user_list)
```
通过字符串获得Unicode的表述
```python
data = 'wang'

data_list = []

for char in data:
	v1 = ord(char)
	data_list.append(v1)
print(data)
print(data_list)

print(hex(v1)) # 输出的是十进制的表示，需要转换为十六进制
```

注意事项：如果列表中是混合的整型和字符串无法比较大小，会出现报错
但是布尔值可以和整型可以比较

**9. 反转原列表**
```python
user_list = ['wangbaoqiang', 'adchenyufan', 'alex', 'jianailiang', 'jianai', '1']
user_list.reverse()
print(user_list)
```

列表的其他功能可以ctrl 点击pycharm中的list就可以得到独有功能