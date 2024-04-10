sed过滤
```
seq 5 >1.txt
sed '3p' 1.txt
vim 1.txt 修改3a
sed '/a/p' 1.txt
```
这个软件会默认全部输出，然后再匹配到的地方再输出一下
![[Pasted image 20231218002729.png]]
如何取消默认输出
##### -n 安静模式输出
```
sed -n '/a/p' 1.txt
```

```
sed -n 'tcp/p' test.txt |wc -l
```
这个跟grep出来显示的一样，但是sed一定不会有颜色显示
而且比较麻烦

##### d 删除指定行（动作）
```
sed -n 'tcp/d' test.txt
```
这下显示再屏幕上的就是没有tcp的内容了
但是这不是真实删掉里面的内容，原来的test.txt没有变化

##### -i 就会替换掉原来的行
```
sed -i 'tcp/d' test.txt
```
里面没有tcp，也就是保存修改文件

##### a 动作

```
sed -i "/udp/d" test.txt
cat -n test.txt
```
这样文件就剩下很少的行，只有#注释的行
```
sed -i "/^#/d" test.txt
```
接下来删除以#开头的行
所以文件就只剩下空行了
指定行数删除
```
sed "1,10d" test.txt
```

```
cat 1.txt
```
```
sed '3a dms' 1.txt
```
![[Pasted image 20231218003904.png]]

##### -i 在指定行前面加行
```
sed '4i dms' 1.txt
```
![[Pasted image 20231218003952.png]]
会发现2行前边多了一个内容

##### -s 替换
```
sed 's#3a#3#g' 1.txt
```
这就是把3a替换成3
这里使用了全局的替换global

如果我希望忽略大小写 需要**I**代表 ignore 大小写
```
sed 's#dms#SMD#g' 1.txt
```
![[Pasted image 20231218004144.png]]
这是没有忽略大小写，只把小写的dms替换成SMD
```
sed 's#dms#SMD#gI' 1.txt
```
这样大小写的dms都替换
![[Pasted image 20231218004235.png]]

如果不要global，就替换最开始的一次
![[Pasted image 20231218004355.png]]

##### -p 动作 打印 一般和-n一起使用，因为不用-n就会显示很多行

```
sed -n '1,5p' test.txt
```
如果只写一个行号，就只打印一个行号






## 总结
```
# 擅长修改
用法：sed [-nri] [动作] 目标文件文件
选项和参数：
-n ：使用安静（silent）模式。在一般sed的用法中，所有来自于STDIN的数据一般都会被列出到终端上。但是如果加上-n参数后，只有经过sed特殊处理的那一行（或动作）才会被列举出来
-r ：sed的动作支持的是延伸性正规表示法的语法。（默认是基础正规表示法语法）
-i ：直接修改读取的文件内容，而不是输出到终端

动作说明：[n1[,n2]] function
n1 n2一般表示为行号，这里中括号表示可选，n2可以要可以不要

function：
a ： 指定行后边插入一行
d ： 删除
i ： 指定行前边插入一行
p ： 打印 # 一般和前边的-n参数一起使用
s ： 替换 需要I忽略大小写，全局替换需要g
```