建议是按照此方式进行linux优化

```
1. 优化ssh
vi /etc/ssh/sshd_config
79 GSSAPIAuthentication yes >>79 GSSAPIAuthentication no
115 #UseDNS yes >>115 UseDNS no
# 注意这里的#代表注释，也需要删除Use前边的#
# 上边这两个改成no
systemctl restart sshd

2. 优化selinux
# 修改配置文件，永久关闭
vi /etc/selinux/config
# 第7行修改为
SELINUX=enforcing >> SELINUX=disabled
需要重启生效
# 立即生效，临时的关闭状态
setenforce 0
sestatus # 查看当前SELinux状态
# 很多生产中的服务器不让重启，所以使用这个可以应急

3. 关闭firewalld
systemctl stop firewalld
systemctl disable firewalld

4. 安装常用软件
yum install lrzsz vim tree wget net-tools screen tcpdump bash-completion -y
```

### net-tools 网络工具

```
ifconfig # 可以用来看ip地址
# 可以查看网网卡的ip
ifconfig enc33 # 可以查看单独一块网卡
```

**rpm -qa 列举所有rpm包**
```
rpm -qa
```
**rpm -ql 列举出rpm包有多少文件**
```
rpm -ql
```

里面包含了很多网络的命令

### screen 

在后期是远程连接服务器，服务器很可能不在国内
这时候中间经过很多网络设备中转，经过很多设备就容易掉线
掉线就非常不好了，关键操作就不能够掉线
```
screen
```
会分配一个新的终端
```
sleep 600
```
如果这时候我们这时候不小心掉线了
重新登录
如果是我们正常使用的终端
掉线重登，之前的命令中终止进程了

如果是开的screen的bash
```
screen -ls
```
![[Pasted image 20231217184515.png]]
会显示我之前打开了几个screen窗口
这首如何恢复呢
```
screen -r 1830
```
这时候之前的进程就恢复了

```
exit
```
这是将screen的terminal退出

我们可以查看这个进程的父进程
```
ps -ef|grep 进程id
```
![[Pasted image 20231217184836.png]]
这里就可以看到我的进程的父进程是1，代表系统进程，所以只要对面服务器不关机，我的xshell的ssh关机是没有啥问题的


### tcpdump

是抓包的命令，比如说公共网络连接的时候，就很容易被人抓包抓下来

wireshark也是一个抓包软件
![[Pasted image 20231217185157.png]]
先安装软件
![[Pasted image 20231217185335.png]]
![[Pasted image 20231217190329.png]]
查找oicq的qq协议就可以抓包qq
里面会有一些信息，但是也有很多信息是加密的
![[Pasted image 20231217190432.png]]
在这里我们是查看自己服务器和重点服务器的ip
1295	21.612697	192.168.100.30	117.88.120.84	OICQ	81	OICQ Protocol 
可以查看最近的服务器，这个是浙江南京的服务器
只要是你的包过了我的电脑，我就能截取到一些信息
wireshark是win下面使用的抓包软件

```
tcpdump -i    ens33      port 22
            指定一个网卡  指定一个端口
```
电脑在不断地发包接收包，所以这就跟之前的破译一样

### bash-completion 超级自动补全

原来像是命令的参数无法补全tab没有这个功能
这个时候下载这个
可以tab补全非常多的命令

![[Pasted image 20231217191310.png]]
检查是否初始优化设置完毕
就检查这个命令，查看所有初始化的rpm包是否是485个

这时候我们可以创建一个系统优化快照
