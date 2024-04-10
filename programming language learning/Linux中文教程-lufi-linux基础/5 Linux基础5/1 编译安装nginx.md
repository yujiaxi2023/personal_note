
## 软件的安装

无论是linux还是win，安装软件都只有几种方式

win:
- 单个exe文件，双击就可以运行
- 绿化软件，idm：这时候下载的是一堆文件，需要先用绿化按钮，win一般安装都是在注册表中添加东西，这就是绿化按钮功能
- 安装包----安装-----启动
- 源代码，C++开发的源代码，源代码不能运行，需要使用编译器编译生成exe或者dll等相关文件，有了相关文件之后就会进行运行

win中的c++编译时非常复杂

linux：
- 自己编译
- 使用别人编译好的
- 形成二进制可执行文件

linux中文件没有后缀的，我们就不知道这是什么文件了，加后缀是防止自己忘记

win是微软一家公司推动主导，所以会对开发者有各种限制，才能在win上边运行，所以会非常规范，win软件，并不会出现太多的问题

linux只贡献了一个内核，软件是各种开发者开发的，所以每个软件的命令参数都是不一样的，非常混乱

可以看图说明，linux的特点就是会一层套一层的继承软件，有集成继承的各种关系，你会看到各种参数并没有采用相同的参数，这就是因为编译者使用的不同习惯造成的
![[Pasted image 20231216170824.png]]


### linux软件安装

**最困难的就是依赖问题**
win中只要安装了微软的运行库就可以兼容绝大部分的软件了

编译安装

编译我们需要下载源码包
最大的源码网站就是github

国内的开源网站有gitee

```
1. 下载源码包
cd /opt/
rm -fr *
curl -o nginx.tar.gz http://nginx.org/download/nginx-1.24.0.tar.gz
```

```
2. 编译
tar -xf nginx.tar.gz
cd nginx-1.24.0/
```
![[Pasted image 20231216172257.png]]
会发现这里的用户和用户组是test1和test，这是因为源码文件写的时候储存的用户和用户组的uid和gid是1001和1001，在本机上这两个id代表的是这两个用户和用户组

```
# 编译参数
# 有源代码的时候我们可以配置什么东西要什么东西不要
# 如果全部功能启用了就是完整版，如果有些功能不要就可以叫做精简版
./configure --prefix=/usr/local/nginx --without-pcre --without-http_rewrite_module --without-http_gzip_module
# 编译
make
# 安装
make install
```
我们为什么不启用这三个功能是因为我们需要安装依赖包
现在还没学到如何安装依赖包，所以暂时不要这几个功能
![[Pasted image 20231216172911.png]]
注意需要有这个绿色的configure文件执行编译
![[Pasted image 20231216173006.png]]
检查成功之后就会自动生成一些文件，比如说关键的makefile
![[Pasted image 20231216173134.png]]
这里会出来一个新的文件还有objs

```
# 必须有Makefile文件才可以执行编译
make
```
这个需要多少时间，决定于两个方面：
- CPU的性能
- 软件的复杂程度

这里的nginx绿色的就是二进制命令
![[Pasted image 20231216174909.png]]
```
[root@localhost objs]# ./nginx -v
nginx version: nginx/1.24.0
```
这里就可以执行这个二进制命令了
但是就是要带上完整路径，只有一个名字是不可以执行的
![[Pasted image 20231216175226.png]]

但是软件只是编译完成，虽然可以执行，但是没有进行安装
所以我们需要安装
```
make install
```
软件安装的目录是之前配置的
```
./configure --prefix=/usr/local/nginx --without-pcre --without-http_rewrite_module --without-http_gzip_module

里面prefix参数指令的目录路径
```
![[Pasted image 20231216175504.png]]

我们还可以打开软件下面的所有文件
![[Pasted image 20231216175545.png]]
我们可以使用tree软件查看有多少文件
### tree以树状结构查看目录
![[Pasted image 20231216175642.png]]
4个目录18个文件
```
tree 目录路径
```
目录下的文件代表什么：
- sbin代表关键启动命令
- html代表网站源代码目录
- conf代表配置文件路径

安装就是把这一堆文件分类放置在对应的目录下面能跑起来就行

### nginx执行

没有配置环境变量的情况下需要使用完整路径
```
3. 运行
/usr/local/nginx/sbin/nginx
# 使用浏览器访问http://<虚拟机的ip地址>
# 关闭防火墙
systemctl stop firewalld
# 取消防火墙的开机自启动
systemctl disable firewalld
```
通过浏览器访问的时候因为有防火墙，所以无法访问
这时候需要关掉防火墙
![[Pasted image 20231216180310.png]]
就会出来这个界面了

