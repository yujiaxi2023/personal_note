
1. import from numpy
```python
a = np.array([2,3.3])
# 创建一个dim=1 长度为2的向量
torch.from_numpy(a)
# 使用.from_nunoy的函数将numpy作为参数导入 数据维持不变 继续是原来的数据类型
# numpy导入的float是double类型

a = np.ones([2,3])
# numpy的ones函数新建矩阵行列为2和3 所有的元素都是1
torch.from_numpy(a)
# 同样的所有的数据保持不变 只是数据类型变为了torch中自带的类型
"""
输出为
tensor([2.0000, 3.3000], dtype=torch.float64)
tensor([[1., 1., 1.],
        [1., 1., 1.]], dtype=torch.float64)
"""
```

2. import from list
```python
torch.tensor([2., 3.2])
# tensor直接写入数据
# FloatTensor/Tensor只接受shape作为参数 数据的维度

torch.FloatTensor([2., 3.2])
# FloatTensor必须要用list包住现有的数据 一般不使用容易混淆
# 如果是torch.FloatTensor(2, 3)表示生成2行3列 或者说shape是(2,3)的数据 并且不需要初始化

torch.tensor([[2., 3.2], [1., 22.3]])
"""
结果
tensor([2.0000, 3.2000]) 

tensor([2.0000, 3.2000]) 

tensor([[ 2.0000,  3.2000],
        [ 1.0000, 22.3000]])
"""
```
数据量不是很大，只用导入一个2x2或1x2的数据类型

**如何生成未初始化的数据 有下面三种方法**
- torch.empty()
- torch.FloatTensor(d1,d2,d3)
- torch.IntTensor(d1,d2,d3)

举例说明
```python
torch.empty(1)

torch.Tensor(2,3)

torch.IntTensor(2,3)

torch.FloatTensor(2,3)

"""
结果
tensor([9.0000e-39])
tensor([[ 0.0000e+00,  0.0000e+00,  2.1019e-44],
        [ 0.0000e+00, -1.5661e-18,  6.0536e-43]])
tensor([[          0,           0,          15],
        [          0, -1578689024,         432]], dtype=torch.int32)
tensor([[9.0000e-39, 9.0918e-39, 1.0102e-38],
        [1.0745e-38, 1.0469e-38, 1.0102e-38]])
"""
```
可以看到生成的数据非常的不规则，可能出现有非常大的非常小的
会出现torch.nan or torch.inf

**设定默认类型**
```python
torch.tensor([1.2, 3]).type()
# Tensor代表的是pytorch中的默认的类型，如果不做任何设置就会转换未floattensor类型
# 'torch.FloatTensor'

torch.set_default_tensor_type(torch.DoubleTensor)
# 如果我们进行转换就可以更换这个默认类型

torch.tensor([1.2, 3]).type
# 'torch.DoubleTensor'
```
在RNN中我们一般使用doubletensor的类型，因为其有更高的精度

**随机初始化**
rand/rand_like, randint

- rand是随机产生0-1之间的均值分布，不包括1

- rand_like接受的参数是一个tensor 读取shape后送给rand函数生成新的张量

- randint需要指定极小值和极大值 【1, 10) 【min,max)
- randint也有_like函数

```python
torch.rand(3,3)

a = torch.rand(3,3)

torch.rand_like(a)

torch.randint(1,10,[3,3])
# 第三个参数是一个整体所以使用list 指定最小值最大值
# randint只能采样整数

"""
结果
tensor([[0.2260, 0.4153, 0.3495],
        [0.2611, 0.0702, 0.6759],
        [0.5696, 0.1898, 0.3363]])
tensor([[6, 1, 8],
        [7, 4, 8],
        [7, 6, 4]])
"""
```

**正态分布**
randn
用于权值或者bias的初始化
- N(0,1) 均值为0 方差为1
- N(u,std)
```python
torch.randn(3,3)

torch.normal(mean=torch.full([10],0), std=torch.arange(1, 0, -0.1))

torch.normal(mean=torch.full([10],0), std=torch.arange(1, 0, -0.1))
# 注意arange不包含右边界
```
注意上述写法有点问题，因为normal函数括号内有long类型的张量
应该改以下
```python
torch.randn(3,3)

torch.normal(mean=torch.full([10],0.), std=torch.arange(1., 0., -0.1))

torch.normal(mean=torch.full([10],0.), std=torch.arange(1., 0., -0.1))
# 后两行代码都是添加了.在数字后边将其变为浮点型
"""
结果
tensor([[ 1.5336, -1.2337,  0.3179],
        [-0.9974,  0.2433, -1.3467],
        [-0.3894, -1.2934, -0.6070]])
tensor([-1.3949, -0.6421,  1.2289, -0.8847, -0.3830, -0.7389,  0.2682, -0.6554, -0.0931,  0.0057])
tensor([ 0.3917,  0.7329,  1.0442, -1.1142, -0.2134, -0.3657,  0.7273,  0.1845, -0.2759,  0.0927])
"""
```

如果需要自定义标准差和均值
如果我们要一个3x3的张量，首先需要让它变为一列9的list
![[Pasted image 20230508162456.png]]
所以我们需要先对这9个数据求均值和方差
![[Pasted image 20230508162542.png]]

**如果要把tensor赋值为同一个元素**
full函数
```python
torch.full([2,3],7)
torch.full([],7)
torch.full([1],7)
"""
结果
tensor([[7, 7, 7],
        [7, 7, 7]])
tensor(7)
tensor([7])
注意不是浮点型数据
"""
```
![[Pasted image 20230508163954.png]]
提供的教材中是floattensor类型的数据
如果是标量 list中就不要计入数值,如果是dim=1的向量,就在list中计入1
list中的第一个数字是表示张量的形状中的行向量,第二个数字表示列向量
更高维的向量就依次类推,从代表的第一个维度开始往上推论

**递增或者递减形成等差数列**
arange/range
```python
torch.arange(0,10)
# 0-10不包括10的等差数列 默认是1递增
torch.arange(0,10,2)
# 第三个参数是代表的等差的差值
torch.range(0,10)
# 不建议使用这个函数

"""
结果
C:\Users\student\PycharmProjects\01 regression proble\basic operation.py:87: UserWarning: torch.range is deprecated and will be removed in a future release because its behavior is inconsistent with Python's range builtin. Instead, use torch.arange, which produces values in [start, end).
  print(torch.range(0,10))
tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
tensor([0, 2, 4, 6, 8])
tensor([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
"""
```

**等分形成等差数列**
```python
import math

torch.linspace(1,10, steps=4)
# 这里的两边都是闭区间,也就是10也取值
torch.linspace(1,10, steps=10)
torch.linspace(1,10, steps=11)
torch.logspace(0,-1, steps=10)
torch.logspace(0,-1, steps=10, base=2)
print(torch.logspace(0, -1, steps=10, base=math.e))
# logspace 的base参数可以设置为2,10,e等底数
# 使用e之前需要导入math

"""
结果
tensor([ 1.,  4.,  7., 10.])
tensor([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
tensor([ 1.0000,  1.9000,  2.8000,  3.7000,  4.6000,  5.5000,  6.4000,  7.3000,
         8.2000,  9.1000, 10.0000])
tensor([1.0000, 0.7743, 0.5995, 0.4642, 0.3594, 0.2783, 0.2154, 0.1668, 0.1292,
        0.1000])
tensor([1.0000, 0.9259, 0.8572, 0.7937, 0.7349, 0.6804, 0.6300, 0.5833, 0.5400,
        0.5000])
tensor([1.0000, 0.8948, 0.8007, 0.7165, 0.6412, 0.5738, 0.5134, 0.4594, 0.4111,
        0.3679])
"""
```
![[Pasted image 20230508165648.png]]
这个log是作为底的


生成全部是0 1的张量
ones/zeros/eye
eye代表单位矩阵

```python
torch.ones(3,3)
torch.zeros(3,3)
torch.eye(3,4)

"""
结果
tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]])
tensor([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])
tensor([[1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.]])
"""
```
对于eye矩阵可以直接
```python
torch.eye(3)
# 直接生成3x3矩阵
```
也可以使用_like方法
```python
a = torch.zeros(3,3)
torch.ones_like(a)
```


**随机打散**
randperm
- random.shuffle
这个函数是用来生成从0到n-1的整数的随机排列的,并且可以随机打乱样本
```python
torch.randperm(10)
# tensor([1, 7, 0, 8, 9, 3, 6, 5, 4, 2])
```
现在我们要实现,有3位同学,考了有数学分数小分,和语文分数小分
我们需要随机打散这两位同学的顺序,但是要保证对应的分数是正确的
```python
a = torch.rand(3,3) # 代表数学成绩小分 有3部分
b = torch.rand(3,2) # 代表语文成绩小分 有2部分
idx = torch.randperm(3)
a[idx]
b[idx]
print(a)
print(b)
```
根据idx对a和b的行进行重新排序的方法是使用索引操作，即`a[idx]`和`b[idx]`。这样，a和b的第i行就会变成原来的第idx[i]行。例如，如果idx是`tensor([2, 0, 1])`，那么a和b的第0行就会变成原来的第2行，第1行就会变成原来的第0行，第2行就会变成原来的第1行。