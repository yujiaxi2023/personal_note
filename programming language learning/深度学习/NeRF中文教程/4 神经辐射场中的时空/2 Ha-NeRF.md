如何处理遮挡问题
在二维上先遮挡掉前景 也就是一个mask部分
![[Pasted image 20230722151821.png]]
然后黑色部分做loss
mlp更喜欢一个拟合 cnn是喜欢一个泛化的工作
![[Pasted image 20230722152212.png]]

如何处理appearance，使用一个CNN学习，因为场景是可以泛化的，光影或者什么别的环境光等等

![[Pasted image 20230722152545.png]]
制造新的图像，使用CNN提取的appearance的特征造出来图片，然后继续提取特征，计算loss就可以进行解耦

![[Pasted image 20230722152736.png]]
![[Pasted image 20230722152834.png]]
![[Pasted image 20230722153049.png]]
可以看到这个中晚霞慢慢的消失的效果
![[Pasted image 20230722153244.png]]
CNN训练的时候会得到仅仅有场景appearance的特征
![[Pasted image 20230722153346.png]]
使用不同艺术风进行渲染
这个考虑的更多是光影变化

![[Pasted image 20230722153631.png]]
nerf在数据量比较大的时候会训练的很慢

![[Pasted image 20230722153837.png]]
![[Pasted image 20230722154235.png]]
可以解耦开各种变量之后可以改变这个光照或者各种元素
![[Pasted image 20230722154346.png]]
