### mkdir命令
```
mkdir make directory 创建文件夹
语法
mkdir 文件夹名称

参数用法
-p 递归创建文件夹
```
```shell
mkdir {A,B} # 可以同时创建多个文件夹
mkdir ./alex/A/B # 这个命令不行
mkdir -p ./alex/A/B # 需要添加参数-p才行
```

创建一百个文件夹命令
会把下面的命令转换为mkdir创建100次的命令
实际上是要给bash脚本
```shell
mkdir A{1..100}
```