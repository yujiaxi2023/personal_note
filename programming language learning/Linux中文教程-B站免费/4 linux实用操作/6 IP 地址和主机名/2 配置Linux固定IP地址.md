虚拟机配置固定IP,用于windows系统和mac os系统

**为什么需要固定IP**
现在虚拟机Linux操作系统, 其IP是通过DHCP服务获取的
DHCP: 动态获取IP地址,即每次重启设备会获取一次,导致IP地址频繁变更

原因1: 家用电脑IP变化无所谓,但是远程连接到Linux系统,如果IP 经常变化,需要频繁的修改适配很麻烦

原因2: 配置了虚拟机IP地址和主机名映射,如果IP 频繁更改,会更改映射关系的有效性


![[Pasted image 20230712160915.png]]

**如何在windows中固定IP**
两个步骤:
1. VMware Workstation 或 Fusion 中配置IP地址网关和网段(IP地址的范围)
2. 在linux系统中手动修改配置文件,固定IP
设置子网iP的网关网段,按照之前说的a.b.c.d的格式设置
![[Pasted image 20230712161115.png]]
设置子网掩码
![[Pasted image 20230712161139.png]]
随后进行NAT设置
![[Pasted image 20230712161200.png]]
设置网关
![[Pasted image 20230712161229.png]]

进入linux操作系统中配置
使用vim编辑配置文件
关键绩点更改
BOOTPROTO = "static" # 由 dhcp更改
IPADDR = "ip地址"
NETMASK = "IP掩码固定"
GATEWAY = "VMware中设置的网关一样"
DNS1 = "设置为网关一致" # 域名解析服务器

使用`systemctl restart network`重启网关之后就可以固定住网关
![[Pasted image 20230712161911.png]]
![[Pasted image 20230712161925.png]]
![[Pasted image 20230712161936.png]]
需要注意修改的是NAT模式

mac中使用的fusion修改
![[Pasted image 20230712162323.png]]
![[Pasted image 20230712162350.png]]


总结
![[Pasted image 20230712162420.png]]
![[Pasted image 20230712162431.png]]
![[Pasted image 20230712162437.png]]
mac中是终端修改第一步
