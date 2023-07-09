sigmoid函数适合probability和RGB的重建
但是这个函数涉及到梯度弥散的情况
Tanh函数是区间范围更大的sigmoid函数
也会存在梯度弥散的现象，在RNN中使用的更多
![[Pasted image 20230707225046.png]]

ReLU函数，阈值小于某一个值就不响应，解决了一定程度的梯度弥散情况
大于0的部分一定不会出现梯度弥散
![[Pasted image 20230707225242.png]]

Leaky ReLU函数，改进了x小于0的时候
将小于0的部分添加了一个很小的斜率
![[Pasted image 20230707225326.png]]

![[Pasted image 20230707225602.png]]

SELU函数，一种更加光滑的曲线，是两种函数的concat
![[Pasted image 20230707225647.png]]

softplus函数，将ReLU函数在0附近有一个平滑的过度
![[Pasted image 20230707225736.png]]

GPU加速
![[Pasted image 20230707225757.png]]
定义device
这里的数字是第几张显卡，如果有8张显卡，这里可以有0-7八种选择
推荐使用to方法，老版本是cuda方法

.to()方法返回一个reference
data返回的data是不一样的东西，net返回的是一样的东西，这代表的是back propaganda的时候产生的tensor有几个
![[Pasted image 20230707230242.png]]
