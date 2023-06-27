从直观上来说
现在sigmoid函数在小于4和大于4的很大范围内都是接近0和1的值
中间的变化非常小难以检测
有梯度弥散的情况
所以需要尽量把数据集中到一个有效范围内
所以这时候使用normalize的操作集中到0的附近小范围变动
![[Pasted image 20230510134559.png]]

![[Pasted image 20230510134710.png]]
可以通过这个图看
如果w1 和 w2 的数量级不接近
这样在梯度下降的时候就会拐弯绕远路
如果是接近圆形，不管从什么方向都可以快速的找到全局最低点

**feature scaling**
有两种
- image normalization
```python
normalize = transforms.Normalize(mean=[0.485,0.456.0.406], std=[0.229,0.224,0.225])
```
图片数据保存时0-255 浮点型数据
所以我们需要normalize数据
这个数据通过image net统计得来的一个数据
就给图片赋值为这几个RGB 和标准差
使用这几个数据可以更好的满足normalize后的数据

- batch normalization
batch normalization就是一个batch中的所有图片 所有像素求一个normalization
形成一个channel
![[Pasted image 20230510135623.png]]
这个例子就是
6张3channel图片HW分别为28

就是将batch中的图片 channel height width这些分别进行组合
然后合并在一起做正则化，也就是打散再相对应的分配

主要解释batch normalization
现在一个batch中存在6张图片 3个 channel 一个channel时784个pixel
将 6张图片和784个像素在一起做一个统计数据
形成一个μ和方差
![[Pasted image 20230510141059.png]]
![[Pasted image 20230510141123.png]]
使用得到 的均值和方差跟每个元素进行缩放操作让其符合正则化分布
![[Pasted image 20230510141158.png]]
![[Pasted image 20230510141206.png]]
使得分布在0的附近波动

额外进行一个处理
![[Pasted image 20230510141258.png]]
![[Pasted image 20230510141303.png]]
这里的μ和σ是不需要梯度信息的，因为是直接从输入数据中统计出来的
但是后边一个操作需要能梯度下降

```python
x = torch.rand(100, 16, 784)

layer = nn.BatchNorm1d(16)
out = layer(x)
```
这里是因为直接把28x28变为了一个784的行
所以是1d的batchnorm
这里就会记录16个channel的均值和方差
运算后会更新一个全局running_μ 和 σ²
```python
layer.running_mean # μ
layer.running_var # σ²
```
均匀分布的均值是0.5
方差是1

规范化的写法pipeline
![[Pasted image 20230510142348.png]]
这就是一个标准的train的行为
![[Pasted image 20230510142417.png]]
要注意这些参数都是要随着计算更新的

```python
x.shape
layer = nn.BatchNorm2d(16)
out = layer(x)
layer.weight
layer.weight.shape
layer.bias.shape
```
均值和方差只能查看全局的 使用running_的方式
![[Pasted image 20230510142834.png]]

打印当前layer的所有参数
```python
vars(layer)
```
![[Pasted image 20230510143017.png]]
test 和 train里是不一样的
因为test一般都是一个数据 没法统计全局的μ和σ
并且γ和β是不更新的
![[Pasted image 20230510143301.png]]

在test数据中
```python
layer.eval()
BatchNorm1d(16,eps=1e-05,momentum=0.1,affine=True,track_running_stats=True)
out = layer(x)
```
![[Pasted image 20230510143419.png]]

进行可视化
使用了batchnorm之后收敛速度加快，精度也会提高
![[Pasted image 20230510143503.png]]
原来的方差 和均值的变化
可以看到明显的变小了
![[Pasted image 20230510143636.png]]

batchnorm的优点
- [ ] 收敛速度快
- [ ] 容易得到最优解
- [ ] 更稳定了 参数调整比较方便