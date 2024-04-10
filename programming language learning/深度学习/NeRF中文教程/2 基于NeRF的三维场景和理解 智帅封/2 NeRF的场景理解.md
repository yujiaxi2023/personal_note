![[Pasted image 20230722130340.png]]
nerf并不具备泛化能力，一个输入对应一个输出
GRF或者一些工作在增强这个泛化能力
在相机位置不准确的时候如何渲染nerf也是一个解决的问题

![[Pasted image 20230722130617.png]]
cnn和slam系统后端进行一个融合
nerf和语义信息结合 iLabel也是一种交互式的方式

![[Pasted image 20230722130758.png]]
NeSF可以进行语义分割
semantic-NeRF是2D分割
![[Pasted image 20230722130901.png]]
左边图像的resolution很低，但是生成的semantic的分割性能很好
![[Pasted image 20230722130956.png]]
现实中如果有相似纹理和几何信息 大概包含一致的于一标签

语义信息需要的预定义的标签，但是这个标签可能会包含有不同的解释
![[Pasted image 20230722131237.png]]
![[Pasted image 20230722131304.png]]
只是在原结构中添加了一个semantic head
这个只跟xyz有关，但是和视角关联不大
![[Pasted image 20230722131405.png]]
如果将原来的color转换为一个语义信息，就可以进行分割任务
![[Pasted image 20230722131453.png]]
是计算于一误差和color误差
![[Pasted image 20230722131526.png]]
![[Pasted image 20230722131605.png]]
可以有不同的输入数据
![[Pasted image 20230722131625.png]]
![[Pasted image 20230722131710.png]]
![[Pasted image 20230722131721.png]]
这就是输出的结果
![[Pasted image 20230722131902.png]]
稀疏性越大sparsity ratio越大
![[Pasted image 20230722132021.png]]
softmax计算的信息熵就有比较高的entropy较高的不确定性
![[Pasted image 20230722132126.png]]
![[Pasted image 20230722132133.png]]
在原图中添加噪声恢复的语义标签是一样可以识别出来
但是噪声会影响到信息熵

real world数据集上面会因为光照不同产生的分割效果不同
![[Pasted image 20230722132631.png]]
对某一个物体进行语义扰动，但是最后的输出结果还是原来的内容，但是这样会产生很多的不确定性，交叉熵增大

![[Pasted image 20230722132744.png]]
从低分辨率转换为高分辨率的标签
coarse label提供了一个稠密，但是插值位置不准确的标志
sparse label提供了一个稀疏，到那时插值位置准确的标签
当进行8倍下采样的时候
![[Pasted image 20230722132933.png]]
结果如上图表示
只要标签是精确的，这个训练结果就可以是正确的
![[Pasted image 20230722133022.png]]
![[Pasted image 20230722133209.png]]
使用每一个类提供一个像素进行训练，得到的最后结果也是可以的，还有1%的和5%的情况
![[Pasted image 20230722133413.png]]

![[Pasted image 20230722133532.png]]
传统的bayesian fusion是像素级别的融合，可以提升CNN预测
![[Pasted image 20230722133647.png]]
![[Pasted image 20230722133846.png]]
使用180张图片进行语义分割

![[Pasted image 20230722133902.png]]
三维角度注入语义信息
