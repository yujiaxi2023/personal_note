创建一个环境，也就是一个文件包含一些内容

```
[root@localhost greptut]# head -50 /etc/services >test.txt
[root@localhost greptut]# ls
test.txt
[root@localhost greptut]# cat test.txt 
# /etc/services:
# $Id: services,v 1.55 2013/04/14 ovasik Exp $
#
# Network services, Internet style
# IANA services version: last updated 2013-04-10
#
# Note that it is presently the policy of IANA to assign a single well-known
# port number for both TCP and UDP; hence, most entries here have two entries
# even if the protocol doesn't support UDP operations.
# Updated from RFC 1700, ``Assigned Numbers'' (October 1994).  Not all ports
# are included, only the more common ones.
#
# The latest IANA port assignments can be gotten from
#       http://www.iana.org/assignments/port-numbers
# The Well Known Ports are those from 0 through 1023.
# The Registered Ports are those from 1024 through 49151
# The Dynamic and/or Private Ports are those from 49152 through 65535
#
# Each line describes one service, and is of the form:
#
# service-name  port/protocol  [aliases ...]   [# comment]

tcpmux          1/tcp                           # TCP port service multiplexer
tcpmux          1/udp                           # TCP port service multiplexer
rje             5/tcp                           # Remote Job Entry
rje             5/udp                           # Remote Job Entry
echo            7/tcp
echo            7/udp
discard         9/tcp           sink null
discard         9/udp           sink null
systat          11/tcp          users
systat          11/udp          users
daytime         13/tcp
daytime         13/udp
qotd            17/tcp          quote
qotd            17/udp          quote
msp             18/tcp                          # message send protocol (historic)
msp             18/udp                          # message send protocol (historic)
chargen         19/tcp          ttytst source
chargen         19/udp          ttytst source
ftp-data        20/tcp
ftp-data        20/udp
# 21 is registered to ftp, but also used by fsp
ftp             21/tcp
ftp             21/udp          fsp fspd
ssh             22/tcp                          # The Secure Shell (SSH) Protocol
ssh             22/udp                          # The Secure Shell (SSH) Protocol
telnet          23/tcp
telnet          23/udp
# 24 - private mail system

```

##### -n 行号标注关键字
```
grep -n 'tcp' test.txt
```
![[Pasted image 20231217235914.png]]
知道了行号，我就想去到这一行去查看细节内容
```
vim test.txt +48
```
就来到了48行

##### -c 对结果进行计数
```
grep -c 'tcp' test.txt
```
```
[root@localhost greptut]# grep -c 'tcp' test.txt
14
```
```
grep -n 'tcp' test.txt | wc -l
```
产生结果是一样的

##### -i 不区分大小写
```
grep -n 'tcp' -i test.txt
```
![[Pasted image 20231218000503.png]]
这样取到的结果不区分大小写

##### -v 取反
```
find / ! -type f
```
在find软件中感叹号！是取反，这里代表除了文件类型都要
```
grep 'udp' test.txt
```
![[Pasted image 20231218000705.png]]
```
grep -v 'udp' test.txt
```
![[Pasted image 20231218000738.png]]


##### -w 精准匹配
```
grep -w 'tcp' test.txt
```
![[Pasted image 20231218000826.png]]
只有整个词是对的才会匹配，只是一部分就不匹配了

##### -o 只显示匹配的结果
```
grep -o 'tcp' test.txt
```
```
grep -ow 'tcp' test.txt
```
用一点正则
```
grep -owE '..p' test.txt
```
![[Pasted image 20231218001026.png]]
配合正则展现结果

##### -A 1 同时输出搜索结果的后几行 after
```
grep 'ftp' test.txt
```
![[Pasted image 20231218001152.png]]

```
grep -A 2 'ftp' test.txt
```
![[Pasted image 20231218001141.png]]
这里就可以显示最后一行后两行也输出出来

##### -B 1 同时输出搜索结果的前几行 before
```
grep 'ftp' test.txt
```
```
grep -B 2 'ftp' test.txt
```
![[Pasted image 20231218001431.png]]

##### -C  2 同时搜索结果的上下行都显示
```
grep 'ftp' test.txt
```
```
grep -C 2 'ftp' test.txt
```
![[Pasted image 20231218001521.png]]

##### -E 扩展正则表达式

```
grep -E 'ssh|ftp' test.txt
```
![[Pasted image 20231218001612.png]]
如果没有参数E，结果就会报错

##### -P 后边接正则 使用perl正则
```
grep -P "\d+" test.txt
```
提取出数字，连续的
![[Pasted image 20231218001724.png]]
```
grep -P "\d{4,}" test.txt
```
获得四位数以上的数字
使用perl正则

## 总结
```
# 擅长过滤
# grep参数
# 按照整行过滤
-n 行号
-c 对结果进行计数
-i 不区分大小写
-v 反向搜索，取反
-w 精准匹配
-o 只显示匹配的结果
-A1 同时打印搜索结果行的后一列
-B3 同时打印搜索结果行的前三行
-C2 同时打印搜索结果行的上下各两行
-E 扩展正则表达式
```