### locate 查询本地有哪些文件 比find好用 但是是需要有一个缓存文件 作为目录查找
```
yum provides locate

yum install mlocate.x86_64 -y

```

![[Pasted image 20231218223439.png]]
这个问题是还没有生成一个缓存
所以locate无法查找这个缓存文件
```
updatedb
locate 文件名
```
不是时时刻刻生成缓存文件
而是隔一段时间生成一个
find是实时查找

### sgid权限
对于locate这个命令
我们首先查看这个locate执行的对象
mlocate.db

```
ll /var/lib/mlocate/mlocate.db
```
![[Pasted image 20231218223822.png]]
可以看到属于用户组slocate

这个时候我们查看locate 命令
```
which locate
ll /usr/bin/locate
```
![[Pasted image 20231218223858.png]]
会发现它们同属于用户组slocate

这个时候如果我更改组的执行权限
```
chmod g-x /usr/bin/locate
ll /usr/bin/locate
```
![[Pasted image 20231218223947.png]]

所以普通用户执行文件的时候是可以执行相同的用户组的文件权限的
也就是读权限
![[Pasted image 20231218224308.png]]

这个sgid其实就是只涉及到读权限,所以并没有多大用
是针对命令文件设置的

```
stat /usr/bin/locate
```
![[Pasted image 20231218224654.png]]
这里的权限显示的是2 sgid

### sticky 粘滞位权限
唯一的例子是tmp目录
```
ll /|grep tmp
```
![[Pasted image 20231218224928.png]]

现在我设置一个谁都可以写文件的目录
```
mkdir /data
chmod 777 /data
ll /data
```
![[Pasted image 20231218225415.png]]

这时候我们可以看到
这个data文件里面的文件时任何一个用户都可以删除的
```
rm -fr root.txt
```
![[Pasted image 20231218225505.png]]

为了保护每个文件的权限,也就是让只有这个用户创建的文件可以由自己用户和root用户删除
我们需要加一个粘滞位权限
```
chmod o+t /data
```
注意这里就是+给other权限位置,而且也和执行位置重合
这时候/data就无法删除其他用户文件
![[Pasted image 20231218225731.png]]
粘滞位的权限是1