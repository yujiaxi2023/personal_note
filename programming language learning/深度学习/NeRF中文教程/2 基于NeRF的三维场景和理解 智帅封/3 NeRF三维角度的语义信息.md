general radiance field GRF
pixel nerf
使用CNN（transformer？）的特征增强泛化能力
如何将先验注入到nerf中

使用CNN 的预测照片进行噪声添加可能更具有意义
现在是一个过拟合的任务
现在很sharpe的边缘会因为nerf采取的全局特征变得smooth

NeRF的优点就是在于过拟合
nerf可以生成带纹理的mesh，但是一般使用的是生成体素，但是打光等内容直接rendering并不好

NeSF（facebook的工作）
![[Pasted image 20230722135433.png]]
使用大量的pre train获得先验信息
将RGB转换为要给density map 然后用一个unet转换为semantic field

![[Pasted image 20230722135553.png]]
这个语义信息是变为三维之后给与的
![[Pasted image 20230722135645.png]]
![[Pasted image 20230722140628.png]]
![[Pasted image 20230722140650.png]]
提取出的内容比较好的
![[Pasted image 20230722140708.png]]
有比较好的泛化能力
