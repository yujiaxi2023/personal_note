构造一组输入数据X和对应的标签y
```python
x_values = [i for i in range(11)]
x_train = np.array(x_values, dtype=np.float32) # 现在是nparray格式
x_train = x_train.reshape(-1,1) # 进行转换为tensor张量 转换为矩阵格式
x_train.shape
```
![[Pasted image 20230430161949.png]]
```python
y_values = [2*1 + 1 for i in x_values]
y_train = np.array(y_values, dtype=np.float32)
y_train = y_train.reshape(-1,1)
y_train.shape
```
![[Pasted image 20230430162202.png]]

```python
import torch
import torch.nn as nn
```

线性回归模型
线性回归就是一个不加激活函数的全连接层

```python
class LinearRegressionModel(nn.Module):
	def __init__(self, input_dim, output_dim):
		super(LinearRegressionModel, self).__init__()
		self.linear == nn.Linear(input_dim, output_dim) 
		# 输入数据的维度和输出数据的维度，这里直接当参数传进去比较好
		# 这里用到哪个层就将哪个层拿出来定义

	def forward(self, x):
		# 这里前向传播也是 定义自己的走法
		out = self.linear(x)
		return out
```
```python
input_dim = 1
output_dim = 1

model = LinearRegressionModel(input_dim, output_dim)
```
![[Pasted image 20230430163818.png]]

指定好参数和损失函数

```python
epochs = 1000 # 迭代次数
learning_rate = 0.01
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate) # 优化器
criterion = nn.MSELoss() # 计算均方误差，也就是损失函数
```
```python
for epoch in range(epoches):
	epoch += 1
	# 注意转换为tensor
	inputs = torch.from_numpy(x_train)
	labels = torch.from_numpy(y_train)
	# 梯度需要清零每一次迭代
	optimizer.zero_grad()
	# 前向传播
	outputs = model(inputs)
	# 计算损失
	loss = criterion(outputs, labels)
	# 反向传播
	loss.backward()
	# 更新权重参数
	optimizer.step()
	if epoch % 50 == 0
		print('epoch {}, loss {}'.format(epoch, loss.item()))
		# 每隔五十次打印一次损失值
```
![[Pasted image 20230430165251.png]]

测试模型预测结果
```python
predicted = model(torch.from_numpy(x_train).requires_grad()).data.numpy()
print(predicted)
```
前向传播一次，最后的data.numpy是转换为array的格式
![[Pasted image 20230430165709.png]]

模型的保存与读取
```python
torch.save(model.state_dict(), 'model.pkl')
# 保存模型的权重参数 w和b 叫model.pkl 回自动加载pkl文件做文件保存
```
```python
model.load_state_dict(torch.load('model.pkl'))
```

动态的保存模型

使用GPU进行训练
只需要把数据和模型传入到cuda里面就可以了
```python
import torch  
import torch.nn as nn  
import numpy as np  
  
x_values = [i for i in range(11)]  
x_train = np.array(x_values, dtype=np.float32)  # 现在是nparray格式  
x_train = x_train.reshape(-1, 1)  # 进行转换为tensor张量 转换为矩阵格式  
x_train.shape  
  
y_values = [2 * 1 + 1 for i in x_values]  
y_train = np.array(y_values, dtype=np.float32)  
y_train = y_train.reshape(-1, 1)  
y_train.shape  
  
  
class LinearRegressionModel(nn.Module):  
    def __init__(self, input_dim, output_dim):  
        super(LinearRegressionModel, self).__init__()  
        self.linear = nn.Linear(input_dim, output_dim)  
  
    def forward(self, x):  
        out = self.linear(x)  
        return out  
  
  
input_dim = 1  
output_dim = 1  
  
model = LinearRegressionModel(input_dim, output_dim)  
  
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  
model.to(device)  
# 指定设备为cuda，这里是判断是否配置好cuda，如果没有配置好就会用cpu跑模型，model to代表着把模型放到那里  
  
criterion = nn.MSELoss()  
  
learning_rate = 0.01  
  
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  
  
epochs = 1000  
for epoch in range(epochs):  
    epoch += 1  
    inputs = torch.from_numpy(x_train).to(device)  
    labels = torch.from_numpy(y_train).to(device)  
    # 输入的x和y写一个to device就可以输入到gpu中  
    optimizer.zero_grad()  
    outputs = model(inputs)  
    loss = criterion(outputs, labels)  
    loss.backward()  
    optimizer.step()  
    if epoch % 50 == 0:  
        print('epoch {}, loss {}'.format(epoch, loss.item()))
```
输出结果
![[Pasted image 20230430172122.png]]
注意上述的整个的python流程经过检验是正确的

这里就可以明显介绍出，我们只用设计前向传播的模型，然后反向传播就会自动的进行计算
这就是所有的深度学习框架的核心点
