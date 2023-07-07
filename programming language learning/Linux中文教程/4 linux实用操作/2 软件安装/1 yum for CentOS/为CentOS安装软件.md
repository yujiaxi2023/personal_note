操作系统安装软件有多种方式，一般分为：
- 下载安装包自行安装
	- win系统exe文件 msi文件
	- max系统dmg文件 pkg文件
- 系统的应用商店内安装
	- win系统的microsoft 商店
	- mac的AppStore

Linux系统同样支持这两种安装方法
在Linux命令行内的应用商店，yum命令安装软件

yum命令
yum：RPM包软件管理器，用于自动化安装配置Linux软件，并可以自动解决以来问题
语法：yum -y install | remove | search 软件名
- 选项：-y，自动确认，无序手动确认安装或卸载过程
- install 安装
- remove 卸载
- search 搜索

yum命令需要root权限，可以su切换，或者sudo
yum需要联网
RPM是Linux系统的安装包名称
![[Pasted image 20230707200808.png]]

yum 命令
- yum -y install wget
- yum -y remove wget
- yum search wget
![[Pasted image 20230707200911.png]]

下载界面如图
![[Pasted image 20230707201036.png]]
这里就是有询问，如果不询问就在初始命令中加-y
![[Pasted image 20230707201118.png]]
卸载界面如图
![[Pasted image 20230707201139.png]]
这里同样可以在开始输入-y自动确认

