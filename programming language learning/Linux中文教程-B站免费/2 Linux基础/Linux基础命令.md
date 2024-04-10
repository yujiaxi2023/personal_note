![[Pasted image 20230401163933.png]]
所有文件都在根目录 /之下
![[Pasted image 20230401164048.png]]
windows中对于路径的描述如上图
Linux中描述为下图所示
![[Pasted image 20230401164150.png]]
练习题
![[Pasted image 20230401164305.png]]
```practice
\test\hello.txt
\itheima.txt
\itcast\itheima\hello.txt
```

**Linux命令入门**
![[Pasted image 20230401164643.png]]
![[Pasted image 20230401165121.png]]
命令是存在3个部分，有命令本身，后面的选项和参数并不是必选项

**小总结**
![[Pasted image 20230419151222.png]]

**ls命令**
命令本体是ls，option有alh三种，参数就是linux路径
![[Pasted image 20230401165326.png]]
![[Pasted image 20230401165441.png]]
home目录是账户目录
![[Pasted image 20230401165621.png]]


**小总结**
![[Pasted image 20230419151255.png]]

**ls命令的参数**
ls -a是展示所有的目录
ls -l是按照列表展示内容
选项是可以组合使用的
可以使用
ls -al或者是ls -la ls -l -a
ls -h 表示用易于阅读的方式展示文件的大小，例如k m g
![[Pasted image 20230401171807.png]]

**小总结**
![[Pasted image 20230419151326.png]]

**cd切换工作目录**
![[Pasted image 20230401171913.png]]
可以用cd更改当前的工作目录
如果不添加参数cd直接回到home目录上

**pwd命令**
![[Pasted image 20230401205204.png]]
查看当前工作目录

**相对路径和绝对路径**
![[Pasted image 20230401205338.png]]
![[Pasted image 20230401205352.png]]
![[Pasted image 20230401205602.png]]
. 代表当前目录 ..表示上一级目录 ~表示回到home目录

![[Pasted image 20230401210003.png]]
```practice
test/hello.txt
../test/hello.txt
~/test/hello.txt
```

**mkdir**
![[Pasted image 20230401210227.png]]
![[Pasted image 20230401210711.png]]
在home目录之外会报错，没有权限
![[Pasted image 20230401211333.png]]

**touch-cat-more**
![[Pasted image 20230401211418.png]]
![[Pasted image 20230401211532.png]]
标识为d的是文件夹，表示为-的是文件
![[Pasted image 20230401211612.png]]
![[Pasted image 20230401211706.png]]
more也可以查看内容
![[Pasted image 20230401211742.png]]
more相比于cat是他可以支持翻页功能，cat是全部文件展示

**小总结**
![[Pasted image 20230419151503.png]]

**cp-mv-re**
![[Pasted image 20230401212116.png]]
文件夹的复制需要带上选项-r

![[Pasted image 20230401212416.png]]
当mv对应的对象不存在时，会对参数1进行改名为参数2

![[Pasted image 20230401212725.png]]
删除文件夹需要添加-r的选项
删除多个目标

**小总结**
![[Pasted image 20230419151614.png]]


通配符
![[Pasted image 20230401213146.png]]
在前后添加✳可以让以这个字符结尾的文件消失
![[Pasted image 20230401213312.png]]
添加了r之后文件夹和文件都可以删除
![[Pasted image 20230401213607.png]]
在root模式下在删除文件的时候
![[Pasted image 20230402145611.png]]
rm -rf /* 表示在根目录下删除所有的文件夹，并且是强制删除

**which find**
![[Pasted image 20230402145926.png]]
which可以查询到命令的程序文件存放位置

![[Pasted image 20230402150251.png]]
find命令可以搜索制定文件
用文件名查找文件使用find 起始路径，例如用斜杠就是根目录，name就是查找文件名
root用户是拥有最大的权限，才能进行
![[Pasted image 20230402151324.png]]
![[Pasted image 20230402151646.png]]
还可以按照文件大小查找文件
用-size的命令，利用+-两个表示大小
在windows上面使用wsl虚拟环境的linux是不能够接入到windows的文件夹

**grep wc 管道符**
![[Pasted image 20230402152603.png]]
两个参数都是必填的
如果带有空格或者特殊符号使用“”包起来

![[Pasted image 20230402163019.png]]
图形化界面中编辑文本，需要对于文本中关键词进行过滤就需要greb命令
![[Pasted image 20230402163149.png]]
当使用greb搜索关键内容的时候就可以找出关键词所在的位置和标红

![[Pasted image 20230402163228.png]]
选项-c可以 统计字节数量，-m可以统计字符数量， -l统计行数， -w统计单词数量
![[Pasted image 20230402163358.png]]
2行 11个单词 59个字节 带上文件名

管道符
![[Pasted image 20230402164838.png]]
| 作用是将左边的结果作为右边的输入
![[Pasted image 20230402164952.png]]
如果grep命令没有文件路径，如果使用管道符，那前面的内容可以作为右边grep命令的输入
![[Pasted image 20230402165140.png]]
![[Pasted image 20230402165321.png]]
本来usr/bin中有很多文件，grep可以提取出
这里也说明了grep也可以提取不是文本内部的内容，也可以查找到文件夹或者文件名称
表示有1070行![[Pasted image 20230402165519.png]]
这表示了使用l表示这个里有多少行的文件，wc统计出有1090行文件代表了有1090个文件

**echo**
![[Pasted image 20230402171233.png]]
输出内容复杂的时候使用双引号
![[Pasted image 20230402171425.png]]
![[Pasted image 20230402171710.png]]
当‘’围绕一个字符的时候是执行这个命令
![[Pasted image 20230402171745.png]]
![[Pasted image 20230402171851.png]]
当使用>的时候在echo后面，就是将后面的内容覆盖到文件中去
就是把原本的内容清空
![[Pasted image 20230402172048.png]]
若使用>>的符号
![[Pasted image 20230402172128.png]]
则是如图所示的追加
只要是产生结果的都能够往后写
但是这个并不是专门为echo使用的命令，例如使用ls，然后覆盖或者添加进去，则文本中就会产生对应的内容
![[Pasted image 20230402172538.png]]

![[Pasted image 20230402172557.png]]
tail可以查看尾部内容，跟踪最新的更改
-f是表示持续跟踪，-num是跟踪几行，默认为10行
![[Pasted image 20230402172749.png]]
![[Pasted image 20230402172828.png]]
一旦后面添加上-数字，就可以看几行
![[Pasted image 20230402172951.png]]
![[Pasted image 20230402173010.png]]
如果是-f，在另外的选项卡中进行该文本的编辑内容，例如使用echo添加，就会在最后一行产生新的内容
一直跟踪不会 停止，如果想要停止就用ctrl c
![[Pasted image 20230402173218.png]]

![[Pasted image 20230402173656.png]]
```practice
echo "my work document:'pwd'" > work.txt
echo "content" >> work.txt
tail -f work.txt
```

**vi vim编辑器**
![[Pasted image 20230402184322.png]]
vim是比vi更先进的版本
![[Pasted image 20230402184641.png]]
命令模式是按键盘的快捷键就是执行不同的功能
输入模式是对于文本进行编辑
底线模式是对整体文件的控制，例如对文件保存和退出等

![[Pasted image 20230402185410.png]]
vim 文件路径就可以使用编辑器编辑文件

输入和底线模式无法互相转换
![[Pasted image 20230402185908.png]]
![[Pasted image 20230402185946.png]]
使用vim hello.txt是直接进入到命令模式
而且如果没有原文档会创建一个新的文档

![[Pasted image 20230402190054.png]]
键盘i键就进入到输入模式
如果我们要回退到命令模式,就esc就行
![[Pasted image 20230402190151.png]]
就回到原来的命令模式
ypp就是复制
dd就是删除
u就是撤销一次

:wq就是保存退出
如果只有w就是保存
如果只有q就是只有退出
![[Pasted image 20230402191000.png]]
一些常见的快捷建进入输入模式
![[Pasted image 20230402191852.png]]
0是移动光标到开头,并不是输入模式
$可以快速移动到当前行的结尾
/可以进入搜索模式,会把搜索的内容用高亮显示,但是动态的每次 只能显示一个
当回车之后,会需要辅助n作为向下,或者N作为向上搜索的命令
![[Pasted image 20230402192207.png]]
当触碰到最后一个的结果,如果依然向下寻找就会出现红字警告
![[Pasted image 20230402192611.png]]
已经搜索到底端,若继续n就会回到第一个结果

ndd就是删除下面的n行,dd就是删除当前行
yy是复制当前行 nyy就是复制当前行和下面的n行,注意,复制不是粘贴
p就是粘贴复制的内容,u就是撤销修改
ctrl r是反向撤销
gg就是跳到首航
G就是跳转行尾
dG就是当前行之下全部删除
dgg就是当前行向上全部删除
d$就是从当前光标到当前行结尾
d0就是当前光标一直删除到当前行开头

![[Pasted image 20230402193838.png]]
底线命令模式
set nu就会出现
![[Pasted image 20230402194042.png]]
如图所示的行号
set paste
当进入到insert模式后
![[Pasted image 20230402194140.png]]
就会在后面出现paste,确保你从外部复制的内容进入输入格式的时候不会出现格式的错乱

**小总结**
![[Pasted image 20230419151812.png]]
