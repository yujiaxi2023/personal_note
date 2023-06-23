使用一个案例
烤咖啡豆的时间和温度作为xy轴进行绘制，x表示得到良好的咖啡
![[Pasted image 20230516124359.png]]
![[Pasted image 20230516124501.png]]
使用200摄氏度和17分钟能否得出好的咖啡可以经过计算得到
现在可以将输入设置为
```python
x = np.array([[200.0, 17.0]])
layer_1 = Dense(units=3, activation='sigmoid')
a1 = layer_1(x)

layer_2 = Dense(units=1, activation='sigmoid')
a2 = layer_2(a1)

if a2 >= 0.5:
	yhat = 1
else:
	yhat = 0
```
Dense代表的神经网络
这里没有加载tensorflow lib 并且没有设置 w 和 b
![[Pasted image 20230516125116.png]]
现在设置x是一个图像数据
```python
x = np.array([[0.0,...245,...240...0]])
layer_1 = Dense(units=25, activation='sigmoid')
a1 = layer_1(x)

layer_2 = Dense(units=15, activation='sigmoid')
a2 = layer_2(a1)

layer_3 = Dense(units=1, activation='sigmoid')
a3 = layer_3(a2)

if a3 >= 0.5:
	yhat = 1
else:
	yhat = 0
```

tensorflow中的数据形式
numpy储存矩阵的形式
![[Pasted image 20230516151451.png]]
![[Pasted image 20230516151520.png]]
现在有一个两行三列的矩阵，它的数据表现在numpy中是右侧的样子
![[Pasted image 20230516151655.png]]
2d形式的矩阵可以多种多样
从下面例子中可以看出np array定义是什么
![[Pasted image 20230516151926.png]]
关键在于最后一个定义
这个代表的是只是一个1d的向量也就是标量，所以不存在矩阵形式
对于下列一个神经网络
![[Pasted image 20230516152200.png]]
![[Pasted image 20230516152210.png]]
这个式子中的 a1 代表一个 1x3 的矩阵
如果用tensorflow的形式表示
```python
tf.Tensor([[0.2 0.7 0.3]], shape=(1, 3), dtype=float32)
```
![[Pasted image 20230516152540.png]]
如果使用numpy数组形式表示
![[Pasted image 20230516152627.png]]

![[Pasted image 20230516174522.png]]
上述是构建的神经网络的层
接下来是把两层网络放到一个sequential中
![[Pasted image 20230516174822.png]]
假设我们现在有下面的训练集 x 和 y
![[Pasted image 20230516174846.png]]
需要把训练集转换为可以输入到运算程序中的形式
![[Pasted image 20230516174911.png]]
接下来就是进行模型计算
![[Pasted image 20230516174923.png]]
![[Pasted image 20230516175012.png]]

使用tensorflow进行模型构建
![[Pasted image 20230516175213.png]]
这是进行图像识别的方式
