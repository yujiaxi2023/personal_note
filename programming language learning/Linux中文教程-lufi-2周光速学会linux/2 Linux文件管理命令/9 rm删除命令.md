### mv命令
```
mv就是move,是移动或者重命名文件

用法:
mv [选项]... [-T] 源文件 目标文件
mv [选项]... 源文件... 目录
mv [选项]... -t 目录 源文件...
将源文件重命名为目标文件,或者将源文件移动到指定目录

-f, --force 覆盖前不询问
-i, --interactive 覆盖前询问
```

```shell
# 1. 移动一个文件到另一个文件夹
mv ./dms.txt ./oldboy # 当前文件夹的txt移动到oldboy

# 2. 移动所有luffy开头的文件,使用通配符
mv luffy* ./oldboy

# 3. 重命名作用
mv 之前文件 重命名后文件
mv dms.txt A.txt 

# 4. 覆盖前询问,mv实际上系统中做了alias别名,其实是mv -i
mv -i dms.txt dms1.txt # dms1存在

# 5. 强制覆盖
mv -f dms.txt dms1.txt
```

### rm命令
```
rm命令就是remove的含义,删除一个或者多个文件,是linux系统重要命令

选项
-f, --force 强制删除,忽略不存在的文件,不提示确认
-i 删除前需要确认
-I 删除超过3个文件或者递归删除前需要确认
-d, --dir 删除空目录
-r, -R, --recursive 递归删除目录和内容
-v, --verbose 详细显示进行的步骤
--help 显示帮助信息并推出
--version 显示版本信息并推出
```

```shell
# 1. 删除普通文件，alias添加了-i进行确认
rm dms.txt  # 删除前会提问，是否会删除

# 2. 一次性删除多个文件
rm chaoge.txt.2 chaoge.txt.3 # 删除多个文件，写入多个文件名，空格分隔

# 3. 删除多个文件夹，必须添加-r才能删除
rm -r mjj # mjj删除文件夹，和里面的内容

# 4. 删除空目录-d
rm -d mjj2 # 不能删除有内容的文件夹
mkdir ilovelinux
rm -d ilovelinux/

# 5. 强制删除文件，并且不提示
rm -f mjj* # 强制删除mjj开头的文件，并不能删除文件夹

# 6. 强制删除所有文件和文件夹
rm -fr ./* # 强制删除当前文件夹所有内容，注意不是删除根目录

# 7. 详细显示删除的过程-v
touch alex mjj cunzhang
mkdir -p ./luffy/yuchao/chaochao
rm -rfv ./* # 强制删除当前目录内容并显示所有过程
```
![[Pasted image 20240313134822.png]]
