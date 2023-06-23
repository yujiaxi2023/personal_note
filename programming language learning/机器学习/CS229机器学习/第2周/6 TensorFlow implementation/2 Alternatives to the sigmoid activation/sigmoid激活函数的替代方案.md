从二分类问题扩展
我们现在不希望限定在0-1的区间范围,希望能够扩展到一个很大的数字
现在我们有了ReLU激活函数
![[Pasted image 20230522182112.png]]
最常见的 集中激活函数
![[Pasted image 20230522182215.png]]
第一种是没有添加激活函数,因为不会产生任何非线性变化

可以对不同的神经元选择不同的激活函数
![[Pasted image 20230523125555.png]]
实际上选择激活函数的很重要的就是根据ground truth label来确定

如果我们是一个二分类问题,选择sigmoid函数就是一个好的方案
![[Pasted image 20230523125648.png]]

如果正在解决回归回归问题,如果是预测未来的股价变化,也就是一个上下问题
![[Pasted image 20230523125735.png]]
未来的结果相对于现在的结果是增加还是减少

如果regression 中的label y只能是非负数的,这个时候选择ReLU函数比较合适
![[Pasted image 20230523125824.png]]

对于hidden layer中最常见使用的是ReLU 函数
在早期神经网络中比较常使用sigmoid但是现在很少使用了
![[Pasted image 20230523125927.png]]

因为ReLU函数 可以有更少的计算量
如果在梯度下降的时候有很多的flat 平的部分,这样会下降的很慢
这个的原因 是在求参数的偏导数的时候如果函数图像是flat也就是平的时候,偏导数的值为0
![[Pasted image 20230523130544.png]]

在output layer中可以有多种的选择方式
原则上是
二分类问题使用sigmoid函数
回归问题使用线性激活函数
大于0的回归问题使用ReLU激活函数
![[Pasted image 20230523130713.png]]

在tensorflow中实现
```python
from tf.keras.layers import Dense
model = Sequential([
	Dense(units=25, activation='relu'),
	Dense(units=15, activation='relu'),
	Dense(units=1, activation='sigmoid')
])
```
![[Pasted image 20230523131040.png]]

如果只使用linear activation情况下
![[Pasted image 20230523143821.png]]
如果我们输入一个数字到一个神经元中
经过神经网络的线性激活之后
![[Pasted image 20230523143914.png]]
计算输出层的结果是
![[Pasted image 20230523144018.png]]
输出的结果形式还是wx + b

所以不管经过多少层的计算,最后结果的形式不会改变
![[Pasted image 20230523144225.png]]

