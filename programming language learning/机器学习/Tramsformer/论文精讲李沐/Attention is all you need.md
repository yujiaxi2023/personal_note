谷歌公司发布的一篇很重要的深度学习基础文章
模型任务专注于BLEU在机器翻译的任务上的提升
它使用的是纯self attention的模型架构
所以可以看出这个架构最开始是在一个小的领域使用的

原本的RNN模型用于机器学习的时候需要时序性的输入，所以在时序上无法并行，并行度较低的时候模型在计算机的表现上比较差
如果使用每个时间点的ht会让内存你占用很大

attention在RNN上的应用
attention是并行度比较高的，导言中比较短，就是摘要的添加

使用卷积神经网络替换循环神经网络，在卷积的问题就是很难应用到很长的输入对象
使用transformer可以将两个相隔很远的像素运用同一条序列输出
卷积的好处是可以输出多个输出通道，一个输出通道可以认为是识别一种特征
使用多头multi-head attention可以进行部分替代

self attention机制，memory network的工作

model architecture
encoder-decoder 的架构
将x1 到 xn个输入，变为一个一个z1 到 zn，zt表现为一个xt的向量表示
这是一个编码器

解码器是一个个生成的自回归模型
给定一个z1生成一个y1，然后y1可以生成y2，这就是自回归模型
![[Pasted image 20230626100902.png]]
这块就是编码器的结构
![[Pasted image 20230626100930.png]]
这就是解码器的输入
N代表是N个层
一个多头注意力机制，一个前馈神经网络MLP，中间要给残差连接，然后normalization
编码器和解码器的差别就是模块中间添加了一个多头注意力

**编码器**
使用了6个一样的层
每个层有一个sublayer
一个注意力机制，一个MLP
![[Pasted image 20230626101314.png]]
这就是输入层的公式，是残差连接的表现
这个模型使用的是固定的dimension

layer Norm 
batch norm 减去均值除以方差就是normalization 就是 将feature进行这个操作
这就是batch norm
![[Pasted image 20230626101630.png]]

layer norm 就是将batch norm转置
![[Pasted image 20230626101659.png]]

因为RNN和CNN输入时一个三维的数据
所以
![[Pasted image 20230626101757.png]]
蓝色时batch norm 黄色时layer norm
![[Pasted image 20230626101835.png]]
就是对矩阵的norm操作不一

因为每个feature 含有的数据不一样，例如图像，在预处理后的图像有的地方的数据为0，所以batch norm中经过计算的数据可以表示为
![[Pasted image 20230626102031.png]]
同样，layer norm的表示
![[Pasted image 20230626102044.png]]
对于为什么使用llayer norm更好，有别的文章解释

**decoder**
使用了6个层
这里使用的是自回归的方式
是一个带掩码的注意力机制
不会注意到后边的内容而是前面的内容

**attention**
output是value的加权平均
加的权重是key和query
权重是query和key的相似度
![[Pasted image 20230626102618.png]]
如果给出的query跟前面的key比较像，就会是黄色
如果是跟后边比较像就是绿色

**原文中使用的attention机制**
点乘两个向量，如果是正交就是0，越大相似度越高
query和key的长度相等，两个向量内积
除以根号dk
使用softmax函数
实际中的计算Q是一个矩阵包含有很多个query
K包含有很多个key
两者每一个值是等长的但是包含的个数是不同的，所以可以转置做乘法

两种常见的注意力机制 additive attention 和 dot-product attention
前者可以计算不同长度的query和key
后者可以应用于同样长度的query和key

如果直接使用dimension的值计算的结果会出现梯度弥散的现象，所以使用更好缩小变化，让梯度变到可以计算的程度

在注意力机制中kt会跟所有的q相乘计算，但是transformer中不能够关注t时间之后的信息，所以需要mask掉kt之后的乘积结果

操作方法就是将qt和kt之后计算的值直接替换成一个很大的负数例如-1e的十次方
softmax之后就会变为0


**multi-head**
