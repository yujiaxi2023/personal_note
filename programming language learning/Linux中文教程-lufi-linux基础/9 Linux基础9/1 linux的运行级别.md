运行级别0 关机
运行级别1 单用户
用于找回root密码的时候常用
运行级别2 不带网络的多用户
运行级别3 完整的多用户模式
运行级别4 保留
运行级别5 桌面模式
运行级别6 重启

### 查看运行级别 runlevel
```
[root@localhost greptut]# runlevel 
N 3
```
这是命令行的运行级别
如果是有桌面的运行级别就是5

###  切换运行级别init

```
init 6 
```
这个操作就产生和reboot一样的作用

### 单用户模式找回密码

需要在开机启动的时候进入内核编辑模式
![[Pasted image 20231218211628.png]]
![[Pasted image 20231218211655.png]]

只要电脑在手里就可以找回密码
单用户模式是不需要密码就可以进入的

![[Pasted image 20231218212305.png]]
这就进入了内核模式,这个时候不能瞎按,不然会出问题
因为瞎按都可能出现更改内容,都会导致启动不了

![[Pasted image 20231218212407.png]]
只需要把ro改成rw
![[Pasted image 20231218212446.png]]
然后删掉这部分
![[Pasted image 20231218212509.png]]
改成这个内容
![[Pasted image 20231218212531.png]]
然后这里就可以启动
然后就可以改密码
![[Pasted image 20231218212556.png]]
单用户是没有中文的,所以这里会出现乱码
是英文的是不会出现乱码的
最后使用
```
exec /sbin/init
```
重启系统就好了

这个必须要碰到实体机才可以修改,单用户是不联网的

### 查看运行级别 systemctl get-default

```
[root@localhost greptut]# systemctl get-default 
multi-user.target
```

### 设置运行级别
```
systemctl set-default graphical.target # 设置默认运行级别是图形
systemctl set-default multi-user.target # 设置默认运行级别为命令行
```
可以从图形化界面切到命令行
但是要从命令行切换到图形化界面,需要安装很多的软件包,然后才可以到图形化


