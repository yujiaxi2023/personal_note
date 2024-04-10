linux和linux之间传输一般使用scp
linux需要跑ssh服务端，另一边才能scp过去
所以如果需要双向传输，就必须要又ssh服务端再跑

windows往linux上跑，只有scp，而且是只能单向，因为windows里面只有客户端没有服务端
win除了scp还有xftp也可以传输
xshell就可以用 rz 上传，sz可以反向下载到windows

从网站上下载
wget和curl
都是单向的从网站上下载
![[Pasted image 20231215225230.png]]

这些方法都可以传文件到linux上

## curl
```
# 下载文件
curl
例子1：
# 下载文件
curl -o 123.zip 下载地址
```
url地址，需要包含有文件的
```
curl -o filelist.gz https://mirror.tuna.tsinghua.edu.cn/centos/filelist.gz
```

curl -o 是为了避免curl显示文件到屏幕上，这是存起来的一个命令
curl其实是默认显示在屏幕上的

当然下载前提是检查网络是否通畅
使用ping命令进行
```
# 检查网络畅通
ping
# 如果网络不通，就重启网络服务
systemctl restart network
```

##### file命令查看文件类型
```
[root@localhost desktop1]# curl -o filelist.gz https://mirror.tuna.tsinghua.edu.cn/centos/filelist.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 7559k  100 7559k    0     0  2886k      0  0:00:02  0:00:02 --:--:-- 2888k
[root@localhost desktop1]# ll -h
total 7.4M
-rw-r--r-- 1 root root 7.4M Dec 15 09:05 filelist.gz
[root@localhost desktop1]# file filelist.gz 
filelist.gz: gzip compressed data, from Unix, max compression
```


### wget
wget是需要额外安装的
```
wget 下载文件的url
```
```
[root@localhost desktop1]# wget https://mirror.tuna.tsinghua.edu.cn/centos/filelist.gz
--2023-12-15 09:12:04--  https://mirror.tuna.tsinghua.edu.cn/centos/filelist.gz
Resolving mirror.tuna.tsinghua.edu.cn (mirror.tuna.tsinghua.edu.cn)... 101.6.15.130, 2402:f000:1:400::2
Connecting to mirror.tuna.tsinghua.edu.cn (mirror.tuna.tsinghua.edu.cn)|101.6.15.130|:443... connected.
ERROR: cannot verify mirror.tuna.tsinghua.edu.cn's certificate, issued by ‘/C=US/O=Let's Encrypt/CN=R3’:
  Issued certificate has expired.
To connect to mirror.tuna.tsinghua.edu.cn insecurely, use `--no-check-certificate'.
[root@localhost desktop1]# wget http://mirror.tuna.tsinghua.edu.cn/centos/filelist.gz
--2023-12-15 09:12:19--  http://mirror.tuna.tsinghua.edu.cn/centos/filelist.gz
Resolving mirror.tuna.tsinghua.edu.cn (mirror.tuna.tsinghua.edu.cn)... 101.6.15.130, 2402:f000:1:400::2
Connecting to mirror.tuna.tsinghua.edu.cn (mirror.tuna.tsinghua.edu.cn)|101.6.15.130|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7741232 (7.4M) [application/octet-stream]
Saving to: ‘filelist.gz.1’

100%[==========================================>] 7,741,232   4.81MB/s   in 1.5s   

2023-12-15 09:12:21 (4.81 MB/s) - ‘filelist.gz.1’ saved [7741232/7741232]
```
前边一个报错是因为清华源的问题
所以需要改https变为http

wget就不用指定文件名了


### linux之间互传

vmware进行克隆不能在开机状态进行克隆
必须关机状态进行克隆

```
scp 文件名 root@ip addr:/文件目录
# 代表以root身份 向哪台机器传输
# 第一次连接需要输入yes no
```
![[Pasted image 20231215231905.png]]
```
# 然后需要输入用户的密码
```
![[Pasted image 20231215231932.png]]
然后就会显示传输成功

这里没有文件大小限制，而且传输速度很快

![[Pasted image 20231215232022.png]]

```
scp 文件1 文件2 目标用户@目标ip地址：目录
scp file  file root@131.010.1：/tmp
```

只有第一次传送的时候需要输入密码
之后再在两个linux之间传输就不需要了

win10以上的版本也有scp
win中的scp不能有中文路径
```
(base) PS C:\Users\student\Desktop> scp CAADRIA2024_TEMPLATE.docx root@192.168.80.128:/root/lintut/desktop1
root@192.168.80.128's password:
CAADRIA2024_TEMPLATE.docx                                                             100%  390KB  12.9MB/s   00:00
```
![[Pasted image 20231215232729.png]]

win之间无法使用，因为默认使用的用户端，不是服务端

### lrzsz

```
[root@localhost desktop1]# yum lrzsz -y
```

最简单的上传
```
rz -E
```
![[Pasted image 20231215233358.png]]
也可以直接拖拽
执行的命令是一样的

```
sz 0.txt
```
这个也显示一样的界面，指定下载到那里去，是交互式界面
![[Pasted image 20231215233503.png]]

