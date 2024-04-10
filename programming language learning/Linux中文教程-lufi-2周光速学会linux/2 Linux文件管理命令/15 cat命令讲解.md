### cat命令

cat命令主要查看内容比较少的纯文本
单词是concatenate,可以连接多个文件内容显示到屏幕上,或者进行重定向

cat功能

| 功能           | 说明                                        |
| ------------ | ----------------------------------------- |
| 查看文件内容       | cat file.txt                              |
| 多个文件合并       | cat file.txt file2.txt > file3.txt        |
| 非交互式编辑或者追加内容 | cat >> file.txt << EOF <br>欢迎来到abc<br>EOF |
| 清空文件内容       | cat /dev/null > file.txt 前面这个是linux系统黑洞文件 |

参数:
```
用法 cat [选项] [文件]...
将文件或者标准输入组合输出到标准输出

清空文件内容,慎用
> 文件名

-A, --show-all 等价于 -vET
-b, --number-nonblank 对非空输出行编号
-e             等价于-vE
-E, --show-ends 在每行结束处显示$
-n, --number 对输出的所有行编号
-s, --squeeze-blank 不输出多行空行
-t             等价于-vT
-T, --show-tabs 将跳格字符显示为^I
-u             (被忽略)
-v, --show-nonprinting 使用^和M-引用,除了LFD和TAB除外
--help
--version

如果文件缺少,或者文件为-,就读取标准输入
```

案例:
1. cat功能参数用法
```shell
1. 查看文本内容,以及功能参数
cat gushi.txt

2. 对非空行显示行号
cat -b gushi.txt # 对非空的行进行编号

3. 对所有行显示行号
cat -n gushi.txt

4. 对所有行尾做$标识
cat -E gushi.txt

5. 不输出多行空行,减少空行数量
cat -s gushi.txt
```

2. cat合成多个文件
```shell
1. 同时看多个文件
cat gushi.txt yu.txt

2. 多个文件内容合并成一个
cat gushi.txt yu.txt > ./yugushi.txt

3. 非交互式编辑和追加内容
cat >> gushi.txt << EOF
> afafd
> adfkjlj
> EOF
```
```shell
4. 清空文件用法
echo > gushi.txt # 这个还有一个空行

5. 直接清空文件内容,没有空行
> gushi.txt

6. 利用cat读取黑洞文件,然后清空其他文本
cat /dev/null
```
