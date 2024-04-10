
```
# 历史
history
```
```
[root@localhost lintut]# history
    1  exit
    2  shutdown -h now
    3  ls
    4  ip addr
    5  shutdown -h now
    6  ls
    7  cd .
    8  cd /
    9  ls
   10  cd ~
   11  ls
   12  exit
   13  clear
   14  ls
   15  mkdir linux-basic-tutorials
   16  ls
...
  300  history

```
这里就可以看到历史中得到的所有命令
之前执行了多少命令，黑客使用了什么历史命令也会阐述
如何清除历史记录呢
```
history -c
```

##### 如果想要调用历史命令
```
!编号
```
```
[root@localhost lintut]# !299
ls /tmp
a.txt
ks-script-T7dPMN
systemd-private-44b64900f5444bcda345fb8f42aac39d-chronyd.service-EuFXTS
vmware-root_555-4282367637
vmware-root_572-2999067484
vmware-root_603-3980363997
vmware-root_636-2730627900
vmware-root_650-2696943027
yum.log
```

当我不记得编号是什么的时候，可以使用模糊搜索，但是只能找最近的命令，而且可以不输入完整的命令，而是使用某几个关键字
```
# 比如我想要找到最近一个cat敏玲
!cat
```
```
[root@localhost lintut]# !cat
cat /etc/passwd
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

history命令还有一个地方记录了

我们的history -c是清理的内存中的历史记录
但是history实际上是存在硬盘里面的 
这样才能保证每次开机的时候能看到历史记录
所以在硬盘没有同步到命令history -c的时候，都是储存在硬盘空间里面的
```
[root@localhost ~]# ls -a
.   anaconda-ks.cfg  .bash_logout   .bashrc  lintut
..  .bash_history    .bash_profile  .cshrc   .tcshrc
```
```
[root@localhost ~]# cat .bash_history
exit
shutdown -h now
ls
ip addr
shutdown -h now
ls
cd .
```
我们可以看到这里存着历史记录

需要历史记录清的彻底，就需要删除掉这个历史命令文件
删除掉之后再继续执行就会新创建这个history文件
这是在退出exit之前将内存刷到硬盘中的文件进行储存

这里的.bash_history是储存的各个用户的历史命令

shell的历史命令会自动记录1000条，这个可以进行设置更改记录
```
echo $HISTSIZE
```
![[Pasted image 20231215181153.png]]
