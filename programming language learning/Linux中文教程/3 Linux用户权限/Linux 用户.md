![[Pasted image 20230405191402.png]]
root用户就是超级管理员
![[Pasted image 20230405191505.png]]

![[Pasted image 20230405191624.png]]
根目录下面进行文件夹创建，需要使用根目录
![[Pasted image 20230405191724.png]]
这样就多了test文件夹
普通用户在大多数的home之外的目录都是没有修改权限的

![[Pasted image 20230405191833.png]]
利用su切换用户 su - 用户名
如果不加入用户名，就会载入到root用户
可以通过exit或者是ctrl d切换回上一个用户
![[Pasted image 20230405192008.png]]
如果不添加账户就会直接切换root
![[Pasted image 20230405192335.png]]
当root用户切换其他用户不需要密码，当普通用户切换就需要密码

![[Pasted image 20230405192507.png]]
利用sudo命令就可以利用root的权限进行命令
需要为普通用户配置sudo认证才可以使用sudo
![[Pasted image 20230405192628.png]]
完成编辑之后就可以在当前用户使用sudo命令
![[Pasted image 20230405193111.png]]
![[Pasted image 20230405193246.png]]
当去除掉权限之后就会询问你密码

![[Pasted image 20230405193741.png]]
针对某文件，可以控制用户的权限，也可以控制用户组的权限
用户组管理需要root用户
![[Pasted image 20230405193835.png]]
![[Pasted image 20230405193926.png]]
![[Pasted image 20230405193936.png]]
创建用户组后可以使用下面四个命令

useradd如果直接-d是指定home路径，如果不指定文件夹就会默认在home下的用户名对应的路径
-g就是指定用户的组，而且这个组必须存在，不然就会创建一个新的组并且加入

用户的删除
![[Pasted image 20230406141602.png]]
当添加-r的时候就会删除用户的home目录

![[Pasted image 20230406141832.png]]
使用id可以查看用户的组
![[Pasted image 20230406141952.png]]
可以使用id查看创建的test3
使用usermod -aG可以将指定的用户加入到指定的组之中
![[Pasted image 20230406142159.png]]
使用了usermod命令之后test4存在于yujiaxi和test4这个组之中

如果要查看系统中一共存在哪些组就使用getent命令
![[Pasted image 20230406142249.png]]
使用getent命令之后就是
![[Pasted image 20230406142436.png]]
下面的是我们创建的组，还有在上面的一些用户名之外的注册时候默认生成的组

![[Pasted image 20230406142606.png]]

**查看权限控制信息**
使用ls -l可以用列表形式查看内容
![[Pasted image 20230406143603.png]]

![[Pasted image 20230419144315.png]]

其中每个字符表示的含义如下

![[Pasted image 20230406143628.png]]
例如drwxr-xr-x代表这是一个文件夹，所属用户的权限又rwx，所属用户组权限是rx权限没有w权限，其他用户权限是拥有rx权限没有w权限
“-”表示的是文件
d是代表文件夹
l代表的是软链接
![[Pasted image 20230406170141.png]]
其中-代表的文件夹 1.txt

其中rwx是什么意思
![[Pasted image 20230406170341.png]]
r代表的是刻度权限，w是可写权限，x代表可执行文件
对于文件夹的x就是是否可以进入这个文件夹
![[Pasted image 20230406171026.png]]
当我们在root用户下面打开ls -l的时候，我们的yujiaxi用户就只有序号3的地方的可读权限
![[Pasted image 20230406171129.png]]
如果我们在这个文件中进行执行修改权限就会出现报错，即使使用了强制执行也无法进行修改
例如在根目录下的文件夹就无法使用yujiaxi用户进行修改

**修改权限控制chmod**
![[Pasted image 20230419144417.png]]
chmod是可以修改文件的权限信息，但是只有在文件或者文件夹的所属用户或者root用户可以修改

语法就是chmod -R
-R可以让文件夹内的所有内容使用同样的操作

**示例**
chmod u=rwx,g=rx,o=x hello.txt
可以将文件修改为rwxr-x--x
![[Pasted image 20230419144759.png]]

![[Pasted image 20230419144809.png]]
加入-R之后其他的内容是一样的写法

![[Pasted image 20230419145417.png]]
这就是把test.txt文件夹修改成其他用户只能写，组用户可以读的状态
![[Pasted image 20230419145831.png]]
表示这个文件夹很危险的权限

但是这样每次写都很麻烦
所以
![[Pasted image 20230419145917.png]]

可以用这种三位数字的方式去调整权限

![[Pasted image 20230419150014.png]]

利用chmod 三位数字 文件名的方式改权限
![[Pasted image 20230419150454.png]]
数字对应是在写系统的时候 **r记为4，w记为2，x记为1**

**小总结**
![[Pasted image 20230419150830.png]]

**chown**
![[Pasted image 20230419171800.png]]
语法：chown -R
运用这个命令可以修改这个文件的所属用户或者是用户组
![[Pasted image 20230419172153.png]]
修改这个文件没有权限，我如果要修改成root，因为root的等级更高，所以没法更改到别的用户或者用户组中

**所以这个命令只能用root执行**

![[Pasted image 20230419172620.png]]

```shell
chown root hello.txt
# 将hello.txt所属用户修改为root

chown :root hello.txt
# 将hello.txt所属用户组修改为root

chown root:yujiaxi hello.txt
# 将hello.txt所属用户修改为root，所属用户组修改为yujiaxi

chown -R root test
# 将文件夹test的所属用户修改为root并对文件夹内全部的内容应用同样规则
```
![[Pasted image 20230705213239.png]]
显示没有权限进行修改，这个现在没有root的权限，所以yujiaxi这个普通用户没有权限把文件修改到root用户下
![[Pasted image 20230705213438.png]]
这样就修改成功
接下来是修改用户组
![[Pasted image 20230705213537.png]]

![[Pasted image 20230705213616.png]]
这个是两者一起修改

![[Pasted image 20230705213859.png]]
这里是用-R操作进行修改

**chown总结**
![[Pasted image 20230705214037.png]]
