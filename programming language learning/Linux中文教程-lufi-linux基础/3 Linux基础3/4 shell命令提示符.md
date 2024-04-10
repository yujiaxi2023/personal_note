## linux shell

shell是linux中比较重要的概念

Linux所有的一切命令都称为shell命令

什么是shell？

计算机时由硬件 --> 硬件上有我们的内核kernel，这个决定了我们的支持什么样的硬件，比方说龙芯，只有加入了linux内核，我们无法控制硬件的

内核我们无法控制，它是用来驱动硬件的

再往上是操作系统

再往上是应用软件
这是win的层级结构
![[Pasted image 20231214233810.png]]

在linux上边
我们执行的是命令行
所以在内核外边有一层shell
所以我们在计算机启动的时候就是启动的shell
然后再shell中调用系统内核，内核接着调用硬件
![[Pasted image 20231214234648.png]]
如果删除了shell，我们什么都干不了


##### 如何看用的是什么shell
```
cat /etc/passwd
# shell再最后一列
```
```
[root@localhost desktop]# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
dms:x:1000:1000::/home/dms:/bin/bash
test1:x:1001:1001::/home/test1:/bin/bash
test2:x:1002:1001::/home/test2:/bin/bash
```
当我们掌握了之后，可以改变用户使用的shell

默认使用的就是/bin/bash
如果使用/sbin/nologin 就是无法登陆的 
后期还可以安装其他的shell

shell就是一个工具
如果我们瞎执行命令，就会在shell这里报错
如果我们输入的格式有问题就会直接报错

有的时候我们会碰到需要优化ssh登录速度
```
# 修改配置文件
# 先进行备份
cp /etc/ssh/sshd_config /tmp/
vi /etc/ssh/sshd_config
# 直接输入:79回车
79 GSSAPISuthentication no
115 UseDNS no
输入:wq保存退出

# 重启sshd服务
systemctl restart sshd

# 如果修改失败
# 还原配置文件
cp /tmp/sshd_config /etc/ssh/sshd_config
systemctl restart sshd
```

### shell提示符

```
# root用户提示符
[root@localhost desktop]# 

# 普通用户提示符
[dms@localhost ~]$ 
```
localhost是我们的主机名

windows主机名是在高级系统设置
![[Pasted image 20231214235452.png]]

同一个网络上有多台计算机，就应该起名字
我们没有改名的时候，就会使用默认的localhost名字

### 更改主机名 hostname

改完主机名需要重新登陆一下才能生效

如果处在主文件夹下面就会用~
```
# 普通用户提示符
[dms@localhost ~]$ 
```
如果在不同的目录下面会显示相对路径的名字
```
# root用户提示符
[root@localhost desktop]# 
```

```
[root@localhost desktop]# 这里的#是代表root
普通用户就是$
```

也可以修改为绝对路径显示
```
# 提示符格式定制
原格式
[root@localhost desktop]# 
```
```
echo $PS1 # 这是一个系统变量用来控制显示
这样会显示系统当前变量
```
```
[root@localhost desktop]# echo $PS1
[\u@\h \W]\$
```
```
cd /usr/local/bin/
export PS1='[\u@\h \w]\$'
# 这就可以修改了显示绝对路径
# 这里面还可以加时间'[\u@\h \t \w]\$'
# 还可以定制花花绿绿
```
在网上可以搜定制的教程
我们需要保存才能改变，不然就会重启失效
```
想要永久修改
cd ~
vi .bashrc
# 找一个空白的地方
export PS1='[\u@\h \w]\$'
就可以永久修改了
```

linux路径
相对路径 不完整路径 特殊一点的就是.和..代表当前和上个目录
绝对路径 完整路径

### 永久修改主机名hostnamectl
```
hostnamectl set-hostname test 就会永久改主机名
```
之前的就是重启系统的时候就会失效了

kali命令行提示符就比较奇怪
这是一个黑客的系统
![[Pasted image 20231215001158.png]]
命令提示符是两行

