```
输入
<
<<
# 标准输入0

输出
> 重定向，将命令执行结果不输出到屏幕上，输出到文件里面，会清空源文件
>> 追加重定向，不会清空源文件
# 标准正确输出1
# 标准错误输出2
```

## 输出

### 输出重定向
![[Pasted image 20231215210610.png]]
后边随便接一个不存在的文件名，如果文件名存在就会被覆盖掉
```
head -20 services > 1.txt
```
这样head -20 services就不会显示在屏幕上了
这些内容就保存在1.txt中

```
[root@localhost desktop]# head -20 services > 10.txt
[root@localhost desktop]# cat 10.txt
# /etc/services:
# $Id: services,v 1.55 2013/04/14 ovasik Exp $
#
# Network services, Internet style
# IANA services version: last updated 2013-04-10
#
# Note that it is presently the policy of IANA to assign a single well-known
# port number for both TCP and UDP; hence, most entries here have two entries
# even if the protocol doesn't support UDP operations.
# Updated from RFC 1700, ``Assigned Numbers'' (October 1994).  Not all ports
# are included, only the more common ones.
#
# The latest IANA port assignments can be gotten from
#       http://www.iana.org/assignments/port-numbers
# The Well Known Ports are those from 0 through 1023.
# The Registered Ports are those from 1024 through 49151
# The Dynamic and/or Private Ports are those from 49152 through 65535
#
# Each line describes one service, and is of the form:
#
```

这个命令的作用是
```
seq 1000 > 2.txt
```
这样就可以将需要的内容存到文件里面

### 输出追加重定向，会将内容添加到文件最后一行的后边

这样操作就不会清空源文件
```
echo 1 >> 1.txt
```
这个时候就不会覆盖，而是在最后添加
所以想毁掉文件
```
> 文件名
```
就这么干，源文件就非常干净了
```
seq 1000 > 1.txt
echo 1001 >> 1.txt
```
这样就是显示1-1001了在1.txt中

重定向只能对文件进行操作

#### 标准正确错误重定向

```
touch 123.txt > 1.txt
```
这样输出的就是空的，没有意义
```
cat 5.txt 1>1.txt 2>2.txt
```
执行一个错误命令
```
cat 5txt
# 会输出报错指令
```
```
cat 5txt 1>1.txt 2>2.txt
cat 2.txt
# 会输出报错指令，和直接运行cat 5txt是一样的
```
```
所以这里1就代表正确的输入到1.txt
2代表错误的输入到2.txt
```

```
pwd 1>a.txt 2>b.txt
adlfkljaldkf 1>a.txt 2>b.txt
```

## 输入

输入重定向的命令非常少

### 输入重定向
![[Pasted image 20231215212437.png]]
在这个网站，我们远程连接这个服务器
![[Pasted image 20231215212524.png]]
备份一下数据库，然后删库
![[Pasted image 20231215212559.png]]
![[Pasted image 20231215212611.png]]
我们删除掉dvwa库
![[Pasted image 20231215212647.png]]
这时候删掉了库

如果我们删除了一个网站拥有的数据库
这时候网站就打不开了，找不到数据库了
所以需要重新安装
![[Pasted image 20231215212420.png]]

这时候我们进行输入重定向
![[Pasted image 20231215212727.png]]
这样我们就可以把数据库灌进去了
这样又可以正常使用了
![[Pasted image 20231215212754.png]]

### 输入追加重定向

很多情况下输入重定向和输入追加重定向没有区别
因为输入的对象是空的
