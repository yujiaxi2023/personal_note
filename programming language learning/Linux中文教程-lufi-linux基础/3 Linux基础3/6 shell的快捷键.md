#### tab键补全

```
# 补全命令
# 如果预选的特别多
```
```
[root@localhost lintut]# group
groupadd   groupdel   groupmems  groupmod   groups 
```
按两次tab就可以显示出group的所有可以补全的信息
如果给的信息很少，那么补全的内容就会更多，很多的可能性
```
[root@localhost lintut]# g
Display all 111 possibilities? (y or n)
```
这就会问你是不是要显示这么些命令
```
# 如果预选少就会正常显示出来内容
```

```
补全路径
# 如果预选的特别多
cd /etc/
```
```
[root@localhost lintut]# cd /etc/
Display all 187 possibilities? (y or n)
```
就会询问你是否需要显示所有可能
```
# 如果预选少
# 就可以直接显示内容
[root@localhost lintut]# cd /usr/src/
debug/   kernels/ 
```

tab关键在于是使用的时候可以帮助你辅助确认是否路径是对的

### 快捷键

```
ctrl + a # 光标跳转到正在输入命令行的首部
ctrl + e # 光标跳转到正在输入命令行的尾部
ctrl + c # 终止前台运行的程序
ctrl + d # 在shell中，ctrl - d 表示退出当前的shell
ctrl + z # 将任务暂停，挂到后台，执行fg命令继续运行
ctrl + l # 清屏，和clear命令等效
ctrl + k # 删除从光标到行末的所有字符
ctrl + u # 删除从光标到行首的所有字符
ctrl + r # 搜索历史命令，利用关键字
ctrl + w # 光标往前删除一个参数
esc + . # 上一条命令的最后一个参数或者目标
```

ctrl + d是退出登录的快捷键
ctrl + z 是放后台，然后fg就可以继续执行
#### ping判断网络通路
```
[root@localhost lintut]# ping 192.168.80.128
PING 192.168.80.128 (192.168.80.128) 56(84) bytes of data.
64 bytes from 192.168.80.128: icmp_seq=1 ttl=64 time=0.066 ms
64 bytes from 192.168.80.128: icmp_seq=2 ttl=64 time=0.414 ms
64 bytes from 192.168.80.128: icmp_seq=3 ttl=64 time=0.486 ms
64 bytes from 192.168.80.128: icmp_seq=4 ttl=64 time=0.184 ms
64 bytes from 192.168.80.128: icmp_seq=5 ttl=64 time=0.812 ms
64 bytes from 192.168.80.128: icmp_seq=6 ttl=64 time=0.161 ms
...

```
这时候只要不打断它就会一直ping下去
```
^Z
[1]+  Stopped                 ping 192.168.80.128
```
这就把命令放后台了
fg就会继续进行
```
[root@localhost lintut]# fg
ping 192.168.80.128
64 bytes from 192.168.80.128: icmp_seq=50 ttl=64 time=0.123 ms
64 bytes from 192.168.80.128: icmp_seq=51 ttl=64 time=0.199 ms
64 bytes from 192.168.80.128: icmp_seq=52 ttl=64 time=0.221 ms
64 bytes from 192.168.80.128: icmp_seq=53 ttl=64 time=0.202 ms
```
然后继续ctrl + z就会暂停
理论上可以无穷进行下去在linux中
如果是win中就是4个包后停止
![[Pasted image 20231215174915.png]]

ctrl + r可以搜索历史命令
```
(reverse-i-search)`': 
```
搜索到命令之后可以方向键右就可以得到了

ctrl + w 往前删一个目标或者参数

esc + . 
```
[root@localhost lintut]# touch a.txt
[root@localhost lintut]# cp a.txt /tmp
[root@localhost lintut]# ls /tmp
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
回溯一下最后一个命令的最后一个参数，或者是目标
