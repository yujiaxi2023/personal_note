![[Pasted image 20230517155251.png]]
对青蛙神经元研究的时候发现只有输入信号超过一定的阈值之后才会对下面一个神经元传递信息
小于这个阈值就没有输出，大于这个阈值就输出一个固定值

只有输入z大于0的时候才会输出一个值
这种函数无法求导
![[Pasted image 20230517155541.png]]
所以提出了一个可导的sigmoid函数
![[Pasted image 20230517155712.png]]
sigmoid函数的导数
![[Pasted image 20230517160008.png]]
sigmoid函数边缘区域会梯度弥散

```python
a = torch.linspace(-100, 100, 10)

print(a)
torch.sigmoid(a)
```
函数是从torch.nn.functional模块中来的
![[Pasted image 20230517160238.png]]

Tanh激活函数再RNN中使用比较多
![[Pasted image 20230517160333.png]]
![[Pasted image 20230517160348.png]]
比较类似于sigmoid函数但是值域不同
![[Pasted image 20230517160411.png]]
导数如上图所示

```python
a = torch.linspace(-1, 1, 10)
torch.tanh(a)
```
![[Pasted image 20230517160458.png]]

ReLU激活函数
Rectified Linear Unit 整型的线性单元
小于0的时候不反应，大于0的时候线性反应
![[Pasted image 20230517160600.png]]
没有放大和缩小的功能，会保持梯度不变，所以会减少激活函数带来的梯度弥散和爆炸的情况
```python
from torch.nn import functional as F
a = torch.linsapce(-1, 1, 10)
torch.relu(a)
F.relu(a)
```
![[Pasted image 20230517160754.png]]

均方差
Mean Squared Error
MSE
![[Pasted image 20230517192749.png]]
一般使用的是线性方程上使用
![[Pasted image 20230517192949.png]]
均方误差求导
![[Pasted image 20230517193130.png]]


Cross Entropy Loss
用于分类的 与softmax结合起来使用的
```python
x = torch.ones(1)
w = torch.full([1], 2)
mse = F.mse_loss(torch.ones(1), x*w)

torch.autograd.grad(mse, [w]) # 列表内是参数

```
这样会出现错误
![[Pasted image 20230517193438.png]]
因为最开始没有要求w是可以进行求导的
```python
w.requires_grad_()

torch.autograd(mse,[w])
```
这样修改还是出现错误
因为pytorch使用的是动态图，图还是原来的图，所以这样更新还是报错
```python
mse = F.mse_loss(torch.ones(1), x*w)

torch.autograd.grad(mse, [w])
```
![[Pasted image 20230517193612.png]]
重新定义之后才能够输出正确结果
也可以在新建的时候直接输入需要gradient信息
```python
w = torch.tensor([1], requires_grad=True)
```

另一种方法
loss.backward
首先还是建立动态图
```python
x = torch.ones(1)
w = torch.full([1],2)
mse = F.mse_loss(torch.ones(1), x*w)

torch.autograd.grad(mse, [w])

w.require_grad_()

torch.autograd.grad(mse,[w])

mse = F.mse_loss(torch.ones(1), x*w)
mse.backward()

w.grad
```
可以直接在loss 上面backward
![[Pasted image 20230522130232.png]]

求导过程可以有两种方式
- 手动进行求导
```python
torch.autograd.grad(loss, [w1, w2,...])
```

- 直接对最后的loss 做一个反向传播
```python
loss.backward()
```
![[Pasted image 20230522130535.png]]
两种方法返回的值是不同的
上面都是均方误差的求导方式
还有cross entropy的方式进行求导，在logistic regression中常用

**Softmax**
- soft version of max
首先我们把所有的取值利用sigmoid函数压缩到0 - 1 之间
然后现在对于多分类问题有一个条件是需要所有概率求和为1
所以引用了softmax函数，所有取值是0-1之间且和为1
最后softmax就会获得结果
![[Pasted image 20230522131042.png]]
它不仅可以将数值转换为概率，还可以将数值中最大值和最小值之间的差距拉开

softmax函数的求导方式
![[Pasted image 20230522133152.png]]
这是softmax函数表达式
从输入到输出，输入是ai 输出是pi
![[Pasted image 20230522133232.png]]
当i = j的情况下也就是a和p是对应关系
求偏导数过程如下
![[Pasted image 20230522133624.png]]
向前传播中已经有了pi和pj的值
所以在反向传播的时候，使用的softmax模块就可以直接结果是pi（1-pj）求值

当i != j
求导过程
![[Pasted image 20230522133916.png]]

所以综上可以得出
![[Pasted image 20230522134112.png]]
其正负号如图所示
![[Pasted image 20230522134321.png]]
图中是三个输入经过softmax函数之后得出的结果
可以看出结果对应着前面一层的3个输入均存在偏导，其中一个存在是 i = j 这时候偏导结果为正，另外两个 i != j 所以偏导为负数

利用pytorch进行计算
```python
a = torch.rand(3) # tensor([0.1440, 0.5349, 0.7022])
a.requires_grad_()
p = F.softmax(a,dim=0)
p.backward()

p = F.softmax(a,dim=0)
torch.autograd.grad(p[1],[a],retain_graph=True)

torch.autograd.grad(p[2],[a])
```
首先随即生成一个 dim 1 长度为3的tensor
首先让其保留grad的信息可以进行求梯度
首先我们需要认识到softmax函数应该是对feature维度上面进行操作
而不是batch维度上进行操作，因为没有作用
![[Pasted image 20230522135318.png]]
如果我们直接调用
```python
p.backward()
```
上面的代码时由于之前已经调用过一次backward 所以自动会清除掉需要梯度信息的命令，也就是代表，如果就是这样写命令，下一次的backward就会报错下列信息
![[Pasted image 20230522135539.png]]
这个时候我们需要修改代码
```python
p.backward(require_grad = True)
```
这样进行了backward操作之后就会保留其梯度信息
最后的loss一定是一个dim 1 长度1的东西或者是一个scaler
所以代码中是调用其中的 第 012 变量 进行计算
