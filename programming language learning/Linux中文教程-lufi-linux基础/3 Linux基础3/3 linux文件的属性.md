## 文件属性

```
# 文件属性
drwxr-xr-x.  19 root root  267 Dec  5 02:59 var
# 第一段的第一个字符，表示文件类型 -文件 d目录 l软连接 b块设备
# 234字符，表示文件所属用户的权限
# 567字符，表示文件所属用户组权限
# 8910字符，表示其他用户对于这个文件的权限
# 第11个字符，表示开启selinux的状态下创建的

# 第二段的数字 表示该文件的硬链接数量

# 第三段的字符串 表示该文件所属用户

# 第四段的字符串 表示该文件的所属用户组

# 第五段的数字 表示该文件的大小

# 第六段到倒数第二段 都是文件的修改时间

# 最后一段 是文件的名称
```
linux是一切都是文件的系统

selinux状态，可以把`.`理解成一个上锁的标志
SELinux是一种安全增强型的Linux操作系统内核模块，它提供了强大的访问控制机制，用于细粒度地控制进程和用户对系统资源的访问。SELinux的全称是Security-Enhanced Linux，它最初由美国国家安全局（NSA）开发，并在Linux社区中得到广泛采纳。

SELinux通过强制访问控制（MAC）来实现其安全目标。与传统的Linux访问控制（DAC）不同，SELinux基于策略规则来定义哪些进程可以访问哪些资源，以及以何种方式进行访问。这种细粒度的控制使得系统更难受到恶意软件和未经授权的访问的威胁。

在使用SELinux的系统上，每个文件、进程和用户都有与之相关联的安全上下文，规定了它们的权限和行为。SELinux的主要目标是提高Linux系统的整体安全性，防止潜在的攻击和漏洞利用。

总的来说，SELinux是一种强大的安全机制，适用于需要高度安全性的环境，如企业服务器和关键基础设施。

因为这个SELinux非常麻烦，所以只有redhat系列有这个SELinux，很多发行版的都没有的 华为欧拉系统（服务器操作系统）和centos没啥区别 阿里巴巴的龙蜥也是类似的

debian系统：比如ubuntu debian kali uos等都不需要

### sestatus 用来查看selinux状态

```
sestatus
```
```
[root@localhost desktop]# sestatus
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Max kernel policy version:      31
```

在主板bios里面有启用禁用，enable disable

我们如何对selinux状态进行编辑
```
ls /etc/selinux
vi /etc/selinux/config
```

**tab可以补全路径**所以在输入路径的时候使用这个可以快速找到路径

![[Pasted image 20231214224510.png]]
进去之后可以修改这里

Linux非常严谨，严格区分大小写
window就不区分

此时查看selinux状态就是disabled
现在创建的文件就不会有selinux上锁的标志
```
[root@localhost ~]# sestatus
SELinux status:                 disabled
```

没有selinux上锁标志就是disabled的情况下创建的

### 硬链接数
一般运维需要使用
```
drwxr-xr-x.  19 root root  267 Dec  5 02:59 var
```
硬链接就像是一个房间有很多的门
如果将门堵死了linux就在linux就会消失，就再也找不到了

#### 创建硬链接
```
ln 文件名 新的硬链接路径
```
```
[root@localhost desktop]# ls -l
total 76
----------. 1 root root     0 Dec 14 05:21 1.txt
-rw-r--r--. 1 root root    22 Dec 14 06:14 2.txt
-rw-r--r--. 1 dms  dms      0 Dec 14 05:21 3.txt
-rw-r--r--. 1 root root     0 Dec 14 05:21 4.txt
-rw-r--r--. 1 root root     0 Dec 14 05:21 5.txt
drwxr-xr-x. 2 root root   141 Dec 14 01:52 dms
-rw-r--r--. 1 root root    21 Dec 14 02:30 linux.txt
-rwxr-xr-x. 1 root root 66824 Dec 14 06:10 tail
[root@localhost desktop]# ln 2.txt dms/a.txt
[root@localhost desktop]# ls -l
total 76
----------. 1 root root     0 Dec 14 05:21 1.txt
-rw-r--r--. 2 root root    22 Dec 14 06:14 2.txt
-rw-r--r--. 1 dms  dms      0 Dec 14 05:21 3.txt
-rw-r--r--. 1 root root     0 Dec 14 05:21 4.txt
-rw-r--r--. 1 root root     0 Dec 14 05:21 5.txt
drwxr-xr-x. 2 root root   154 Dec 14 08:57 dms
-rw-r--r--. 1 root root    21 Dec 14 02:30 linux.txt
-rwxr-xr-x. 1 root root 66824 Dec 14 06:10 tail
```

```
cat 2.txt
cat dms/2.txt
```
```
[root@localhost desktop]# cat 2.txt
akljdfgh
adfkjahdjf
:
[root@localhost desktop]# cat dms/a.txt
akljdfgh
adfkjahdjf
:
```
如果删除任意的硬链接入口，就会减少硬链接的数量
有多少个硬链接的入口，就是有多少个硬链接数量
只有所有的硬链接消失了，就非常难找回（技术要非常好）
![[Pasted image 20231214230416.png]]

就跟win一样，这块空间就会被别的内容覆盖

![[Pasted image 20231214230602.png]]
首先更改了用户组
然后删除了同名用户的同时删除了用户组
所以显示出来的就是一个gid（用户组id）

首先创建了两个linux1 和 linux2
然后在linux1下面创建test用户， linux2下面创建dms用户
然后产生对应的uid和gid
如果这个时候在test用户下面创建了一个文件，它所属的uid和gid是被记住的，然后一旦保持属性转移到linux2的dms用户，这个时候回根据uid和gid去检索对应的值并显示出来

![[Pasted image 20231214231015.png]]

文件属性并不会记录用户名

#### 文件大小
```
drwxr-xr-x.  19 root root  267 Dec  5 02:59 var
```
可以看到包含的字节数
如果想看到kb
```
ls -lh # 就会显示kb等内容
```
```
[root@localhost dms]# ls -lh
total 13M
-rw-------. 1 root root 1.3K Dec 11 02:47 anaconda-ks.cfg
-rw-r--r--. 2 root root   22 Dec 14 06:14 a.txt
-rw-------. 1 root root 1.3K Dec 11 02:45 copy1.cfg
-rwxr-xr-x. 1 root root 6.5M Dec 14 01:52 vmlinuz-0-rescue-79cb8153c5e5418ebbb03c16607aad63
-rwxr-xr-x. 1 root root 6.5M Dec 14 01:52 vmlinuz-3.10.0-1127.el7.x86_64
```
可以看到有kb mb
只保留一位小数，所以会自动进行四舍五入
-lh 对应的是human

## linux记录的时间

### 访问时间 access time

只要访问一次文件就会修改时间，win也是一样的

### 修改时间 modify time


### 改变事件 change time

### stat 来看文件的各种属性
```
stat 文件名
```
```
[root@localhost desktop]# stat 2.txt
  File: ‘2.txt’
  Size: 22        	Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d	Inode: 201332233   Links: 2
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2023-12-14 08:58:32.191044758 -0500
Modify: 2023-12-14 06:14:34.944364761 -0500
Change: 2023-12-14 08:57:13.864701942 -0500
 Birth: -
```
我们chmod一下这个文件
```
[root@localhost desktop]# stat 2.txt
  File: ‘2.txt’
  Size: 22        	Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d	Inode: 201332233   Links: 2
Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2023-12-14 08:58:32.191044758 -0500
Modify: 2023-12-14 06:14:34.944364761 -0500
Change: 2023-12-14 09:20:43.971206059 -0500
```
可以发现change时间变了

##### 概念区分

访问时间（Access Time）和修改时间（Modification Time）是文件元数据中的两个重要时间戳，它们记录了文件的不同时间点的状态变化。

访问时间（Atime）：

访问时间表示文件最后一次被读取的时间。
当文件被打开、阅读、执行等操作时，访问时间会被更新。
在一些文件系统中，启用"noatime"选项可以禁止或减少对访问时间的更新，以提高性能。

修改时间（Mtime）：

修改时间表示文件最后一次被修改的时间。
当文件内容发生变化时，修改时间会被更新。
大多数编辑操作、写入文件、更改文件属性等都会导致修改时间的更新。

变化时间（Ctime）：

变化时间表示文件的状态信息最后一次发生变化的时间。
包括文件内容的修改、权限的变更等都会导致变化时间的更新。
注意，即使只是修改文件的权限而不改变其内容，变化时间也会更新。

总体来说，这三个时间戳提供了关于文件状态的不同方面的信息。访问时间告诉你最后一次文件被访问的时间，修改时间告诉你最后一次文件内容被修改的时间，而变化时间告诉你最后一次文件状态变化的时间


ls -l 显示的是modificaiton的时间

```
[root@localhost desktop]# stat 4.txt
  File: ‘4.txt’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 201332229   Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2023-12-14 05:21:20.940128832 -0500
Modify: 2023-12-14 05:21:20.940128832 -0500
Change: 2023-12-14 05:21:20.940128832 -0500
 Birth: -
[root@localhost desktop]# cat 4.txt
[root@localhost desktop]# stat 4.txt
  File: ‘4.txt’
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d	Inode: 201332229   Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2023-12-14 09:28:46.936312258 -0500
Modify: 2023-12-14 05:21:20.940128832 -0500
Change: 2023-12-14 05:21:20.940128832 -0500
 Birth: -
```
这个例子很好的展现了Atime的变化

