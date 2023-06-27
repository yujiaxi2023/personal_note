![[Pasted image 20230522150219.png]]
实现上图中神经网络需要下面的代码
![[Pasted image 20230522150400.png]]

逻辑回归过程
第一步是定义使用什么方式链接输入x 和 参数w 和 b
![[Pasted image 20230522150650.png]]
第二步是确定loss  和 cost function cost 和loss 区别在于例子个数 loss 是一个例子 cost 是加和之后求平均
![[Pasted image 20230522150730.png]]
第三步是训练数据到最小的cost function
![[Pasted image 20230522150832.png]]

对应到代码中的任务是
第一步构建前向传播的动态图模型
![[Pasted image 20230522150938.png]]
第二步时构建损失函数
![[Pasted image 20230522150956.png]]
最后一步时训练减少cost function
![[Pasted image 20230522151022.png]]

拆解上述的代码
![[Pasted image 20230522151057.png]]
第一步输入各种库
第二步建立前向传播模型中
![[Pasted image 20230522151141.png]]

建立损失函数
对MNIST数据集的手写数字分类中
我们使用交叉熵损失函数
![[Pasted image 20230522151301.png]]
这个代码时指定一个loss 的计算过程

如果你需要实现一个regression 问题，一般使用均方误差函数
![[Pasted image 20230522151422.png]]
cost 函数可以写作
![[Pasted image 20230522151544.png]]

接下来就是梯度下降过程
![[Pasted image 20230522151627.png]]
也就是重复下列计算过程
![[Pasted image 20230522151648.png]]
反向传播可以帮助你计算这个过程
![[Pasted image 20230522151730.png]]
通过调用上述的模块进行
