![[Pasted image 20230814204347.png]]
foundation model
是现代大模型的基础
当模型的体量增加的时候，可以覆盖的任务种类就更多
![[Pasted image 20230814204450.png]]
将研究使用到各个子division上
![[Pasted image 20230814204549.png]]
现在主流的是按照vision transformer的模型
![[Pasted image 20230814204922.png]]
SAM的模型设计比较简单
![[Pasted image 20230814205017.png]]
![[Pasted image 20230814205044.png]]
首先小规模人工标注
然后机器和人互相帮助进行标注
然后进行完全自动化标注过程

![[Pasted image 20230814205239.png]]
因为mask的标注时间是非常有限的，所以在很多比较精细的内容是难以识别的
![[Pasted image 20230814205326.png]]
使用一个小样本的数据集，例如44k的数据进行fine tuning，这个会让在原本的数据集上有一个提升，但是实际上会减少泛化能力
![[Pasted image 20230814205458.png]]
这是经过了高质量的encoder之后形成的分割内容
![[Pasted image 20230814205724.png]]
![[Pasted image 20230814205759.png]]
如果只是经过finetune，在对泛化之后的内容的ap下降太多了
经过小数据集训练会生成一个数据遗忘的问题
![[Pasted image 20230814210026.png]]
![[Pasted image 20230814210157.png]]
![[Pasted image 20230814210524.png]]
使用原始SAM进行分割，形成一个重建3d模型的内容
会产生一个伪影，所以原始的重建不会很好
![[Pasted image 20230814210636.png]]
![[Pasted image 20230814210652.png]]
![[Pasted image 20230814210713.png]]
SAM原始模型会产生一些伪影artifact
![[Pasted image 20230814210742.png]]
应用SAM在一个更好的精细程度上面
![[Pasted image 20230814210911.png]]
通过自己的数据集进行迁移
![[Pasted image 20230814211028.png]]
![[Pasted image 20230814211113.png]]
这是通过采样点进行传播工作
就可以通过少量的采样点进行视频内容的分割
使用0样本的方法，得到的结果都是可以的
zero-shot的方式
![[Pasted image 20230814211444.png]]
foundation model使用了大量的数据进行预训练
标注mask是比较昂贵的工作
标注点是否是一个更好的工作
![[Pasted image 20230814211626.png]]
为了得到temporal consistency通过点和windows进行local search
如果找到的内容不一样，会给出一个惩罚

现在做图像分割更关注generalizable 和 zero shot
open vocabulary的问题
用少量数据提升模型能力
