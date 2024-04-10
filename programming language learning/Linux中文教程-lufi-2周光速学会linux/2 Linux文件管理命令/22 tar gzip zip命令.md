### tar命令
tar命令在linux系统里面,可以实现对多个文件进行,压缩,打包,解包

打包
将一大堆文件或者目录汇总成一个整体

压缩
将大文件压缩成小文件,节省磁盘空间

```
语法
tar [选项] [参数]

-A, --catenate 新增文件到已经存在的备份文件
-B 设置区块的大小
-c, --create 建立新的备份文件
-C <目录> 这个选项用在解压缩,如果要在特定目录解压缩,可以使用这个选项
-d 记录文件的差别
-x, --extract或者--get 从备份文件中还原文件
-t, --list 列出备份文件的内容
-z, --gzip或者ungzip 通过gzip指令处理备份文件
-Z, --compress或者--uncompress 通过compress指令处理备份文件
-f<备份文件>或者--file=<备份文件> 指定备份文件
-v, --verbose 显示指令执行过程
-r, 添加文件到已经压缩文件
-u, 添加改变了和现有的文件到已经存在的压缩文件
-j, 支持bzip2解压文件
-v, 显示操作过程
-l, 文件系统边界设置
-k, 保留原有文件不覆盖
-m, 保留文件不被覆盖
-w, 确认压缩文件的正确性
-p, --same-permissions 用原来的文件权限还原文件
-P, --absolute-names 文件名使用绝对名称,不移除文件名称前的"/"号,不建议使用
-N <日期格式> 或者--newer=<日期时间> 只将较指定日期更新的文件保存到备份文件中
--exclude=<范本样式> 排除符合范本样式的文件
-h, --dereference 跟踪符号链接,将它们所指向的文件归档输出
```

案例
仅打包不压缩
```shell
tar 参数 包裹文件名 需要打包的文件
tar -cvf alltmp.tar ./*
```
打包后用gzip命令压缩,节省磁盘空间
```shell
tar -zcvf alltmp.tar ./*
```
解包命令
```shell
tar -xvf ../alltmp.tar ./
```

列出文件中的内容
```shell
tar -ztvf alltmp2.tar.gz
```

单独拆开和取出压缩文件的内容
```shell
1. 拆开单独的压缩文件
tar -zxvf alltmp2.tar.gz ./开心.txt # 拆除开心的文件
2. 显示单独的压缩文件
tar -ztvf alltmp2.tar.gz ./kx.txt # 显示压缩包中某个文件
3. 解压缩到指定目录
tar -zxvf alltmp2.tar.gz -C ./alltmp/ 
4. 排除文件解压缩
tar -ztvf alltmp2.tar.gz
tar -zxvf alltmp2.tar.gz --exclude alex.txt
5. tar压缩快捷方式的源文件,而不是快捷方式
tar -xvf alltmp.tar
tar -cf kx.tar ./kx.txt
ll # 显示的是软连接压缩了
# 现在需要压缩源文件
tar -zchf kx2.tar.gz ./kx.txt
tar -ztvf kx2.tar.gz # 这样里面就是源文件了
```


### gzip命令

```shell
1. 对当前所有txt进行gzip压缩
gzip ./*.txt
ll
# 显示的是一个txt压缩成一个gz文件
# gzip必须在tar打包文件夹后才能压缩文件夹

2. 列出压缩的内容
gzip -l alex.txt.gz
```

### zip命令

简单进行压缩解压缩命令
```shell
zip alltmp.zip ./*

unzip alltmp.zip
```