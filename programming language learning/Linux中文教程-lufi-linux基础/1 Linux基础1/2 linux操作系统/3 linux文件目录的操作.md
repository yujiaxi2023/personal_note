- 查看文件 ls（list）
- 新建文件 touch 文件名
```
touch dms.txt
```
一次性创建批量文件
```
touch {1..10}.txt
touch {a..f}.txt
```

- 删除文件 （linux没有回收站，所以比较危险）rm
```
rm b.txt c.txt e.txt
rm -f b.txt c.txt e.txt 强制删除-f force
rm -f {1..10}.txt
```

- 复制文件（第二个文件需要重命名）cp（copy）
```
cp anaconda-ks.cfg copy1.cfg
# 第二个参数还可以指定文件夹
```

- 文件重命名mv（move）
```
mv copy1.cfg copy_1.cfg
```

## 目录（其实就是文件夹）

- 创建文件夹mkdir 目录名称
```
mkdir 目录名称
```

- 进入路径cd 路径（相对路径/绝对路径）
```
cd 路径名称
```
```
# 去上一级目录
cd ..
```

- 重命名目录mv
```
mv 文件夹名字 新名字
```

- 复制目录 cp
```
cp -a 目录名 新目录名字
```
这是复制所有文件夹的内容

- 删除目录rm
```
rm -f -r 目录名称
rm -rf 目录名称
```


## 操作回顾

- pwd 在win下面是分盘的，在linux里面只有一个盘 打印当前目录
```
/ 顶级目录
/root
```

- ls 展示文件
```
touch {1..100}.txt
ls
# 展示大量的文件 默认显示1个文件名 

ls -l
# 展示很多信息和创建时间 还有权限名称等

ls *.txt
# 可以找到特定后缀名的文件

ls -1
# 按照一行1个的方式进行展示
# 不可以使用2和以上的别的数字

ls -a
# 查看所有文件并包含隐藏文件
touch .1.txt
# 用.开头就可以创建隐藏文件

ls -a -1
# 叠加效果，看隐藏文件并由隐藏文件
```

- mkdir
```
mkdir -p 1/2/3/4
# 创建多级目录 parent会自动创建父目录
mkdir dev{01..10}
# 创建同级多个目录
```

