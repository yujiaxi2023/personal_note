## 用户组管理

我们创建了很多用户，将用户进行分组
windows和linux都有用户组的概念

用户和用户组都是计算机资源
组一般称为group
用户和用户组可以有无数个
为什么要用户组呢，因为我们需要给user权力的时候，可以批量进行操作，这样用户可以继承用户组的权利

在关系中，有1v1，1v多，多v多

用户和用户组就是多对多的关系

![[Pasted image 20231213221003.png]]

```
[root@localhost ~]# id
uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
```
我们会发现linux在创建用户的时候会默认创建一个同名的组
每个用户都会存在一个主组，每个用户都会有一个主组外加一些其他组

```
[root@localhost ~]# id dms
uid=1000(dms) gid=1000(dms) groups=1000(dms)
```

### 创建组 groupadd
```
userdel -r 用户名
```
这样可以删除用户主目录和邮件池

```
groupadd test
```
创建的组是在/etc/group中存放信息
```
cat /etc/group
```
```
[root@localhost ~]# cat /etc/group
root:x:0:
bin:x:1:
daemon:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mem:x:8:
kmem:x:9:
wheel:x:10:
cdrom:x:11:
mail:x:12:postfix
man:x:15:
dialout:x:18:
floppy:x:19:
games:x:20:
tape:x:33:
video:x:39:
ftp:x:50:
lock:x:54:
audio:x:63:
nobody:x:99:
users:x:100:
utmp:x:22:
utempter:x:35:
stapusr:x:156:
stapsys:x:157:
stapdev:x:158:
input:x:999:
systemd-journal:x:190:
systemd-network:x:192:
dbus:x:81:
polkitd:x:998:
ssh_keys:x:997:
tss:x:59:
abrt:x:173:
sshd:x:74:
postdrop:x:90:
postfix:x:89:
chrony:x:996:
dms:x:1000:
```

#### 新创用户加入组 useradd -g --gid GROUPS 建立新账户的主组
```
useradd -h
```
```
[root@localhost ~]# useradd -h
Usage: useradd [options] LOGIN
       useradd -D
       useradd -D [options]

Options:
  -b, --base-dir BASE_DIR       base directory for the home directory of the
                                new account
  -c, --comment COMMENT         GECOS field of the new account
  -d, --home-dir HOME_DIR       home directory of the new account
  -D, --defaults                print or change default useradd configuration
  -e, --expiredate EXPIRE_DATE  expiration date of the new account
  -f, --inactive INACTIVE       password inactivity period of the new account
  -g, --gid GROUP               name or ID of the primary group of the new
                                account
  -G, --groups GROUPS           list of supplementary groups of the new
                                account
  -h, --help                    display this help message and exit
  -k, --skel SKEL_DIR           use this alternative skeleton directory
  -K, --key KEY=VALUE           override /etc/login.defs defaults
  -l, --no-log-init             do not add the user to the lastlog and
                                faillog databases
  -m, --create-home             create the user's home directory
  -M, --no-create-home          do not create the user's home directory
  -N, --no-user-group           do not create a group with the same name as
                                the user
  -o, --non-unique              allow to create users with duplicate
                                (non-unique) UID
  -p, --password PASSWORD       encrypted password of the new account
  -r, --system                  create a system account
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  -s, --shell SHELL             login shell of the new account
  -u, --uid UID                 user ID of the new account
  -U, --user-group              create a group with the same name as the user
  -Z, --selinux-user SEUSER     use a specific SEUSER for the SELinux user mapping
```

创建两个新组规定到指定组内部
首先创建用户
```
groupadd test
```
新创用户
```
[root@localhost ~]# useradd -g test test1
[root@localhost ~]# useradd -g test test2
[root@localhost ~]# id test1
uid=1001(test1) gid=1001(test) groups=1001(test)
[root@localhost ~]# id test2
uid=1002(test2) gid=1001(test) groups=1001(test)
```

### 删除组 groupdel

删除组，在linux中每个用户都应该有一个组，如果组内有很多用户，就不能移除

所以删除组之前需要清除组内所有的以这个组为**主组**的用户

1. 删除以这个组为主组的所有用户
```
userdel -r test1
userdel -r test2
```

2. 修改用户的主组，让这个组没有以这个为主组的用户
```
usermod -h
usermod -g / --gid GROUP # 强制更改为GROUP为主组
```

### 将用户加入另一个其他组
```
usermod -G / --groups 组名 用户名
```
```
[root@localhost ~]# usermod -G test dms
[root@localhost ~]# id dms
uid=1000(dms) gid=1000(dms) groups=1000(dms),1001(test)
```

### linux用户修改密码

一般的密码修改会不符合linux对于密码复杂度的要求
所以如果太简单的密码是不允许进行修改的
123@qq.COM这种密码复杂度是允许的（数字，大小写字母，特殊符号，超过8位数）
1qaz@WSX 这种密码也比较好记（滚键盘）

```
# 设置密码
passwd
例子1： passwd test1
# 用root用户给普通用户修改密码
[root@localhost ~]# passwd dms
Changing password for user dms.
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: all authentication tokens updated successfully.
[root@localhost ~]# passwd dms
Changing password for user dms.
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: all authentication tokens updated successfully.
[root@localhost ~]# passwd dms
Changing password for user dms.
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: all authentication tokens updated successfully.
```
可以看到虽然会显示这是个不好的密码，但是也可以正常使用

```
# 更改普通用户自己的密码
passwd
```
![[Pasted image 20231213224313.png]]

```
例子3：
# 免交互修改密码
echo 123456|passwd --stdin test1
```

##### echo就是在屏幕上输出内容
我们使用管道符，就可以将这个输出应用到这个修改中
这是可以避免交互式改密码的卡在某一个执行界面的问题
非交互式修改密码是更加直接的

这种是在修改服务器密码的时候，大量的操作的时候方便进行批量化操作的


#### 查看用户是否被锁定
```
usermod
usermod -L test1
lchage -l test1
[root@localhost ~]# lchage -l dms
Account is not locked.
Minimum:	0
Maximum:	99999
Warning:	7
Inactive:	Never
Last Change:	12/13/2023
Password Expires:	Never
Password Inactive:	Never
Account Expires:	Never
```
Local CHange AGE的缩写，就是管理本地用户账户的密码更改信息

如果account expires，登录就会立即更改密码

```
# 禁止用户登录
usermod -s /sbin/nologin test2
grep -w 'test2' /etc/passwd
```

### groupmod可以更改组名等操作
```
groupmod -h
groupmod -n --new-name NEW-GROUP # 改名为NEW-GROUP
```

linux常用命令也就一百个左右

