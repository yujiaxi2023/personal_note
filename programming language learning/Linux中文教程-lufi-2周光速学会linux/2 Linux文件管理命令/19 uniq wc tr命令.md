### uniq 命令

uniq命令可以输出或者忽略文件中的重复行,常与sort排序结合使用
```
用法: uniq [选项]... [文件]
从输入文件或者标准输入中筛选相邻的匹配行写入到输出文件或者标准输出

不附加任何选项的时候匹配行将在首次出现的地方被合并

-c, --count 在每行前加上表示相应行目出现次数的前缀编号
-d, --repeated 只输出重复的行
-u, --unique 只显示出现过一次的行,是针对-c统计后的结果
```

案例:
```shell
1. 多行连续的时候进行去重
uniq filename.txt

2. 排序之后进行去重
sort -n luffy.txt | uniq

3. 重复行计数
sort -n luffy.txt | uniq -c 

4. 只统计重复的行,并且统计词书
sort -n luffy.txt | uniq -dc

5. 找出只出现过一次的行
sort -n luffy.txt | uniq -u
```

### wc 命令

用于统计文件的行数,单词,字节数

```
-c, --bytes 打印字节数
-m, --chars 打印字符数
-l, --lines 打印行数
-L, --max-line-length 打印最长行的长度
-w, --words 打印单词数
```

案例
```shell
1. 统计文件的行数
wc -l luffy.txt

2. 统计单词的数量
echo "alex wupeiqi cunzhang chaoge" | wc -w

3. 打印字符数, 会发现因为每行结尾都会有默认一个$, 所以结果是7
echo "chaoge" | wc -m # 这里的结果是7

4. 输出最长行的字符数
cat alex.txt | wc -l
who # 显示当前有几个终端登录
who | wc -l
```


### tr命令

tr命令是从标准输入中替换,缩减或者删除字符,将结果写入到标准输出

```
用法: tr [选项]... SET1 [SET2]
从标准输入中替换,缩减和删除字符,并将结果写入到标准输出

字符集1: 指定要转换或者删除的原字符集

当执行转换操作的时候,必须使用参数"字符集2"指定转换的目标字符集

但执行删除操作的时候,不需要参数"字符集2";

字符集2: 指定要转换成的目标字符集

-c, --complement 取代所有不属于第一字符集的字符;
-d, --delete 删除所有属于第一字符集的字符
-s, --squeeze-repeats 把连续重复的字符用单独一个字符表示
-t, --truncate-set1 先删除第一字符集较第二字符集多出的字符
```

案例

```shell
1. 将整个字符串大写
echo "my name is alex" | tr '[a-z]' '[A-Z]'

2. 使用-d删除参数
echo "my name is alex and i am 9999 years old" | tr -d '[a-z]'
echo "my name is alex and i am 9999 years old" | tr -d '0-9'

3. 把文件作为标准输入做字符替换
tr 'a' 'A' < file.txt

4. 删除多个连续重复的字符
echo "iiiii am alexxxx" | tr -s "iaxl"
```

