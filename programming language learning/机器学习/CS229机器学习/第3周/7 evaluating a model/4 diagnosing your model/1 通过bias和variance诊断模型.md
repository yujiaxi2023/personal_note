bias和方差在提升模型表现上常被视为关键指标
![[Pasted image 20230609182153.png]]
可以看到, 高方差和高截距都是不好的模型表现
当high bias的情况下cost function在train set和cross validation set表现都是不好,都表现的非常高
当high variance的情况下是过拟合,此时train set上面cost function很小,但是cv set上面的cost很高
中间的情况下train set 和validation set都表现的比较好
![[Pasted image 20230609191336.png]]

如果使用更多条件的模型, 这里的cost function在train set上表现会更好
在validation set上面表现是类似一个凸函数
![[Pasted image 20230609191641.png]]

如何评价模型中的bias 和 variance是一个权衡的过程,需要选择最好的条件
![[Pasted image 20230609192139.png]]
有时候是high bias和 high variance可能会同时存在
bias代表在训练集上表现不好, variance代表是交叉验证数据集的表现跟训练集表现相差太多了
