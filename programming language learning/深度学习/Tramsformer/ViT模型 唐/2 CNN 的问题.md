卷积需要扩大感受范围就需要更深的网络
例如使用的kernal size 是3的时候
感受到的特征就很小
如果需要感受更大的范围，需要更多的卷积层不断地整合特征
![[Pasted image 20230717172755.png]]
transformer中的感受野第一层就很大

![[Pasted image 20230717173332.png]]
输入的patch图像块，转换为特征输出，然后用全连接变为另外的维度
P代表的是有多少个图像块
![[Pasted image 20230717173638.png]]
+1代表的是额外准备的一个位置编码，为了输出的时候计算FFN的时候用
输入为
![[Pasted image 20230717173727.png]]
做一个tensor的加法，位置都是互相对应的
然后经历一个多头注意力 配上残差
然后做MLP做残差
然后重复
![[Pasted image 20230717173902.png]]
![[Pasted image 20230717173934.png]]

多头中有部分关注的范围比较小，有点关注的比较大范围
到了一定层次之后关注的范围都很大
![[Pasted image 20230717174141.png]]
![[Pasted image 20230717174257.png]]
做编码和不做编码有区别，但是无论如何编码，结果相差不大
![[Pasted image 20230717174639.png]]

Transformer in Transformer
ViT中一个patch是16 x 16，信息量比较多，可以继续在细分就是TNT
外部和内部的transformer分开
外部的处理跟刚才一样
内部的transformer不一样
![[Pasted image 20230717175202.png]]
![[Pasted image 20230717175355.png]]
![[Pasted image 20230717175509.png]]
将内外部的向量整合为同一维度，然后相加即可
![[Pasted image 20230717175615.png]]
内外部都需要添加位置编码
![[Pasted image 20230717175705.png]]
特征可以分的更开更明显，T-SNE是压缩到二维的图像中看特征之间的距离关系
