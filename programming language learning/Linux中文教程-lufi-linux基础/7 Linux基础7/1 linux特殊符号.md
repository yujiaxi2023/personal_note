### 注释`#`
```
# 注释 备注 批注
如果我瞎写一段字符
系统会提示没有这个命令
但是如果添加了#
系统会默认后边的是注释，就会消失了
```
![[Pasted image 20231217214523.png]]
还有一些是使用//注释


### 命令的分隔符;
```
; 命令的分隔符
touch 11.txt;chmod 777 11.txt
```
这个和管道符并不一样，管道必须是上一个有输出作为下一个的输入


### 上级目录..
```
cd ..
```

### 当前目录.
```
cd .
```

### 换行""解析变量
```
echo adjklf # 原本是只能输出单行

但是我们使用换行

[root@localhost ~]# echo "fakjdhf
> klajdfhgoraehnrf
> akldjfeiahgkladflj
> adlkjfnczklvjadf
> alkdf"
fakjdhf
klajdfhgoraehnrf
akldjfeiahgkladflj
adlkjfnczklvjadf
alkdf

# 这样可以比较方便的进行重定向等内容
```

### 换行’‘不解析变量

```
# 很多情况下和双引号""一样的
# 比如说输出文本的时候，只要不涉及变量就是一样的
```

#### 变量
查看系统设置的环境变量
```
env
```
![[Pasted image 20231217215353.png]]
这里会显示
这些大写字母代表系统环境变量的名称，它们在Linux系统中用于存储各种配置信息和参数。以下是其中一些常见的环境变量及其含义：

1. XDG_SESSION_ID=3：
	- 会话ID，用于标识用户的会话。

2. HOSTNAME=localhost.localdomain：

	- 主机名，表示计算机在网络上的名称。

3. TERM=xterm：

	- 终端类型，指定终端的类型。

4. SHELL=/bin/bash：

	- 用户默认的Shell，即命令行解释器。

5. HISTSIZE=1000：

	- 命令历史记录的大小，表示在命令行中可保存的历史记录数目。

6. SSH_CLIENT=192.168.80.1 63138 22：

	- SSH客户端信息，包括源IP地址、端口和SSH端口号。

7. SSH_TTY=/dev/pts/1：

	- 当前终端的TTY设备。

8. USER=root：

	- 当前登录用户的用户名。

9. LS_COLORS=...：

	- 定义ls命令输出中文件和目录的颜色。

10. MAIL=/var/spool/mail/root：

	- 邮件存储路径，指定用户的邮件存储位置。

11. PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin：

	- 环境变量之一，包含可执行文件的搜索路径。

12. PWD=/root：

	- 当前工作目录，表示用户当前所在的路径。

13. LANG=en_US.UTF-8：

	- 默认语言设置，指定系统的语言和字符编码。

14. SHLVL=1：

	- Shell级别，表示当前Shell的嵌套深度。

15. HOME=/root：

	- 用户主目录的路径。

16. LOGNAME=root：

	- 登录用户名。

17. SSH_CONNECTION=192.168.80.1 63138 192.168.80.132 22：

	- SSH连接信息，包括源IP、端口和目标IP、端口。

18. LESSOPEN=||/usr/bin/lesspipe.sh %s：

	- less命令打开文件时使用的过滤器。

19. XDG_RUNTIME_DIR=/run/user/0：

	- 运行时目录，用于存储用户运行时文件的目录。

20. _=/usr/bin/env：

	- 最后执行的命令。

21. OLDPWD=/var/www/html：

	- 上一个工作目录的路径。

这些环境变量在系统中用于配置和控制各种操作，它们提供了关于系统和用户环境的重要信息。

#### 变量
计算机中的变量就是需要变化的东西，不固定的东西
当前值是这个，但是可以改变

#### 常量
固定不变的，比如某个数值，圆周率这种


### 声明环境变量export

```
export LANG=en_US.UTF-8
env
```
![[Pasted image 20231217220251.png]]
![[Pasted image 20231217220258.png]]
展示就会变成全英文

### 解析变量双引号“” 和不解析变量单引号''
```
echo "$LANG"
```
```
[root@localhost ~]# echo "$LANG"
en_US.UTF-8
[root@localhost ~]# echo '$LANG"
> ^C
[root@localhost ~]# echo '$LANG'
$LANG
```

常量的值是固定的
变量的值是不固定的

### 转义符\
用于将一些linux默认设定的一些符号变为符号本来的意思

### 路径分隔符/

### 历史命令调用！
```
history
!225 # 执行255号命令
```

### 通配符*
```
ls *.txt
```
windows中也是有的

### $调用变量
```
echo $HISTSIZE
echo HISTSIZE
echo $alkdjfladhg # 输出是空
```

```
[root@localhost ~]# echo $HISTSIZE
1000
[root@localhost ~]# echo HISTSIZE
HISTSIZE
```

这引申出一个错误用法
```
rm -rf $akldjfl/*
```
这时候前边的部分是空，所以就会删除root

**如何声明一个变量**
```
sab=/tmp
echo $sab
```


### 重定向
#### 输出重定向>
#### 输出追加重定向>>
#### 输入重定向 <
#### 输入追加重定向 <<

### 管道|

### ||二选一，前一个命令失败了就执行第二个
```
echo 123||echo 119
ech 192|| echo 123
```

### && 和，一起执行
```
echo 123 && echo 456
```
第一个失败了第二个也不执行
要么一起要么一起不启动
```
ech 123 && echo 123
```

##### 和；的区别

分号其实是每个命令后边默认会执行的内容
其实就是把两行写成一行
```
echo 12;
echo 122
echo 12 ; echo 123
```
所以两者之间有区别，&&两个命令之间会前后影响，分号；不会影响而是分别执行

### & 放后台运行
```
top
top &
ps -ef|grep top
```
```
[root@localhost ~]# top &
[1] 17070
```

### ~代表家目录，当前用户下
```
cd
cd ~
# 两个操作都是回到家目录
```

### 反引号
用来嵌套命令的
之前如果想要打包所有结尾是conf的文件在一个压缩包里面
```
find /etc -type f -name "*.conf" -exec tar -zcf /tmp/etc.tar.gz {} \;
```
这时候的输出是只有一个文件被正确打包，这时候我们就可以使用嵌套
嵌套是先执行反引号内部的命令再执行外部的 
![[Pasted image 20231217222902.png]]
```
tar -zcf /tmp/etc.tar.gz `find /etc -type f -name "*.conf"`
tar -tf /tmp/etc.tar.gz
```
![[Pasted image 20231217223011.png]]
就会显示出许多文件了



# 总结特殊符号

```
- # 注释
- ; 执行多条命令
- .. 上级目录
- . 当前目录
- "" 识别变量的多行输入
- '' 不识别变量多行输入
- ` 嵌套命令
- ! 执行历史命令
- \ 转义符
- / 路径分隔符
- * 通配符
- $ 执行环境变量
- > 重定向系列
- >>
- <
- <<
- | 管道符
- || 或执行
- && 同时执行
- & 放后台执行
- ~ 家目录
```

![[Pasted image 20231217223510.png]]
使坏
网络可以输入命令的时候
使用分号就会操作服务器
如果权限非常大
就可能有很大的漏洞