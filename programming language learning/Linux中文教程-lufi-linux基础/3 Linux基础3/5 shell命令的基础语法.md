
## shell命令的基础语法

linux的shell命令：

### 格式1

命令后边啥也不接
例子：
```
ls
pwd
id
```
可以无参数执行的命令

### 格式2

命令后带1个参数
例子：
```
ls -a
ls -l
usermod -h
usermod -L
usermod --help
```
这里参数有短参数和长参数
功能是等效的

### 格式3

命令后带多个参数的
例子：
```
ls -a     -l    -h # 我们可以中间空格空很多个都不影响
# 多个参数可以合并
ls -alh
```

### 格式4

命令带参数 然后带1个目标
例子：
```
ls -l /boot
rm -fr /tmp/* # 这时候用相对路径比较容易出事
# 要注意有的版本的时候如果/tmp不存在，有可能就会直接/*删掉根
# 这样非常危险
```

### 格式5

命令只带有一个目标
```
cd /tmp
ls /tmp
mkdir test
useradd dms
```

### 格式6

命令带多个目标
```
cp -r /tmp /root 复制目录
touch {1..10}.txt
cp 1.txt 2.txt 3.txt /tmp # 是多个目标复制到文件夹，后边必须是文件夹
```


### 格式7

命令带多个参数多个目标
```
ls -alh /tmp /boot /opt
cp -av /root /root2
```


### shell的基础语法

```
命令     参数     目标
ls       -a -l    /opt
rm       -rf      /opt/test1


命令      目标1      目标2
mv        源路径     目标路径
cp

命令
reboot

用法：mv [选项]··· [-T] 源文件 目标文件
或者：mv [选项]··· 源文件··· 目录
或者：mv [选项]··· -t 目录 源文件···

# 格式解释
[选项] 可选择
···· 可以有多个
```