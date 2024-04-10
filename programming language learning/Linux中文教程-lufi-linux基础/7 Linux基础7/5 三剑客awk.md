awk默认使用空格作为分隔符
```
[root@localhost greptut]# awk '{print $1}' 1.txt 
2
3
This's
10
```
需要使用`{print $1}`才可以显示出第一列
需要更改要输出的列就是改数字就行了
如果没有这一列就会显示空白

**最后一列$NF**
```
awk '{print $NF}' 2.txt
```
这就会自动显示每一行的最后一列

如果我想要复数的列数
```
awk '{print $1,$NF}' 2.txt
```
会默认按照从左往右的顺序展示，先展示第一列再展示最后一列

```
[root@localhost greptut]# echo "orange 10 100
> apple 20 50
> mongo 50 20
> banana 5 200" > 2.txt
[root@localhost greptut]# cat 2.txt 
orange 10 100
apple 20 50
mongo 50 20
banana 5 200
[root@localhost greptut]# awk '{print $1"总价值:",$2*$3}' 2.txt 
orange总价值: 1000
apple总价值: 1000
mongo总价值: 1000
banana总价值: 1000
```
实现一个简单的计算价值

双引号中的内容是原样输出

= 代表变量赋值
== 代表判断 a == 1
```
awk 'NR==1' 2.txt
awk 'NR<3' 2.txt
```

打印指定行

过滤内容
```
grep 'apple' 2.txt
sed -n '/apple/p' 2.txt
awk '/apple/' 2.txt
```

取行号
```
sed -n '1,2p' 2.txt
awk 'NR>0 && NR<3' 2.txt
awk 'NR<3' 2.txt
awk 'NR<=2' 2.txt
```

##### -F 指定分隔符

**很多时候不是默认使用空格做分隔符，而是使用冒号：做分隔符**
```
awk -F ":" 'NR==1{print $1}' /etc/passwd
```


**文本拼凑**

双引号中间的内容按照原样进行输出

```
awk -F ":" '{print $1":123:"$7}' /etc/passwd
```

**过滤文本**
```
awk -F "[ /]+" '$2~/^47/' 1.txt
```

```
awk -F ":" '$1~/h/{print $1,$7}' /etc/passwd
```
就可以检查出第一列有h的，并列举出来

**按照行号筛选**
```
awk 'NR<=3{print $0}' 1.txt # > < == >= <=
```

