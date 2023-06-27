is 和 == 的区别是什么？
- == 用于 比较两个值是否相等
- is 用于表示内存地址是否一致
```python
# example
v1 = []
v2 = []

print(v1 == v2) # True 两个值相当
print(v1 is v2) # False 不属于同一块内存
```
```python
# example
v1 = []
v2 = v1

print(v1 == v2) # True 两个值相当
print(v1 is v2) # True 属于同一块内存
```
```python
# example
v1 = None
v2 = None

print(v1 == v2) # True 两个值相当
print(v1 is v2) # True 属于同一块内存
```
None内存都是同一个位置
