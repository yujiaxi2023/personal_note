可以通过特殊权限给普通用户提权,让用户拥有root权限
特殊权限是把执行权限位给合并了
![[Pasted image 20231218220554.png]]
这时候我们看passwd这命令有什么权限
```
which passwd
stat /usr/bin/passwd
stat /etc/services
```
会发现首位是4
所以这个时候我们改一下权限
```
chmod u-x /usr/bin/passwd
```
![[Pasted image 20231218220744.png]]
这时候s->S,代表文件没有执行权限了
有suid权限的文件还是比较少的

我们改密码的时候改的是shadow文件
```
ll /etc/shadow
```
![[Pasted image 20231218221103.png]]

普通用户是不能直接改这个文件的,如果可以那就随便改变root用户了
每次改密码都找root很麻烦
普通用户想要改密码如果每次都切root就非常麻烦了
其他用户改密码都需要输入当前密码,并且输入一个复杂的密码


### suid 其他用户可以执行该文件属主的权限

![[Pasted image 20231218222049.png]]
如果取消了passwd的suid权限就不能改密码了
```
chmod u-s /usr/bin/passwd
```
![[Pasted image 20231218222142.png]]
这就是文件变成了普通可执行文件
只有加回来s权限就可以继承属主的权限
![[Pasted image 20231218222132.png]]

```
netstat -ltp # 普通用户执行这个命令就会报警
# 这个后边PID就不会显示
```
![[Pasted image 20231218222330.png]]
![[Pasted image 20231218222431.png]]
上边是root用户执行对应的命令,是可以显示pid
但是我如果想要任何的普通用户都可以执行这个命令查看pid
```
which netstat
chmod u+s /usr/bin/netstat
```
这样加过suid权限的文件就可以被普通用户执行成功
![[Pasted image 20231218222608.png]]
这个前提是普通用户是有这个文件的执行权限的

SUID ( Set owner User ID up on execution )
是针对命令文件设置的

![[Pasted image 20231218224801.png]]
统计出来这里的权限是4 suid