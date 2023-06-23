**1. 添加元素**
```python
data = {"liu", "guan", "wang"}
data.add("zheng")
print(data)
```
```python
data = set()
data.add("zhou")
data.add("lin")
print(data)
```

**2. 删除元素**
```python
data = {"liu", "guan", "wang", "zhang", "li"}
data.discard("guan")
print(data)
```
删除因为集合中是非重复类的元素,所以删除不用在意顺序

**3. 交集**
```python
s1 = {"liu", "zhao", "pi"}
s2 = {"liu", "feng", "pi"}
s4 = s1.intersection(s2) # 取两个集合的交集
print(s4) # {"liu", "pi"}

s3 = s1 & s2 # 取两个集合的交集
# 得到的结果一摸一样
```

**4. 并集**
```python
s1 = {"liu", "zhao", "pi"}
s2 = {"liu", "feng", "pi"}
s4 = s1.union(s2) # 取两个集合并集
s3 = s1 | s2 # 取两个集合并集
```

**5. 差集**
```python
s1 = {"liu", "zhao", "pi"}
s2 = {"liu", "feng", "pi"}
s4 = s1.difference(s2) # 求s1中有s2中没有的值
s3 = s1 - s2 # 跟上边一样的结果

s5 = s2.difference(s1) # 求s2中有s1中没有的值
s6 = s2 - s1
```
