NeSF需要一些计算成本
SLAM是一个实时交互式的work
![[Pasted image 20230722140935.png]]
imap是一个完全基于nerf的slam的工作
![[Pasted image 20230722141000.png]]
有深度map的时候训练时间会大大加快

如何估计相机姿态这也是一个重要工作

![[Pasted image 20230722141128.png]]
这个表征过程是很高效的，相比于原来的工作，有对于没有扫描的内容有很好的泛化的功能，这是使用nerf运用于slam的工作

![[Pasted image 20230722141240.png]]
imap中加入语义信息，有一个定制化的三维结果
![[Pasted image 20230722141322.png]]
这是一个2015年完成的一个工作，用户的输入可以对现实场景进行理解，系统会通过svm和随机场进行扩散，形成一个分割的效果

iLabel
加入用户指导，然后交互的告诉一个内容语义，然后就可以将像素级别的标注扩散到房间中
![[Pasted image 20230722141622.png]]
使用鼠标点，然后输入语义信息就可以形成一个表示
![[Pasted image 20230722141740.png]]
![[Pasted image 20230722141810.png]]
这个也是进行svm分类
![[Pasted image 20230722141941.png]]
这个过程中可以进行定位加网络的自动化，只需要标注就可以了

![[Pasted image 20230722142039.png]]
![[Pasted image 20230722142117.png]]
通过3个神经元就可以分为不同的层次
![[Pasted image 20230722142257.png]]
对于一些简单小物体的检测
![[Pasted image 20230722142316.png]]
![[Pasted image 20230722142338.png]]
![[Pasted image 20230722142432.png]]
![[Pasted image 20230722142653.png]]
