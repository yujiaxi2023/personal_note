图像中的噪点问题，在降采样的时候，频谱会重叠
![[Pasted image 20230721202359.png]]
一般会进行low pass filter
可以解决这个问题
![[Pasted image 20230721202447.png]]
具体的就是下面的定理
![[Pasted image 20230721202503.png]]

![[Pasted image 20230721202512.png]]
具体的表现就是上图，降采样就会bluffer一下
![[Pasted image 20230721202639.png]]
这个midnerf为了是解决不牺牲高精度的情况下，保证低精度的重建准确性
![[Pasted image 20230721203038.png]]
mipnerf就是使用low pass filter会提升这个性能

nerf的假设是物体时静态的，如果要延伸到动态场景有点难
satellite nerf可以实现卫星图像，有open source
反渲染三要素 shape material light 但是现实是户外的shape不能够很好的被简化过的sfm重现出来，如果是假设场景，人们更多的是关注图像表达的要素
soft shape reputation并不能很好的edit，所以跟传统的相比并不好
锯齿问题和伪影问题是不同情况下的问题，伪影更多是因为照片不够，resolution比较低，采样频率低就会遇到锯齿问题
nerf一般来说psnr合成数据syntactic data 30多就很好了，real scene 27 28左右

nerf关注的不应该是三维场景模型的重建，而是关注每时每刻看到的图片数据

