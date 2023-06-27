**基本使用方法**
创造一个矩阵
```python
x = torch.empty(5,3)
x
```
![[Pasted image 20230430150812.png]]
```python
x = torch.rand(5,3)
x
```
![[Pasted image 20230430150858.png]]
输出的格式是tensor张量格式
![[Pasted image 20230430150658.png]]
![[Pasted image 20230430150704.png]]

初始化全零的矩阵
```python
x = torch.zeros(5,3,dtype=torch.long)
```
![[Pasted image 20230430151007.png]]
```python
x = x.new_ones(5,3,dtype=torch.double)

x = torch.randn_like(x,dtype=torch.float)
```
这里的randn_like 是跟前面的矩阵构建一样的矩阵
![[Pasted image 20230430151150.png]]

展示矩阵大小
```python
x.size()
```
![[Pasted image 20230430151227.png]]

基本计算方法
```python
y = torch.rand(5,3)
x + y
```
![[Pasted image 20230430151313.png]]
```python
torch.add(x,y) # 一样的也是上面加法的操作
```
![[Pasted image 20230430151347.png]]

索引
```python
x[:,1] #冒号表示取所有，后边的数字表示取第几个
```
![[Pasted image 20230430151534.png]]

view操作可以改变矩阵维度
```python
x = torch.randn(4,4)
y = x.view(16)
z = x.view(-1,8)
print(x.size(), y.size(), z.size())
```
![[Pasted image 20230430151719.png]]

与numpy的协同操作
```python
a = torch.ones(5)
b = a.numpy()
```
需要把tensor格式转换为array的格式
![[Pasted image 20230430151813.png]]
这样就可以和numpy交互

```python
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
```
![[Pasted image 20230430151911.png]]
