![[Pasted image 20230626200316.png]]
3类应用模型
区别在于应用的端

![[Pasted image 20230626200433.png]]
这里的三个句子分别代表的是
第一个句子是编码端输入的德语句子，将要翻译这个句子
第二个是解码端的输入
第三个是ground truth

![[Pasted image 20230626200552.png]]
整体的运行模式如上图
![[Pasted image 20230626200713.png]]
对应的这个代码中的例子为上图

这里的特殊字符P S E代表的是？
S代表start E代表end P代表填充字符pad字符
这里的batch size 是1
正常的情况并不会只包含一个batch而是很多的batch
![[Pasted image 20230626200856.png]]
会设置一个最长的字符数量，不足的输入就会添加pad填充空白部分

teach forcing
保证训练的时候会mask掉后边的部分

![[Pasted image 20230626201241.png]]
这是在构建编码端的词表
![[Pasted image 20230626201305.png]]
解码端的此表
![[Pasted image 20230626201315.png]]
两者的长度
![[Pasted image 20230626201325.png]]
这里就是transformer原文中的一些超参数

接下来是模型部分
![[Pasted image 20230626202107.png]]
最开始是初始化类中定义三个部分，编码解码和投影
projection是用softmax函数判断哪一个输出的可能性最大
decoder输出的512dimension的tensor需要投影，这里是反向投影到词表的大小，然后使用softmax

前向传播的是接受两个输入
encoder的输入和decoder的输入
![[Pasted image 20230626202455.png]]
![[Pasted image 20230626202532.png]]
这里是encoder的最终输出，也就是key 和 value的部分
![[Pasted image 20230626202728.png]]

![[Pasted image 20230626202836.png]]
这里是decoder的输入和输出
![[Pasted image 20230626202904.png]]
然后就是输入到projection中


接下来是encoder部分代码
![[Pasted image 20230626203738.png]]
首先是embedding这个输入的词向量

然后设置position encoding 位置编码
![[Pasted image 20230626203805.png]]

![[Pasted image 20230626203855.png]]
这是使用n个encoder层进行堆叠

这里的前向传播时
首先时字符转换为数字，然后转换为对应的向量
![[Pasted image 20230626204109.png]]

然后就i是位置编码
![[Pasted image 20230626204216.png]]
就是第一步的output进行计算

位置编码的实现
![[Pasted image 20230626204300.png]]
![[Pasted image 20230626204433.png]]
这里时实现括号内的公式
![[Pasted image 20230626204629.png]]
这里时position乘以各种部分得到的结果进行cos和sin
然后维度变化
![[Pasted image 20230626204709.png]]
![[Pasted image 20230626204715.png]]
这就是让定义的pe函数不进行更新

![[Pasted image 20230626204835.png]]
这个代码告诉从哪里开始进行pad符号填充

![[Pasted image 20230626204953.png]]
这就是一个self attention的输入的计算出来的矩阵
![[Pasted image 20230626205018.png]]
是这个公式的括号内部分

pad是句子原来不存在的，所以计算时候不能计算pad
所以需要去掉这个部分
所以需要添加一个符号矩阵，是pad的部分是1，所以就可以消除掉这个位置的影响力
![[Pasted image 20230626205237.png]]

这里的get_attn_pad_mask如何实现
![[Pasted image 20230626210218.png]]
获得解码端和编码端的输入和输出的长度，两个是不一样的长度在交互注意力层中，在自注意力中是一样的，但是都会补完为相同的长度
![[Pasted image 20230626210512.png]]
然后将pad的0的部分转换为True的符号

这里的循环时将上一层输出作为输入
![[Pasted image 20230626211339.png]]

encoderlayer的实现方式
初始化函数为前馈神经网络和自注意力的多头机制
这里的self attention是encoder layer中的自注意力过程
3个input相同，但是代表的是value key 和query
![[Pasted image 20230626211608.png]]

这里的多头注意力机制实现方式
输入的是QKV三个矩阵，也就是这里embedding后的词向量
这如果词向量的长度是4，那这里的矩阵是4个batch
![[Pasted image 20230626211822.png]]
为什么encoder layer需要有3个输入，是因为在后边的交互注意力中需要有2个来自于encoder层的输入
![[Pasted image 20230626212011.png]]
分头使用了view函数，q k矩阵的维度应该相同，否则不能够相乘

然后实现一个内积来看相关性的多少
![[Pasted image 20230626212204.png]]
![[Pasted image 20230626212217.png]]
