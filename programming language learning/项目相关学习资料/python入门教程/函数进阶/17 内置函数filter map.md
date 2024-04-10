**filter**：筛选
```python
lst = ["张无忌", "张三丰", "张翠山", "灭绝师太", "妲己"]  
# 要提取出所有姓张的 下面lambda函数是返回的true false结果  
f = filter(lambda x: x.startswith("张"), lst)  
print(f) # <filter object at 0x0000029D3FEDC3D0>  
print(list(f)) # ['张无忌', '张三丰', '张翠山']  
f1 = filter(lambda x: not x.startswith("张"), lst)  
print(list(f1)) # ['灭绝师太', '妲己']
```
![[Pasted image 20230919000338.png]]
类似于是有了一个true和false的一个列表作为filter过滤


**map**：映射
```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
# 希望有result = [1, 4, 9, 16, 25, 36, 49, 64, 81]  
result = [item * item for item in lst]  
print(result) # [1, 4, 9, 16, 25, 36, 49, 64, 81]  
r = map(lambda x: x**2, lst)  
print(list(r)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]
```
功能是上下一样的，但是map在后边数据分析可能有别的进阶用法
