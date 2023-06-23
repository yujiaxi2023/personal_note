首先还是看logistics regression
![[Pasted image 20230523152948.png]]
二分类问题中我们只需要关注其中一个的输出,剩下一个输出直接非就可以了
也就是1-第一个输出

在softmax regression中
![[Pasted image 20230523153141.png]]
这些结果的加和也是必须为100% 

如果是n分类问题
![[Pasted image 20230523153354.png]]
![[Pasted image 20230523153628.png]]
对于logistics regression的损失函数
当y取值不同的时候是不一样的loss function,所以结果应该是不一样的

对于softmax regression
这里的分类就变成了n个函数
![[Pasted image 20230523153928.png]]
![[Pasted image 20230523154054.png]]
在这个损失计算中,是为了让loss 更加靠近1

如果需要完成十分类问题
这里的output layer 是需要添加到10个单元
![[Pasted image 20230523160139.png]]

![[Pasted image 20230523160243.png]]

这里的softmax function跟之前的sigmoid 或者是ReLU不太一样
因为这里计算出来的softmax 中包含了前面的z1-z10
如果是sigmoid或者是ReLU,z1就只跟a1有关,z10 只跟a10相关

在tensorflow中实现
```python
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
model = Sequential([
	Dense(units=25, activation='relu'),
	Dense(units=15, activation='relu'),
	Dense(units=10, activation='softmax')
])
```
![[Pasted image 20230523160731.png]]
```python
from tensorflow.keras.losses import
	SparseCategoricalCrosstropy
model.compile(loss= SparseCategoricalCrossentropy())
```
![[Pasted image 20230523160859.png]]
```python
model.fit(X,Y,epochs=100)
```
![[Pasted image 20230523160951.png]]


一个更好的使用softmax 的方法 
现在计算有两种方法可以得到同一种结果
![[Pasted image 20230523164743.png]]
```python
x1 = 2./10000
print(f"{x1:.18f}") # 打印小数点后的18位

x2 = 1 + (1/10000) - (1-1/10000)
print(f"{x2:.18f}") 
```
![[Pasted image 20230523165229.png]]
这代表我们式子写对了,但是计算结果是存在误差的

![[Pasted image 20230523165418.png]]
更新的关键,减少误差的关键在于减少中间量
![[Pasted image 20230523165553.png]]
这里就是将a直接写入表达式,这样可以减少roundoff errors

![[Pasted image 20230523165721.png]]
更新了之后最后一层的sigmoid函数就应该变为没有激活函数的形态
然后再求损失函数的时候,直接引入lib中包含有的logit函数z 也就等于sigmoid函数式子,只不过是在计算loss 的时候计算

![[Pasted image 20230523170007.png]]
这样计算能够更精确的原理是,tensorflow可以忽略掉计算出来ezi非常小或者非常大的情况

针对自动驾驶系统，需要进行多分类问题的识别
单个输入的图像中应该包含有多个label
![[Pasted image 20230523184102.png]]

由几种方式可以实现
第一种
使用不同的神经网络进行不同的识别任务
![[Pasted image 20230523184153.png]]
这个也是可行的分类方式

第二种
在output中输出的是3个不同的label值
![[Pasted image 20230523184242.png]]

所以multi label classification 和 multi class classification是不一样的
