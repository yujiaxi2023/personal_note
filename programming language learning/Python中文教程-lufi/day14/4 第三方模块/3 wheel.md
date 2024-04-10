wheel是python第三方模块包的文件格式的一种,我们也可以基于wheel安装一些第三方模块

- 安装wheel格式支持,这样pip再安装第三方模块的时候,就可以处理wheel格式的文件了
`pip3 install wheel`
- 下载第三方的包(wheel格式), 例如: https://pypi.org/project/requests/#files
![[Pasted image 20231026162512.png]]
- 进入下载目录,终端基于pip直接安装
![[Pasted image 20231026162543.png]]

wheel是python后来支持的文件格式,可以理解成一个压缩包,开发者通过特殊方式压缩成whl格式的文件,上传到某个位置

默认的安装路径在:
```
Mac系统: lib/python3.9/site-package
win系统: python39/Lib/site-packages/
```
这个目录在sys.path种,所以直接在代码中直接导入下载的第三方包是没问题的

在使用wheel安装的时候需要注意操作系统的版本兼容的wheel包,一般来说升级wheel可以解决大部分的wheel问题
