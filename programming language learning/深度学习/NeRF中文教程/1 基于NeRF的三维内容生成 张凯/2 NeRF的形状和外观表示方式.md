 ![[Pasted image 20230718210929.png]]
novel view对于real data比较困难
右边是depth map，看不到geometric quality
surface novel 在 geometric quality上看不到  level of detail
如何生成这样一段视频
![[Pasted image 20230718211211.png]]
通过28张图片train一个nerf
有了这个三维内容进行渲染一个新的图片
右边是相机视角的分布

NeRF拆分为反渲染中的三要素：shape appearance rendering
![[Pasted image 20230718211403.png]]
shape上并非是polygon或者是point cloud，而是一种软的表现方式
![[Pasted image 20230718211439.png]]
![[Pasted image 20230718211519.png]]
可以把这个过程堪称一个函数

NeRF在一个ray上 sample很多点，每个点的都有不同的颜色，然后这就是一个camera
![[Pasted image 20230718211654.png]]
![[Pasted image 20230718211739.png]]
![[Pasted image 20230718211758.png]]
这些点结合就可以得到这个ray的颜色

NeRF成功在于shape是一个虚化的shape，image loss 会在需要的地方创建三维模型。
![[Pasted image 20230718212058.png]]

过去有很多使用神经网络的，但是使用的都是hard geometry
缺点在于rending比较costly
![[Pasted image 20230718212337.png]]
优点是不存在genus 问题，不能从球变为圆圈
![[Pasted image 20230718212439.png]]
如何edit soft shape也是一个问题
![[Pasted image 20230718212501.png]]
soft shape modeling才是最重要的提高表现的因素

图片是将xy映射成RGB
实体是将xyz映射为occupancy或者是density 
NeRF映射成RGB density
overfit是倾向于拟合一个smooth 的 signal
这个不利于我们形成3d content
我们实际上需要的是sharp的novel field
![[Pasted image 20230718212950.png]]
中间添加了一个feature之后才能够生成一个保真的信号

用神经网络表示信号的方式，专业属于是neural field
- 每一个NeRF的内容大约在10MB左右，所以好处在于很方便的在网络上传输
- 场景没有discretized 是更高保真的object
- 神经网络中有一些为了smooth使用的regularization

这里的soft shape是每一个特征都在空间中占有一点点的感觉，就是类似于雾状物，所有的feature都是连在一起

NeRF一个比较好的在于输出的大小是合适的，而且效果很好，因为我们需要的是一个感兴趣的向量，也就是对应的这个雾状物体中

NeRF的density field接近物体表面不透明度比较高，内部也比较高，但是这个内部的density比较随机，因为梯度比较弱

σ代表的是光在空间中传播衰减的速度，或者这个材质对于光照的吸收速率
![[Pasted image 20230718213933.png]]

NeRF使用了一个很expensive的rendering方式，因为每条线都需要很多点的颜色组合到一起，如果每个点都需要query一个神经网络，会很慢

NeRF解决的拍摄场景
围绕物体拍摄 360 inward-facing：没有背景或者背景是白色的
![[Pasted image 20230721185629.png]]
forward-facing：单向的方向，只在一个区间内波动
![[Pasted image 20230721185636.png]]
全景图像拍摄场景
![[Pasted image 20230721185644.png]]
unconstrained 360 outward-facing：在房间内拍摄，但是相机是unregular的
![[Pasted image 20230721185652.png]]
围绕一个场景拍摄同时重建了周围的背景
![[Pasted image 20230721185803.png]]
![[Pasted image 20230721185815.png]]
因为场景延申到很远的地方，所以涉及到一个resolution的问题
因为我们rendering的是一幅图中的各处点，关键在于如何将这些点进行分布
如果是bounding cube的情况下，点的分布比较好设置
但是如果是一个没有边界的图片的时候，前景可能清晰，但是背景就很糊
如果点分布在前景背景中，前景背景就都糊了

如何解决户外的边界问题
nerf可以compositional的性质，1个ray上面sample点，这个点可以放到不同的NeRF里面，所以这个点可以放在foreground 和background上面
就是将点分前景和背景
![[Pasted image 20230721201322.png]]

但是这样还没有解决resolution的问题，2种caputure setting，用一个球将摄像机和场景分隔开，inward是外部的球，outward是内部的球，这两者有对称性
![[Pasted image 20230721201456.png]]
一种mapping的方式，可以将无边界化为cube
![[Pasted image 20230721201543.png]]
所以这样的symmetric就可以用原始的nerf来将东西转变为小的cube渲染
![[Pasted image 20230721201645.png]]
![[Pasted image 20230721201714.png]]
foreground background的划分情况
这个nerf++生成的就是这些优化
![[Pasted image 20230721201756.png]]

NeRF现在还不能线上跑
渲染出来的就是一张图片，nerf转换会掉quality，而且需要增加编辑性
