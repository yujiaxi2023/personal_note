0：scalar
1：vector
2：matrix
3：n-dimentional tensor

```python
import torch
from torch import tensor
```

scalar 数值
vector 向量
matrix 矩阵
n-dimentional tensor 高纬度数据

**Scalar**
通常是一个数值
```python
x = tensor(42.)
x
```
![[Pasted image 20230504171224.png]]

```python
x.dim()
```
![[Pasted image 20230504171236.png]]
dimention 维度

```python
2 * x
```
![[Pasted image 20230504171312.png]]
数值计算

```python
x.item()
```
![[Pasted image 20230504171333.png]]
有几项

**vector**
例如：【-5.，2.，0.】比如这三个特征是身高体重年龄，一个向量中是很多个值组成的
```python
v = tensor([1.5, -0.5, 3.0])
print(v)
v.dim()
v.size()
```
![[Pasted image 20230504171632.png]]
维度和size都可以查看

**matrix**
- 一般计算的都是矩阵，通常是多维度的
就是许多向量组成的矩阵
```python
M = tensor([[1., 2.],[3., 4.]])
print(M)
```
![[Pasted image 20230504172637.png]]
构建了一个矩阵
```python
M.matmul(M)
```
![[Pasted image 20230504172757.png]]
```python
tensor([1., 0.]).matmul(M)
```
![[Pasted image 20230504172841.png]]
```python
M * M
```
![[Pasted image 20230504172903.png]]
```python
tensor([1., 2.]).matmul(M)
```
![[Pasted image 20230504172943.png]]
计算矩阵的内积和乘法

![[Pasted image 20230504173059.png]]
![[Pasted image 20230504173111.png]]
对于图像中不仅是有像素值，还有RGB三个channel

