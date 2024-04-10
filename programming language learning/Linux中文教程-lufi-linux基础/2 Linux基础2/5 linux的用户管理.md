### 创建用户useradd

```
useradd dms
ls /home/
```
创建用户会自动把家用户创建好了
ssh远程登录需要输入密码
```
ssh root@ip addr
ssh dms@ip addr # 这时候需要输入密码，但是因为是空密码，所以不让登录
```

### 设置用户密码passwd

```
passwd dms # 后边输入用户名
# 更改用户的密码
就可以直接输入了
```
```
[root@localhost dms]# passwd dms
Changing password for user dms.
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: all authentication tokens updated successfully.
```

这时候才能通过ssh登录新建用户

给root改密码
```
passwd
```
给普通用户改密码需要输入旧密码

#### 如果使用本地登录

当开机登录的时候输入需要的账户名
![[Pasted image 20231212141852.png]]

linux是可以同时登陆不同用户的，没有限制登录数量
win就会限制用户登录数量

登录的叫终端，每登录一次等于多开启了一个终端

### 统计现在打开了几个终端w

```
[root@localhost dms]# w
 00:21:30 up 21:54,  2 users,  load average: 0.00, 0.01, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1                      Mon02   21:54m  0.01s  0.01s -bash
root     pts/0    192.168.80.1     Mon02    2.00s  0.11s  0.02s w
```
我们看到这里登录有2个终端，这是为什么呢？
你通过终端命令`w`查看当前系统的用户信息。在这个输出中：

1. `root tty1` 表示在本地的 tty1 终端登录了一个名为 root 的用户。
2. `root pts/0` 表示通过网络连接（IP地址为192.168.80.1）的 pts/0 终端登录了另一个名为 root 的用户。

换句话说，你有两个终端窗口，一个是本地终端（tty1），另一个是通过网络连接的终端（pts/0）。两个窗口都是以 root 用户身份登录的。这是常见的情况，特别是在虚拟机（vmware）和远程连接工具（如xshell）中同时打开了终端。

##### win的远程桌面
当成功在win上进行了远程桌面，就会锁屏掉被控制的电脑桌面，说明无法同时登录多个终端

### 删除用户 userdel 用户名

win创建一个新的用户
![[Pasted image 20231212142913.png]]
创建之后如果不登录用户，就不会在用户文件夹下面创建新的文件夹
![[Pasted image 20231212143011.png]]

在linux下面只要创建用户就会创建home文件夹

win下如果想要删除用户
不会自动删除用户的文件夹

linux上删除用户并不会删除home目录
```
userdel 用户名
```
```
[root@localhost home]# rm -r dms
rm: descend into directory ∑dms∏? y
rm: remove regular file ∑dms/.bash_logout∏? y
rm: remove regular file ∑dms/.bash_profile∏? y
rm: remove regular file ∑dms/.bashrc∏? y
rm: remove regular file ∑dms/.bash_history∏? y
rm: remove directory ∑dms∏? y
```

如果这时候重新创建同名的文件就会报警告
![[Pasted image 20231212143548.png]]
这代表不会从样板目录中复制文件
因为在刚才创建到dms用户家目录中有一些隐藏文件
![[Pasted image 20231212143700.png]]

是从/etc/skel中拷贝的隐藏文件
```
[root@localhost ~]# ls -a /etc/skel
.  ..  .bash_logout  .bash_profile  .bashrc
```

win中也有一样的操作
![[Pasted image 20231212143837.png]]
这些目录会复制到新建用户的文件夹下
![[Pasted image 20231212143856.png]]

所以刚才的警告就是说明，这时候创建的同名用户，是不会新拷贝skel文件中的东西的

而且创建信箱文件的时候也会展示，已经存在
```
[root@localhost ~]# ls /var/spool/mail/
dms
```

新创建一个用户就会多一个邮箱文件，只要不重名

### 修改用户 usermod

在win下面修改用户
![[Pasted image 20231212144331.png]]
可以修改用户组，如果修改到管理员组就会拥有管理员权限
可以禁用该用户，就不能登录了
![[Pasted image 20231212144554.png]]
禁用的用户就是向下的箭头

#### usermod -h
usermod 有很多的参数，不需要全部记住
```
[root@localhost ~]# usermod -h
Usage: usermod [options] LOGIN

Options:
  -c, --comment COMMENT         new value of the GECOS field
  -d, --home HOME_DIR           new home directory for the user account
  -e, --expiredate EXPIRE_DATE  set account expiration date to EXPIRE_DATE
  -f, --inactive INACTIVE       set password inactive after expiration
                                to INACTIVE
  -g, --gid GROUP               force use GROUP as new primary group
  -G, --groups GROUPS           new list of supplementary GROUPS
  -a, --append                  append the user to the supplemental GROUPS
                                mentioned by the -G option without removing
                                the user from other groups
  -h, --help                    display this help message and exit
  -l, --login NEW_LOGIN         new value of the login name
  -L, --lock                    lock the user account
  -m, --move-home               move contents of the home directory to the
                                new location (use only with -d)
  -o, --non-unique              allow using duplicate (non-unique) UID
  -p, --password PASSWORD       use encrypted password for the new password
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  -s, --shell SHELL             new login shell for the user account
  -u, --uid UID                 new UID for the user account
  -U, --unlock                  unlock the user account
  -v, --add-subuids FIRST-LAST  add range of subordinate uids
  -V, --del-subuids FIRST-LAST  remove range of subordinate uids
  -w, --add-subgids FIRST-LAST  add range of subordinate gids
  -W, --del-subgids FIRST-LAST  remove range of subordinate gids
  -Z, --selinux-user SEUSER     new SELinux user mapping for the user account

```

#### 禁用用户 usermod -L usermod --lock

```
usermod -L dms # 下次登录的时候生效
```

#### 解锁用户 usermod -U usermod --unlock

```
usermode -U dms # 下次登录的时候生效
```

