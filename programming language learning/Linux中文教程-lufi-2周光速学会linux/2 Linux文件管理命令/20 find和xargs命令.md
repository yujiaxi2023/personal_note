### stat命令

stat命令用于显示文件的状态信息, stat命令输出的信息比ls命令输出的信息要更详细

语法
```
stat [选项] [参数]
```

选项
```
-L, --dereference 跟随连接
-f, --file-system 显示文件系统状态而不是文件状态
-c, --format=格式 使用指定输出格式代替默认值,每使用一次指定格式换一行
    --printf=格式 类似--format,但是会解释反斜杠转义符,不使用换行作为输出结尾,如果希望使用换行,可以在格式中加入"\n"
-t, --terse 使用简洁格式输出
    --help 显示此帮助信息并退出
    --version 显示版本信息并退出

有效的文件格式序列(不使用 --file-system):
%a 八进制权限
```

参数
文件:指定要显示信息的普通文件或者文件系统对应的设备文件名

```
stat alex.txt # 比较关心的是访问时间,修改时间,更改时间3个属性
```
![[Pasted image 20240315143702.png]]

### find命令

find命令用在指定目录下查找文件, 任何位于参数之前的字符串都将是为需要查找的目录名称

如果使用该命令的时候, 不设置任何参数, 则find命令将在当前目录下查找子目录和文件

并且将查找到的子目录和文件全部进行显示

```
find 处理符号连接 要查找的路径 参数 限定条件 执行动作
find -H -L -P    PATH        options tests actions
```

语法
```
find 查找目录和文件, 语法:
find 路径 -命令参数 [输出形式]

参数说明:
路径: 告诉find在那里去找你要的东西
```

| 参数               | 解释                                                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| pathname         | 要查找的路径                                                                                                                               |
| options 选项       |                                                                                                                                      |
| -maxdepth        | <目录层级>: 设置最大目录层级                                                                                                                     |
| -mindepth        | <目录层级>: 设置最小目录层级                                                                                                                     |
| tests 模块         |                                                                                                                                      |
| -atime           | 按照文件访问access的时间查找,单位是天                                                                                                               |
| -ctime           | 按照文件的改变change状态来查找,单位是天                                                                                                              |
| -mtime           | 根据文件修改modify时间查找文件,最常用                                                                                                               |
| -name            | 按照文件的名字查找,支持通配符搜索                                                                                                                    |
| -group           | 按照文件的属组搜索                                                                                                                            |
| -perm            | 按照文件的权限查找                                                                                                                            |
| -size n`[cwbkMG` | 按照文件的大小 为n个由后缀决定的数据块<br>其中后缀为:<br>b:代表512位元组的区块(如果用户没有指定后缀,则默认为b)<br>c:代表字节数<br>k:表示kilobytes(1024字节)<br>w:字(2字节)<br>M:兆字节<br>G:千兆字节 |
| -type 查找某一类型的文件  | b-块设备文件<br>d-目录<br>c-字符设备文件<br>p-管道文件<br>l-符号链接文件<br>f-普通文件<br>s-socket文件                                                            |
| -user            | 按照文件属主来查找文件                                                                                                                          |
| -path            | 配合-prune参数排除指定目录                                                                                                                     |
| Actions模块        |                                                                                                                                      |
| -prune           | 使find命令不在指定的目录寻找                                                                                                                     |
| -delete          | 删除找出的文件                                                                                                                              |
| -exec或者-ok       | 对匹配的文件执行相应的shell命令                                                                                                                   |
| -print           | 将匹配的结果标准输出                                                                                                                           |
| OPERATORS        |                                                                                                                                      |
| !                | 取反                                                                                                                                   |
| -a -o            | 取交集,并集,作用类似&&和\                                                                                                                      |

```shell
1. 根据名字进行全盘搜索
find / -name "*.txt"

2. 指定目录搜索
find /opt -name "*.txt"

3.只寻找最大深度是1的文件夹的txt文件
find /opt -maxdepth 1 -name "*txt" 

4. 搜索一定规律的文件
touch {1..10}alex.txt
find . -name "[0-9]"
mkdir {1..10}mjj
find . -name "[0-9]" # 这样会找出所有的文件和文件夹
find . -type f -name "[0-9]" # 这样只会找出file
find . -type f -name "[0-9]" # 这样只会找出file
find . -type f -name "[0-9]*" -delete # 这样会删除掉这些内容

5. 根据访问时间戳搜索
find . -atime -2 # 搜索两天以内被访问的文件
"""
时间说明
-atime -2 搜索在2天内访问过的文件
-atime 2 搜索恰好在2天前访问过的文件
-atime +2 搜索超过2天内被访问的文件
"""

6. 组合按照访问时间戳查找
find . -type f atime -2
find . -type f atime 2
find . -type f atime +2

7. 反向查找
find . -maxdepth 1 ! -type d # 找到除了文件夹以外的类型

8. 根据文件夹大小搜索
find . -type f -size +200M # 搜索超过200M的文件
find . -maxdepth 2 -type f -size +200M # 搜索超过200M的文件

9. 忽略文件夹搜索
find . -path "./test_find" -prune -o -name "*.txt" -print
```
![[Pasted image 20240315154512.png]]
```shell
10. 执行-ok动作
find . type f -name "*.txt" -ok rm {} \; # 执行rm命令删除搜索到的文件
```


### xargs命令

xargs又称管道命令,构造参数等
是给命令传递参数的一个过滤器,也是组合多个命令的一个工具它把一个数据流分割为一些足够小的块,以方便过滤器和命令进行处理

简单的就是将其他命令的标准输出作为标准输入传递给沟边的命令
```
-d 位输入指定一个定制的分隔符,默认是空格
-i 用{}代替 传递的数据
-I string 用string来代替传递的数据-n[数字] 设置每次传递几行数据
-n 选项限制单个命令行的参数个数
-t 显示执行详情
-p 交互模式
-P n 允许的最大线程数量是n
-s [大小] 设置传递参数的最大字节数(小于)
-x 大于 -s 设置的最大长度结束 xargs命令执行
-0, --null 用null分隔,为不是空白,禁用引号和反斜杠处理
```

```shell
1. 多行数据变为一行数据
xargs < chaoge.txt # 直接就可以变为一阿航数据

2. 限制每行输出个数 -n用法
xargs -n 2 < chaoge.txt

3. 按照指定符号,进行拆分 -d用法
echo "alex,mjj,chaoge,cunzhang" | xargs -d "," -n 2

4. 将所有的txt文件,移动到alltmptxt目录中-i用法
find . -name "*.txt" | xargs -i mv {} alltmptxt/ # 花括号代表前边的内容

5. 将上边的文件移动出来 -I用法
find . -name "*.txt" | xargs -I alltxt mv alltxt ./
# 将找到的文件命名为一个字符串然后将它移动到./中

```