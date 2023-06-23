![[Pasted image 20230303184514.png]]
结论一
普通的神经网络，例如图中，如果输入一张图片猫，然后将他encoder 然后转变成一个 hidden representation Z 然后再将Z decoder到一个尽可能相近的图片，而在variational auto encoder中，中间量Z，会被拆解为，例如中间的Z 有6个变量，然后会将头两个变量去做parameterize 一个做平均，一个做标准差，进行高斯分布Gaussian，然后六个维度变成3个gaussians，然后需要sample出一个三维向量，然后再反馈到decoder

![[Pasted image 20230303185343.png]]
结论二
这里介绍的一种VQ-VAE训练方式，是将encoder训练出一个h向量，然后通过这个h向量找到一个code book中最近的那一个向量，然后再decoder，这里的三个步骤都是经过训练的
![[Pasted image 20230303190354.png]]
这里是描述整个过程中的损失情况，首先是reconstruction的损失，Xt是原图像，然后D(ezt)是隐藏量化表示的decoder，是一种标准重建损失，第二部分是codebook loss，这里的训练是让你的code book的向量更接近于actual hidden representation，目的是为了让你的code book vector更加接近于你输入的vector，最后一部分是commit loss，这是让encoder的vector能够近似映射到code book中的vector，不然中间就没有信息流动，这部分的损失就是commit loss
![[Pasted image 20230303190711.png]]
![[Pasted image 20230306122336.png]]
会把源文件encode变成不一样的色块，然后将这些色块进行向量转化，对应到训练后的code book中，然后generate出后边的白色的色块，重新生成一段内容
![[Pasted image 20230306124836.png]]
![[Pasted image 20230308155613.png]]
他是分为三层进行generate的