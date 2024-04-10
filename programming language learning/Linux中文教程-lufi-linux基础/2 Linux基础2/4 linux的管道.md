### cat查看文件所有行
```
# 从上到下查看文本内容
cat
例子1：cat test03.txt # 查看test03.txt全部内容
# 从下到上倒着查看文本内容
tac
例子1：tac test03.txt # 倒着查看test03.txt的全部内容
```
不管文件多长，都会看完，如果文件太大，也会全部显示就会看到刷屏刷半天，大到一定程度，电脑会卡死，因为需要加载文件从硬盘到内存
所以这个适合看小文件，不适合看大文件

```
vi anaconda-ks.cfg # 进入编辑文件

# 进入到编辑模式
:set number # 显示文件有多少行
```
vi的三种模式：
- 常规模式
- 编辑模式 `i a o`
- 命令模式 `:`

![[Pasted image 20231211165510.png]]

### head查看文件头几行
```
# 查看文件头几行
head
例子1： head test03.txt # 查看文件前10行，默认
例子2： head -n 5 test03.txt # 查看文件前5行
例子3： head -5 test03.txt # 查看文件前5行
```
包括空白行
### tail 查看文件倒数几行
```
# 查看文件倒数几行
tail
例子1： tail test03.txt # 查看文件倒数10行
例子2： tail -n 5 test03.txt # 查看文件倒数5行
例子3： tail 5 test03.txt # 查看文件倒数5行
```
包括空白行的内容

### 管道

管道就是将原始内容过滤一下`|`

```
[root@localhost dms]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:d4:9b:89 brd ff:ff:ff:ff:ff:ff
    inet 192.168.80.128/24 brd 192.168.80.255 scope global noprefixroute dynamic ens33
       valid_lft 1730sec preferred_lft 1730sec
    inet6 fe80::dc85:f288:d55e:1b8c/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```
我们会发现查看内容很繁琐，我们其实只需要最后4行的数据
这时候我们能使用管道符
```
[root@localhost dms]# ip addr|tail -n 4
    inet 192.168.80.128/24 brd 192.168.80.255 scope global noprefixroute dynamic ens33
       valid_lft 1642sec preferred_lft 1642sec
    inet6 fe80::dc85:f288:d55e:1b8c/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

这样我们还是觉得多了
```
[root@localhost dms]# ip addr|tail -n 4|head -n 1
    inet 192.168.80.128/24 brd 192.168.80.255 scope global noprefixroute dynamic ens33
```
这样就可以只打印出来这一行

单独使用head tail都必须要一个目标文件才能进行处理
在管道中就没有这个要求
但是要求是：
- 在管道中第一个命令必须有输出，（没有输出的就像是ls，mkdir，有输出的就像是cat，tail，head等）
- 管道的作用就是对第一条命令的输出结果进行再加工

### cut 数空格从第几个开始切一直到第几个
```
[root@localhost dms]# ip addr|tail -n 4|head -n 1|cut -c 4-30
 inet 192.168.80.128/24 brd
```
这个命令还需要自己数，所以比较麻烦，所以并不非常需要

**linux的管道：最强大的功能**
linux实现一个复杂的功能，就可以使用多个软件一起处理，也就是我们把ip addr，head，cut，tail是一个个的软件，更加开放和自由
win中，要实现一个复杂的功能，就需要一个强大的软件
## xshell使用快速命令

![[Pasted image 20231211171043.png]]
在这里勾选上快速命令
![[Pasted image 20231211171125.png]]
然后双击红色部分就可以编辑快捷命令，我们只需要设置自己习惯的快捷键就可以快速的使用这个复杂的命令

