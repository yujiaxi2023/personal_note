我们完全可以将编译好的东西打包
然后传输到另一个机器的相同目录下，就可以实现运行
```
tar -zcf /tmp/nginx_dms.tar.gz # 代表当前目录已经编译好了
ll -h /tmp
```
![[Pasted image 20231216184358.png]]
```
scp nginx_dms.tar.gz root@ip addr:/tmp
# 输入密码就推送过去
```
接下来进入到另一台机器
```
cd /tmp
ll -h
```
然后将文件挪到之前的目录下
```
mv ngnix_dms.tar.gz /usr/local/
ll -h /usr/local
tar -zxf nginx_dms.tar.gz
ls
pwd
/usr/local/nginx/sbin/nginx
# 然后就启动了
# 同样的看防火墙是否关着
# 关着才会能被浏览器请求到
```

所以这说明了，只要有一个人编译了，就不需要每个人都下载源代码
所以linux厂商就发现了
redhat系列：rpm redhat package manager
debian系列：deb

### tree查看当前命令
```
tree 
```
啥也不接就是查看当前目录

### rpm安装
```
# redhat package manager rpm
# 我们可以去镜像站找到rpm文件
wget 下载url
找到当前目录下的rpm文件
rpm -ivh tree.rpm（rpm文件）
```
接下来就可以使用tree的命令了
只要我们有rpm包
### rpm卸载
```
rpm -e tree
```
这样就可以卸载掉软件

rpm安装软件有一个问题
如果稍微复杂的软件，需要有依赖包
我们需要先装上依赖包，一层一层的不停的装到所有的依赖包
这个就非常麻烦了

### yum安装
```
yum install vim -y
```
yum会自动分析需要什么依赖包，提前按照逻辑安装好依赖包


# 安装的问题

- 源码编译：可以定制（而且不知道平台，所以有可能找错系统平台等）
- rpm：不能定制，安装方便
- yum自动解决rpm依赖包的问题

### yum install是如何安装的

![[Pasted image 20231216185928.png]]
我们可以看到这里使用的三个yum的下载网站
![[Pasted image 20231216190110.png]]
这里是在日本找到的网站
所以每个区域对应的源是不一样的

是自动选择一个仓库下载网址
centos官方的仓库是centos.org的镜像源仓库
![[Pasted image 20231216190406.png]]
![[Pasted image 20231216190356.png]]
这是我们查看centos使用仓库的命令
使用vim进去查看，如果enabled=0代表这个仓库被禁用了
启用的是没有enabled
![[Pasted image 20231216190503.png]]

为了加快下载速度，所以centos官方允许别的各个地区的镜像
yum里面有一个list名单
![[Pasted image 20231216190805.png]]
首先会把这里的releasever替换成centos6还是7
然后
![[Pasted image 20231216190838.png]]
这里就会替换成x86-64或者是32位
然后就根据你的ip地址推荐很多的镜像地址

