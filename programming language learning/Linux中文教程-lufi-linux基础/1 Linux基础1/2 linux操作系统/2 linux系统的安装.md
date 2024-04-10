linux系统的自由度非常高，可以自己把自己干掉

# 使用vmware player

使用vmware player安装虚拟机运行centos7，镜像文件网上随便下载就行

linux最高权限用户root
**这里我们设置的密码是123456**

如果我们要使用非图形化的linux，我们就需要远程连接

**第一个linux命令**
## 使用windows远程连接linux
```linux
# 查看IP地址
ip addr
```
```shell
# 远程连接linux
(base) PS C:\Users\student> ssh root@192.168.80.128
The authenticity of host '192.168.80.128 (192.168.80.128)' can't be established.
ED25519 key fingerprint is SHA256:SyQEUWvinuhnQBMn+n1dKpm+ZM0X25m/4i8jcrbFHdw.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.80.128' (ED25519) to the list of known hosts.
root@192.168.80.128's password:
Last login: Tue Dec  5 03:01:37 2023
```
这时候我们在cmd就可以进行粘贴

我们尽量用远程控制会很方便
以后的服务器都不在本地使用，所以使用远程控制机器才是正道

当我们窗口关闭之后，需要重新连接ssh才能连接上centos
但是第二次连接就可以只用输入密码就可以

## 使用xshell进行远程连接

下载xshell免费版通过ip地址和账号密码就可以实现远程连接centos

这个时候准备工作结束

## linux的关机重启

```shell
shutdown -h now
shutdown -h 10 # 10min after shutdown
```

```shell
shutdown -r now # 重启
reboot
```
## vmware player的快照

如果想要进行vmplayer中快照功能，需要全部备份所有文件，并储存到新的文件夹中，并且使用vmplayer打开就可以了

