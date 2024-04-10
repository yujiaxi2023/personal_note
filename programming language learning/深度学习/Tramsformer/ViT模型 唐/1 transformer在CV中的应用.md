将图片转换为矢量之后直接应用
![[Pasted image 20230717170447.png]]
transformer是将输入序列进行特征提取
![[Pasted image 20230717170636.png]]
q 和 k 一个是查找别人的向量 ， k 是代表被查找的向量
v代表的是输入向量的特征
这里面a是代表qk相乘点积
![[Pasted image 20230717170847.png]]

ViT的architecture
![[Pasted image 20230717171033.png]]
输入一个图像，图像拆分为patch，进行标号
将每个窗口图片进行embedding 变为一个300长度的向量
进行一个全连接层映射到一个1024维度或者是别的维度
![[Pasted image 20230717171440.png]]

将位置进行编码
有三种形式
- 不使用位置编码
- 使用数字编码
- 使用位置横纵坐标编码
![[Pasted image 20230717171841.png]]

这个ViT使用的是分类任务
这里0会跟所有的后边的相乘
![[Pasted image 20230717172213.png]]
所以分类任务，只用将0这个地方做FFN做分类

物体检测任务会使用到decoder
![[Pasted image 20230717172404.png]]
