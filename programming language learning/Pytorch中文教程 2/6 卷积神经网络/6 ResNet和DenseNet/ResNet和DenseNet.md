深度残差网络
残差模块

让梯度弥散或者梯度爆炸
希望更深层的网络不会比浅层网络更差
![[Pasted image 20230510150259.png]]
这样我们中间添加一个模块
捷径的存在让中间没有进行衰减
这是每隔几层添加一个捷径

![[Pasted image 20230510150516.png]]
这就是一个unit
![[Pasted image 20230510150530.png]]

这样一个unit最好选择2-3个卷积层比较合适
![[Pasted image 20230510150657.png]]
这个残差模块不能够进行维度或者是channel的衰减
所以要保证进去之后变化结束后的 x‘ 和 输入的x 是一样的size
这样才能够相加
才能保证不会比原来差

![[Pasted image 20230510150910.png]]
如果是按照这个层计算是减少90的内存
![[Pasted image 20230510150958.png]]

![[Pasted image 20230510151307.png]]

![[Pasted image 20230510151705.png]]
这就是残差网络的原因
中间计算的就是残差
使用新的函数减去上一层的输入 就是中间的变化值

一个resnet是如何实现的
```python
class ResBlk(nn.Module):
	def __init__(self, ch_in, ch_out):
		self.conv1 = nn.Conv2d(ch_in, ch_out, kernel_size=3, stride=1, padding = 1)
		self.bn1 = nn.BatchNorm2d(ch_out)
		self.conv2 = nn.Conv2d(ch_out, ch_out, kernel_size=3, stride=1, padding=1)
		self.bn2 = nn.BatchNorm2d(ch_out)
		self.extra = nn.Sequential()
		if ch_out != ch_in:
		# [b,ch_in,h,w] => [b,ch_out,h,w]
			self.extra = nn.Sequential(
				nn.Conv2d(ch_in, ch_out, kernel_size=1, stride=1),
				nn.BatchNorm2d(ch_out)
				)
	def forward(self, x):
		out = F.relu(self.bn1(self.conv1(x)))
		out = self.bn2(self.conv2(out))
		out = self.extra(x) + out
		return out
```
![[Pasted image 20230510152505.png]]
上面就是一个基本单元
ch in 和 ch out 可以不一致
![[Pasted image 20230510152807.png]]
使用这个代码就可以让其维度保持一致可以相加
![[Pasted image 20230510152842.png]]


**DenseNet**
在resnet基础上拓展，这种捷径可以连接到各种的层
其实是做了一个concat操作
必须要设计不让后边的占用数据过多
