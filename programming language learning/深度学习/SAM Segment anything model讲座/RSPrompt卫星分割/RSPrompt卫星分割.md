![[Pasted image 20230815065708.png]]
原始的SAM模型
prompt提示的分割任务
![[Pasted image 20230815072036.png]]
一种交互式的设计，提供点或者方框，或者粗粒度的分割，或者文本
就可以进行分割任务
![[Pasted image 20230815072318.png]]
利用SAM进行标注的改进
SAM比较依赖先验的人工指导

![[Pasted image 20230815072521.png]]
复杂背景容易对分割任务产生泛化性的削弱


![[Pasted image 20230815072609.png]]
因为SAM是基于先验的人工知道，和无分类类别的任务
所以不适合全自动的一种图片理解任务
![[Pasted image 20230815072700.png]]
复杂背景的情况下，很可能难以分割出来完整的物体，需要经过精细化设计才能够获得一个合适的prompt

![[Pasted image 20230815072837.png]]
生成prompt的信息来源是哪里
采用ViT的backbone的中间层的特征，用一个轻量特征聚合器来形成特征

使用什么样的prompt更合适，点 框 或者 粗粒度的mask
输出采用的是生成prompt embedding，不是采用坐标

![[Pasted image 20230815073251.png]]
SAM是一种交互式的分割方法
图像编码器 提示编码器 和mask decoder
使用transformer来进行特征的交互

SAM-segmentation
是利用SAM的backbone的信息
基于mask2former 或者 maskrcnn的头进行转接到decoder得到mask
![[Pasted image 20230815073513.png]]

SAM-classification
先使用一个完整SAM进行所有内容分割之后，得到多个实例的mask
然后使用分类器进行分类，如果使用CLIP就是一个zero shot的例子
![[Pasted image 20230815073631.png]]

SAM-detection
先经过一个目标检测器，得到位置和类别，然后将目标送入一个完整的SAM
这里类似于一个细粒度后处理的工作
![[Pasted image 20230815073725.png]]

RSPrompter
![[Pasted image 20230815073740.png]]
使用冻结的encoder 获得中间的语义信息的特征和encoder的特征
使用轻量级的特征聚合器得到稠密的特征图
通过prompter获得prompter embedding和类别
进入decoder中可以得到mask

![[Pasted image 20230815073944.png]]
从中间层下采样，获得一个小的特征图，使用残差连接获得一个聚合特征

![[Pasted image 20230815074053.png]]
使用RPN head获得一些特征
然后经过Rol Pooling得到一些特征向量
最后接一些功能头
原始的prompt是将坐标经过傅里叶变化获得高频表达
如果使用mlp就需要使用sin来表达

![[Pasted image 20230815074503.png]]
损失函数是使用了多种损失联合

![[Pasted image 20230815074534.png]]
query-based prompter
flatten之后形成一些token

![[Pasted image 20230815074640.png]]
使用了匈牙利匹配算法使用loss 
![[Pasted image 20230815074803.png]]
使用的分类数据集和大小

![[Pasted image 20230815074851.png]]
SOTA比较
在小数据集中有比较好的泛化能力

![[Pasted image 20230815075304.png]]
对于mask decoder 中使用的内容是比较多的计算
收敛速度比较慢，因为使用transformer的架构，所以输入的是一条，进行cross attention或者self attention就比较耗费资源

![[Pasted image 20230815075542.png]]
FastSAM
![[Pasted image 20230815075603.png]]
MobileSAM

![[Pasted image 20230815075706.png]]
去耦合的方式

![[Pasted image 20230815075808.png]]
基于vision text的模型CLIP模型 进行融合

![[Pasted image 20230815075952.png]]
