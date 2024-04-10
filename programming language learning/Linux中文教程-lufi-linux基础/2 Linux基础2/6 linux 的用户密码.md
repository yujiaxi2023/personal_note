我们可以查看文件的所有密码
```
cat /etc/passwd # 每创建一个用户，就会增加一行，我们会看到很多的系统用户是默认创建的
```
```
[root@localhost ~]# cat /etc/passwd
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
# 上面就是默认的用户
dms:x:1000:1000::/home/dms:/bin/bash
```

我们还可以从后往前看
```
tail -n 5 /etc/passwd
```
```
[root@localhost ~]# tail -n 5 /etc/passwd
abrt:x:173:173::/etc/abrt:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
dms:x:1000:1000::/home/dms:/bin/bash
```
还可以看到用户的家目录，每个用户家目录不一样


### 通过id查看用户的id信息
```
id
```
```
[root@localhost ~]# id
uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
```
上边查看psswd文件中也会显示uid 比如dms的uid是1000
root用户的uid是0
一般自建用户的uid是1000起步，小于1000的一般是系统用户

**所有的用户信息都存储在/etc/passwd文件中**
**所有的用户密码都存储在/etc/shadow文件中** 我们可以通过shadow文件中加密过的密码密文查看是否储存了用户密码
有很长的密文的就是有密码

比如说我创建了多个linux，多个linux中都包含有/etc/shadow文件，我现在想要把其中一个用户的密码文件覆盖到另一个用户的密码文件，那这样密码就变化了，只要权限足够，就可以将不同用户下的shadow文件覆盖另一个文件
![[Pasted image 20231213215154.png]]
但是并不需要覆盖这么复杂，就直接vi进去修改密文

![[Pasted image 20231213215442.png]]
只有root权限才能改这个文件


