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
对于为什么使用layer norm更好，有别的文章解释

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
![[Pasted image 20230626143702.png]]

**multi-head**
原文中显示，与其将key和query做h次的函数计算
不如将key和query投影到h维度做一次计算
然后再反向投影回来
将value key query都投影到线性层d维度
这时候三个值都有对应的参数W可以对应
将学习到的参数相乘然后使用attention机制
因为这个是模仿CNN的多输出通道的好处，所以这里使用的M是8，也就是8头的attention
这里就是投影8次，也就是8头的意思
规定了最后输出的MLP维度为512，所以512/8 = 64
所以每次投影到64维度，连续操作9次
![[Pasted image 20230626150140.png]]


**transformer中如何使用attention**
![[Pasted image 20230626150237.png]]
编码器输入时n个长为d的向量
注意力层有3个输入时key value 和query
为什么称之为自注意力机制，就是因为输入的值作为value key 和query三个值
对于每一个query都会计算一次
输出就是输入的每一个value的加权和
这是不考虑投影的状况和多头的情况
考虑投影和多头，就会计算多个h层投影进行比较
![[Pasted image 20230626150610.png]]
上图表明了当query 和 key 相近的地方采取的权重应该时最大的，对于最后的output 的影响也是最大的

解码器也是self attention
区别在于有一个mask，不会注意后边的一些东西

第三个attention不是自注意力，这里的key 和value时编码器的输出
解码器的第一个self attention输出query
这里因为key 和query时来自两个不同输入的数据
所以需要比较两者的相似度，还是相似度越高的权重越重
例如hello world 就是左边的编码器的输入
你好世界为右边的解码器的输入
如何将hello world对应上你好世界
在看到”你“这个字符的时候会跟hello的encode 比较相近
看到”好“的时候也是和hello比较相近
所以最后就会out put出对应的结果
也就是你和好两个字会对hello这个输入给到一个比较大的权重
而不是对于world 给出一个比较大的权重
这样才能翻译正确

**feed forward**
是一个全连接层
position-wise的意思就是每一个字符就对应一个MLP
![[Pasted image 20230626151509.png]]
这里就是两个线性层
先计算的是将输入的512dimension的tensor进行线性层的计算升维
然后外套一个线性层将其降维回到512dimension

现在用一个单头的为例
输入的是各种不同长度的tensor
经过attention后得到的是同样长度的输出
attention就是对于输入的value进行加权
然后经过相同权重的MLP
然后得到一个transformer的输出
经过attention之后，在输出的模块中已经抓取出来我感兴趣的数据到一个中间模块中
![[Pasted image 20230626152158.png]]

对比RNN是如何操作
输入数据
经过MLP层
在经过第二个输入的时候，将上一层中的MLP输出的数据一起进入到新的MLP层中，这样就能够进行时序信息的传递
![[Pasted image 20230626152206.png]]

可以看到到两个模式的区别就是使用序列的方式不一样
RNN中前一个跟后一个的输入关联性强，这代表在短期内，或者增加了长短期记忆后可以选择相关性高的词汇
Transformer中则是将所有的全局信息加入，不管两个相隔多远，只要是被注意力机制学习到的都可以视作翻译的结论之一

在attention中没有时序信息
但是在transformer中将输入的信息中添加了一个position的信息，也就是在第一个encoder中加入对应的position的信息

在计算机中是用一个32bit或者64bit的来表示一个数字
使用一个32位向量来表示一个数字
在文中是使用512位向量来表示数字
也就代表这个512位向量是123456位的位置信息

**为什么使用self attention**
![[Pasted image 20230626153713.png]]
解释一下3个指标
第一个计算复杂度
第二个顺序计算，代表前边一个计算和后边一个计算中间需要等多少次，计算一个layer的过程中，越低代表计算复杂度越低
第三个就是一个信息从一个数据点到另一个数据点的距离位多少

n是序列的长度，d是向量的长度
self attention中是key 和 query相乘，key 和value 都是n x d的矩阵tensor
所以结果就是n平方d，这就是算法复杂度
矩阵里面计算所以sequential很低
最长的距离因为query和key每一个都要给对应相乘，只是权重不同罢了，所以距离为1

在recurrent中，序列长为n的话就是每个每个进行计算，所以你取得d就决定了算法复杂度
这个是长为n的序列化操作，所以需要等待n次计算才能得到结果，最开始的数据和最后的数据中间相隔很长 

self attention的优势是在处理长数据上效果更好

问题在于使用transformer模型进行计算的计算成本比较高
![[programming language learning/深度学习/Tramsformer/论文精讲李沐/1706.03762.pdf]]