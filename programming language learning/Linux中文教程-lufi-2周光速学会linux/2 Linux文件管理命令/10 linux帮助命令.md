### man帮助命令
```shell
语法
man 命令

例如
man rm
```
![[Pasted image 20240313141352.png]]

### --help参数
```shell
用法
rm --help

精简版help
```

### help 命令
```shell
help rm
```

### info命令
```shell
info rm
```

### 互联网获取

可以搜索汉化版本

### linux开关机命令

### shutdown重启或者关机

```shell
shutdown help
```

### 重启

```shell
shutdown -r 10 # 10分钟后重启
shutdown -r 0 # 立刻重启
shutdown -r now # 立刻重启
```

### 关机

```shell
shutdown -h --halt 停止的含义

shutdown -h 10 # 10分钟后关机
shutdown -h 0
shutdown -h now # 立即关机
```

halt, poweroff, reboot命令关机和重启
```shell
reboot # 重启
```
```shell
powerof

halt # 关机
```

### 关机,重启,注销命令列表
| 命令              | 说明                   |
| --------------- | -------------------- |
| shutdown -h now | 立刻关机,企业用法            |
| shutdown -h 1   | 1分钟后关机,也可以写时间例如11:30 |
| halt            | 立刻关闭系统,需要手动切断电源      |
| init 0          | 切换运行级别为0, 0 表示关机     |
| poweroff        | 立刻关闭系统, 且关闭电源        |
| 重启              |                      |
| reboot          | 立刻重启机器,企业用法          |
| shutdown -r now | 立刻重启,企业用法            |
| shutdown -r 1   | 1分钟后重启               |
| init 6          | 切换运行级别为6,这个级别是重启     |
| 注销命令            |                      |
| logout          | 注销退出当前用户             |
| exit            | 注销退出当前用户,快捷键ctrl + d |

### Linux 命令行常用快捷键

```
CTRL + c 中断当前操作
CTRL + l 清空屏幕内容
CTRL + d 退出当前用户=logout
CTRL + a 光标移动到行首
CTRL + e 光标移动到行尾
CTRL + u 光标前的内容删除
```

### Linux环境变量

windows下的环境变量PATH, 系统会按照PATH的设定,到每个PATH定义的目录下自动搜索可执行文件
如何查看linux的PATH变量

```shell
echo 打印内容 # 输出打印的内容
echo PATH # 这样是简单的打印PATH字符信息
echo $PATH # 这样会出现一些结果
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
which ls # 会显示ls在哪个目录
alias rm='rm -i'
	/usr/bin/rm
```
PATH一定是大写的变量,是由很多的目录组成,分隔符是:号,并不是windows的;号
