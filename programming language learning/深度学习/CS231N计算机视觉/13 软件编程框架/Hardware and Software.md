![[Pasted image 20230331145738.png]]
Torch采用的Lua语言编写的，有了Python接口就变成了PyTorch，是facebook的
tensorflow是google，百度有paddlepaddle的平台，MXNet是Amazon的，CNTK是mircrosoft
集成到一起是Keras，比较适合初学者
![[Pasted image 20230331150455.png]]
![[Pasted image 20230331150851.png]]
keras可以快速验证模型，在tensorflow和pytorch可以构建计算图，自动求导
![[Pasted image 20230331151029.png]]
在numpy上面写一个右侧的计算图应该怎么做
首先初始化xyz三个变量，然后写公式
![[Pasted image 20230331151130.png]]
如果c相对于xyz的偏导数，需要手动构建局部梯度
例如c相对于自己的梯度是1
b的上游梯度c，做求和算法是梯度的均分，就用全1矩阵
a和z用+门是和b的梯度相同，所以copy一份b的梯度
xy是相乘，所以梯度是交换，所以用上游梯度相乘对方就是对方的梯度
![[Pasted image 20230331151544.png]]
numpy构建是只能在CPU上运行，无法在GPU运行
![[Pasted image 20230331151731.png]]
randn是随机数标准正态分布
将ND两个初始设定的数字传入，形成了一个xshape的矩阵，3x4的矩阵
每一个值都是符合均值为0，标准差为1的标准正态分布
![[Pasted image 20230331151939.png]]
然后构建出前向的计算图，也就是下面的公式
然后把中间计算图每一步的上游梯度构建出来
运行就可以计算出这几个梯度
![[Pasted image 20230331152115.png]]
在pytorch中就是numpy加上自动求导机制，然后加上了GPU
![[Pasted image 20230331152157.png]]
pytorch就不需要我们一个个从计算图中进行梯度计算
不需要手工构建梯度
![[Pasted image 20230331152402.png]]
pytorch也可以指定GPU
![[Pasted image 20230331152430.png]]
pytorch有3大抽象层次，tensor就是类似于numpy的array，可以GPU上运行
自动求导，追踪计算图，上面c.backward就是c相对于x的偏导数
能够自动求导的tensor,张量称为变量variable
pytorch封装好的module,激活函数,线性层,卷积层等等,也可以根据父类自定义一些函数
![[Pasted image 20230331153106.png]]
![[Pasted image 20230331153128.png]]
![[Pasted image 20230331153151.png]]
生成了4个随机数组
![[Pasted image 20230331153210.png]]
前向运算mm表示矩阵的乘法
代码表示使用relu函数,第一个神经网络的输出乘以第二个神经网络的权重,得到第二个神经网络 的输出,是一个线性层,预测值减去标签值平方求和是均方误差损失函数,L2损失函数
![[Pasted image 20230331153515.png]]
![[Pasted image 20230331153542.png]]
根据反向传播梯度设定学习率
![[Pasted image 20230331153604.png]]
为了简便手动求导的模式,直接用loss.backward,就是求出requires_grad=True的损失函数
![[Pasted image 20230331153722.png]]
需要用with函数让autograd不跟踪下面的内容,也就是w1和w2学习率的内容,而且每次需要把w1和w2这两个权重更新为0,不然会进行叠加
![[Pasted image 20230331153848.png]]
这段是为了用自动求导去求得loss相对于xy的梯度而不是w1和w2的梯度
![[Pasted image 20230331153928.png]]
定义前向传播的过程求得loss这个损失函数
![[Pasted image 20230331154044.png]]
下划线的操作是in-place,是更新了内存的内容,想让w1.grad这个内容重新变为0
![[Pasted image 20230331154139.png]]
其中ctx是内部参数
![[Pasted image 20230331154306.png]]
定义一个类,然后实例化一个对象,就出席拿了一个myrelu函数,这里有一个apply是因为function是一个父类函数,所以我们apply这个函数
![[Pasted image 20230331154503.png]]
nn模块,可以导入各种层,sequential就是搭积木,可以把下面的函数叠加到一块
![[Pasted image 20230331154604.png]]
用nn里面的损失函数模块就可以计算损失函数
![[Pasted image 20230331154625.png]]
模块里面有很多有用的损失函数
![[Pasted image 20230331154657.png]]
然后直接进行反向传播
![[Pasted image 20230331154735.png]]
pytorch中的potim模块
![[Pasted image 20230331154754.png]]
这里的adam优化器,第一动量是momentum,第二动量是rmsprop
![[Pasted image 20230331154855.png]]
这里可以更新优化参数
![[Pasted image 20230331154918.png]]
第三个封装是很多神经网络的层
![[Pasted image 20230331155008.png]]
首先是初始化定义集合函数值
![[Pasted image 20230331155032.png]]
进行前向传播
![[Pasted image 20230331155102.png]]
实例化这个模型
![[Pasted image 20230331155126.png]]
这这里设置了一个parallelblock
![[Pasted image 20230331155201.png]]
在sequential中堆叠两个模型
![[Pasted image 20230331155249.png]]
![[Pasted image 20230331155321.png]]
这是一个高效的利用方式,对于计算机视觉
![[Pasted image 20230331155403.png]]
pytorch还可以使用一些预训练模型
![[Pasted image 20230331155434.png]]
![[Pasted image 20230331155443.png]]
计算图可视化
![[Pasted image 20230331155459.png]]
pytorch是一种动态计算图
![[Pasted image 20230331155516.png]]
是一边进行前向传播一边构建动态计算图
![[Pasted image 20230331155552.png]]
这样的话不是特别高效
![[Pasted image 20230331155631.png]]
静态计算图是可以构建好计算图随时调用
tensorflow早先版本是用的计算图,2.0之前
![[Pasted image 20230331155804.png]]
![[Pasted image 20230331155828.png]]
![[Pasted image 20230331155929.png]]
左侧为动态图的版本,定义前向传播过程和喂数据进去在原来是两个过程,在新版本是合并了
![[Pasted image 20230331160043.png]]
![[Pasted image 20230331160125.png]]
把numpy的array变成tensorflow的tensor
![[Pasted image 20230331160156.png]]
用tf.gradienttape进行动态计算图构建
![[Pasted image 20230331160237.png]]
![[Pasted image 20230331160254.png]]
就构建图中所示的过程直接构建
最后进行反向传播
![[Pasted image 20230331160320.png]]
![[Pasted image 20230331160608.png]]
训练迭代50次,都是放在迭代图中的上下文管理器中
![[Pasted image 20230331160650.png]]
采用的也是均方误差损失函数
![[Pasted image 20230331160733.png]]
keras封装了高层的库
![[Pasted image 20230331160810.png]]
首先实例化一个sequential模型,用model.compile就可以制定损失函数,优化器等,model.fit可以训练模型
![[Pasted image 20230331161430.png]]
这里动态图的表现比静态图表现更好
![[Pasted image 20230331161522.png]]
tensorflow有一个可视化平台
![[Pasted image 20230331161612.png]]
![[Pasted image 20230331161645.png]]
![[Pasted image 20230331161655.png]]
静态图可以合并卷积层,构建后不需要源代码
![[Pasted image 20230331161725.png]]
![[Pasted image 20230331161737.png]]
动态网络可以运用于循环神经网络
![[Pasted image 20230331161807.png]]
递归神经网络更加复杂,可以接受上上层的输入
![[Pasted image 20230331161859.png]]
这种模块化网络需要动态计算图
pytorch是于caffe2集合在一起的
底层是C++的高性能运算,和python结合在一起,又方便理解,但是又运行的快速
![[Pasted image 20230331162130.png]]
底层实际是c++的内容
![[Pasted image 20230331162212.png]]
ONNX可以在个框架下的模型在其他的框架模型
![[Pasted image 20230331162241.png]]
