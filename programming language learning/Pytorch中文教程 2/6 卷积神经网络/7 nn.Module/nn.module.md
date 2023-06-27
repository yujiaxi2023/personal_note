是构建网络都需要使用的一个父类
```python
class MyLinear(nn.Module):
	def __init__(self, inp, outp):
		super(MyLinear, self).__init__()
		# requires_grad = True
		self.w = nn.Parameter(torch.randn(outp, inp))
		self.b = nn.Parameter(torch.randn(outp))
	def forward(self, x):
		x = x @ self.w.t() + self.b
		return x
```
初始化中完成自己的逻辑
forward中构建计算图的前向构建

- nn.Module是一个父类
nn.Linear
nn.BatchNorm2d
nn.Conv2d

- nn.Module可以嵌套

有什么好处
1. 提供了很多的模块 非常的方便
- Linear
- ReLU
- sigmoid
- Conv2d
- ConvTransposed2d 转置卷积层
- Dropout
- ···

调用初始化函数 然后用 .call 调用forward函数

2. container
```python
self.net = nn.Sequential(
	nn.Conv2d(1, 32, 5, 1, 1),
	nn.MaxPool2d(2, 2),
	nn.ReLU(True),
	nn.BatchNorm2d(32),

	nn.Conv2d(32, 64, 3, 1, 1),
	nn.ReLU(True),
	nn.BatchNorm2d(64),

	nn.Conv2d(64, 64, 3, 1, 1),
	nn.MaxPool2d(2, 2),
	nn.ReLU(True),
	nn.BatchNorm2d(64),

	nn.Conv2d(64, 128, 3, 1, 1),
	nn.ReLU(True),
	nn.BatchNorm2d(128)
)
```
Sequential 容器
里面不仅可以调用已有的nn module中的模块
还可以调用自己写的模块
![[Pasted image 20230510155108.png]]
这样可以 重复很多很多次这样的流程

3. parameters 可以管理参数
```python
net = nn.Sequential(nn.Linear(4,2), nn.Linear(2,2))
list(net.parameters())[0].shape
list(net.parameters())[3].shape
list(net.named_parameters())[0]
list(net.named_parameters())[1]

dict(net.named_parameters()).item()
optimizer = optim.SGD(net.parameters(),lr=1e-3)
```
两个线性层通过concat融合在一起
使用.parameter方法会返回一个生成器list
里面包含有所有的参数
![[Pasted image 20230510155712.png]]
pytorch给每个参数起名字 比如weight 或者bias
这里返回的是第0维度的weight和bias
![[Pasted image 20230510155831.png]]

如果使用dict 调用item
![[Pasted image 20230510155906.png]]

可以用optim方法导入到优化器中进行优化


4. modules 内部的模块
- modules：all nodes
- children：direct children

可以得到一个网络结构的直系亲属
```python
class BasicNet(nn.Module):
	def __init__(self):
		super(BasicNet.self).__init__()
		self.net = nn.Linear(4,3)
	def forward(self, x):
		return self.net(x)

class Net(nn.Module):
	def __init__(self):
		super(Net, self).__init__()
		self.net = nn.Sequential(BasicNet(), nn.ReLU(), nn.Linear(3,2))
	def forward(self, x):
		return self.net(x)
```
我们首先定义了一个basicnet
然后要查看这个根节点的children是什么
![[Pasted image 20230510160652.png]]
可以看到有这些参数
这个net 的children就是一个sequential类
![[Pasted image 20230510160729.png]]
有5个children 分别如下
![[Pasted image 20230510160821.png]]


5. 可以把内部所有的tensor转移到cpu或者cpu上 to（device）
```python
device = torch.device('cuda')
net = Net()
net.to(device)
```
a.to返回的是a-gpu
前者是cpu的

对于一个nn.module 返回的是同一个东西
只有是tensor是可以在cpu和gpu中用这个命令互换

6. save and load 保存和加载
```python
device = torch.device('cuda')
net = Net()
net.to(device)

net.load_state_dict(torch.load('ckpt.mdl'))

torch.save(net.state_dict(), 'ckpt.mdl')
```
训练中每隔一段时间就check point
这是一个save操作
![[Pasted image 20230510161441.png]]
开始train之前要检查是否有check point
先把保存文件load为pytorch的类
然后数据加载到参数里面，这样就不需要从0开始train


7. train 和 test 状态切换
dropout 或者 bnorm 在train 和 test 中是不一样的
分别需要对于每一个nn.module状态进行切换就麻烦
如果我使用的所有的模块都是来自于module
那我就只需要一行命令就可以进行切换
```python
device = torch.device('cuda')
net = Net()
net.to(device)

# train
net.train()

# test
net.eval()
```


8. 实现我们自己的类 implement own layer
例如在pytorch中没有一个展平的操作
```python
class Flatten(nn.Module):
	def __int__(self):
		super(Flatten, self).__init__()
	def forward(self, input):
		return input.view(input.size(0), -1)
class TestNet(nn.Module):
	def __init__(self):
		super(TestNet, self).__init__()
		self.net = nn.Sequential(nn.Conv2d(1, 16, stride=1, padding=1),
		nn.MaxPool2d(2,2),
		Flatten(),
		nn.Linear(1*14*14, 10))
	def forward(self, x):
		return self.net(x)
```
还有一个reshape功能没有提供类功能
只有函数功能
只有class 能够写到nn.Sequential里
![[Pasted image 20230510162517.png]]

更底层的一个类的实现
```python
class MyLinear(nn.Module):
	def __init__(self, inp, outp):
		super(MyLinear, self).__init__()
		# requires_grad = True
		self.w = nn.Parameter(torch.randn(outp, inp))
		self.b = nn.Parameter(torch.randn(outp))
	def forward(self, x):
		x = x @ self.w.t() + self.b
		return x
```
定义一个线性函数
nn.Parameter是一个包装的类 封装一下
可以让你的tensor进入到这个类中,然后就会自动的进行requires_grad = True
然后再forward中写好我们的逻辑然后返回
这个自己定义的linear 和 已经有的linear是完全没有区别的