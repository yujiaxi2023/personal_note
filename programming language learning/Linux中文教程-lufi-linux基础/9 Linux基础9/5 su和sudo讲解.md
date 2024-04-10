## su 和 sudo
```
su == switch user
sudo == superuser do
```

```
1. 配置/etc/sudoers
# 用户名     所有终端 = 运行的用户身份   命令ALL
zhangsan      ALL=(ALL)               /bin/sytemctl,/usr/bin/vim
2. 使用sudo执行命令
# 使用sudo来执行命令
sudo systemctl stop network # start,stop,restart

# 查看可以使用的授权命令
```

### su

root可以很容易的切换到普通用户
```
su - dms
```
其他的用户切换到root是使用root密码

但是要注意这里的su是起了一个子进程,所以是可以退出,退出就回到了原来的用户进程了
```
ctrl + d
```
推荐是su - 用户名
这样可以进入到用户的家目录下面
![[Pasted image 20231218231526.png]]
不带 - 就不会继承家目录和一些环境变量


### sudo

是用来授权的命令
授权也是一个个命令授权,并不是所有的root权限都一次性授予
![[Pasted image 20231218231853.png]]

```
visudo
```
这个可以编辑授权
授权新的用户权限是使用绝对路径指定到文件中
![[Pasted image 20231218232042.png]]
一定要符合这个格式,不然无法保存
授权之后立马生效
![[Pasted image 20231218232117.png]]
![[Pasted image 20231218232131.png]]
这样普通用户就已经被授权了
但是要注意的是普通用户执行授权命令的时候需要加sudo
```
sudo reboot
```
这样就可以进行普通用户的重启了

### sudo -l 查看授权指令
```
sudo -l
```

### sudo cmd  以授权的方式来执行命令

这个是一个很搞笑的场面,给到了用户vim权限
这时候打开shadow文件可以干掉root
可以用自己的密码替换root密码
```
sudo vim /etc/shadow
```
![[Pasted image 20231218232501.png]]

执行visudo的时候编辑的是/etc/sudoers
```
visudo
vim /etc/sudoers
```
两个命令是一个作用
这样就可以自己给自己提权