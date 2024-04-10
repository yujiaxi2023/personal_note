![[Pasted image 20230710105220.png]]
预测值在0.5作为分界进行输出

如果某些病症并不是很紧急，或者是机器模型出现误诊会造成严重后果，需要提高输出为1的阈值，这样可以让你的输出更加precision，但是会减少recall，你能正确检测出病人的比例减少了，但是一旦你检测出来，你的precision就很高
![[Pasted image 20230710105507.png]]
![[Pasted image 20230710105656.png]]
如果你需要检测出更多的病例，确保得病的人尽量被检测出来，误诊产生的损失较少，或者是没有检测出来结果的人会立马死，这个时候就需要提高recall，减少precision的权衡，这样需要减小阈值
![[Pasted image 20230710105720.png]]
我们通过改变threshold阈值来改变recall 和 precision
大部分的情况下precision和recall会有一个权衡会产生一个曲线，这个时候我们需要根据这个曲线进行权衡
![[Pasted image 20230710105919.png]]
但是选择阈值并不能在validation set上设定，因为那个时候你的超参数已经设计完了

引入**f1**参数
在不能明显根据precision和recall选择数据的情况下使用f1是更好的过程
![[Pasted image 20230710110239.png]]
创建F1分数是因为average并不好用
为了避免P & R过小，需要这个分数去衡量结果
harmonic mean 调和公式
![[Pasted image 20230710110446.png]]
