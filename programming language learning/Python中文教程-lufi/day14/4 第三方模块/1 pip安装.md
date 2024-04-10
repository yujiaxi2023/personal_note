python内部提供的模块有限，所以在平时开发的过程中，经常会使用第三方模块
而第三方模块必须要先安装才能使用，下面介绍常见啊3种安装第三方模块的方式

使用第三方模块就是用别的写好开源代码，自己用


## pip最常用

这是python种最常用的第三方模块安装方法
pip其实是一个第三方模块包管理工具，默认安装python解释器的时候会自动安装，默认目录：
Mac：是python安装目录的bin目录下面，在环境变量中看
Windows：是python安装路径下的scripts目录，也是环境变量中看
为了方便在终端运行pip管理工具，会把所在的路径添加到系统环境变量中
```shell
pip install 模块名
```


如果电脑种某些情况没有找到pip，可以手动安装：
- 下载`get-pip.py`文件到任意目录
```
地址：https://bootstrap.pypa.io/get-pip.py
```
- 打开终端进入目录，用python解释器运行已经下载的`get-pip.py`文件就可以安装成功
![[Pasted image 20231026160239.png]]
可以执行下载的py文件，就会自动装上
当电脑中有多个python版本，所以需要指定版本号，就会在当前python下下载pip

使用pip安装第三方模块非常简单，只需要自己终端执行`pip install 模块名`即可
![[Pasted image 20231026160436.png]]
![[Pasted image 20231026160446.png]]
pip install就是去pypi网站找到版本并下载
默认安装的是最新的版本，如果想要指定版本：
```python
pip install 模块名称==版本

例如
pip3 install django==2.2
```
这里的warning就是代表着pip的版本落后了，可以更新你的pip工具

## pip更新
上图的黄色字体显示：目前在电脑上的版本如果是20.2.3，最新的是20.3.3版本，如果想要升级为最新的版本，可以终端执行他提示的命令：
![[Pasted image 20231026160735.png]]
注意，每个电脑的这个命令不一样

## 豆瓣源

pip默认是通过https://pypi.org上下载第三方模块（也就是别人的py代码），中国下载国外的网站速度很慢，加速可以使用国内的源下载
- 一次性使用
`pip3.9 install 模块名称 -i https://pypi.douban.com/simple/`
- 多次使用
- 配置
```
# 终端执行命令
pip3.9 config set global.index-url https://pypi.douban.com/simple

# 执行完成后，提示在我都本地文件中写入了豆瓣源，以后通过pip安装第三方模块的时候，就会默认使用豆瓣源
# 自己以后可以打开文件直接修改源地址
Writing to /Users/wupeiqi/.config/pip/pip.conf
```
- 使用
```
pip3.9 install 模块名称
```


写在最后，有其他的源可供选择（豆瓣应用广泛）
```
阿里云：http://mirrors.a;iyun.com/pypi/simple/
中科院：https://pypi.mirrors.ustc.edu.cn/simple/
清华：http://pypi.tuna.tsinghua.edu.cn/simple/
中科大：http://pypi.mirrors.ustc.edu.cn/simple/
```

