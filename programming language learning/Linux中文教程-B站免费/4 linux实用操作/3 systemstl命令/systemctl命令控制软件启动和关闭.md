**systemctl命令**
Linux系统中很多软件（内置或者第三方）均支持使用systemctl命令控制：启动，停止，开机自启动

能够被ststemctl管理的软件，一般称为：服务
语法：systemctl start | stop | status | enable | disable 服务名
![[Pasted image 20230707202200.png]]

系统内置的服务比较多，比如：
- NetworkManager，主网络服务
- network 副网络服务
- firewalld 防火墙服务
- sshd，ssh服务（FinalShell远程登陆Linux使用的就是这个服务

[如果您使用的是WSL（Windows Subsystem for Linux），那么您的Linux系统将使用System V init系统，而不是systemd。在这种情况下，您无法运行systemd命令，但可以运行等效的Sysvinit命令。您可以使用命令`ps -p 1 -o comm=`来查看您正在使用的init系统](https://www.partitionwizard.com/partitionmanager/system-not-booted-with-systemd-as-init.html)[1](https://www.partitionwizard.com/partitionmanager/system-not-booted-with-systemd-as-init.html)。

[如果您想要使用systemd作为init系统启动，目前没有办法在WSL上使用systemd作为PID 1运行。WSL使用它自己的专有、闭源init（位于每个WSL发行版的根目录（即/init）中）作为PID 1。这对于WSL的运行至关重要。它执行许多关键功能，如启动虚拟网络堆栈和许多其他功能](https://askubuntu.com/questions/1279047/how-to-boot-system-with-systemd-as-init-system-pid-1)[2](https://askubuntu.com/questions/1279047/how-to-boot-system-with-systemd-as-init-system-pid-1)。
进行 查看操作的时候报错的原因如上
![[Pasted image 20230707202735.png]]

![[Pasted image 20230707202934.png]]
使用 替代的命令并不能查找到这些东西

您可以使用sysvinit命令来代替systemd命令。它们的语法相似，不太复杂。下面是一些常用的systemd命令及其对应的sysvinit命令：

|Systemd命令|Sysvinit命令|
|---|---|
|`systemctl start service_name`|`service service_name start`|
|`systemctl stop service_name`|`service service_name stop`|
|`systemctl restart service_name`|`service service_name restart`|
|`systemctl status service_name`|`service service_name status`|
|`systemctl enable service_name`|`chkconfig service_name on`|
|`systemctl disable service_name`|`chkconfig service_name off`|

您可以根据您正在使用的教程，尝试使用等效的命令，这样您就不会再看到“System has not been booted with systemd as init system (PID 1). Can’t operate.”这个错误了。

[在WSL上，您可能无法使用NetworkManager或firewalld服务。这是因为WSL不支持systemd，而这些服务依赖于systemd。此外，WSL2实际上是一个“受管理的”虚拟机，我们作为用户无法访问。控制网络的是这个虚拟机。您的WSL2发行版作为一个容器运行在该虚拟机内。在WSL中尝试使用Network Manager就像在Docker容器中尝试使用它一样——这可能没有多大意义](https://superuser.com/questions/1731930/cant-open-network-manager-gui-on-wsl2-ubuntu)[1](https://superuser.com/questions/1731930/cant-open-network-manager-gui-on-wsl2-ubuntu)。

![[Pasted image 20230707203139.png]]
![[Pasted image 20230707203147.png]]
这是在CentOS虚拟环境上面进行操作的结果

![[Pasted image 20230707203216.png]]这是停止开机自启动的命令

![[Pasted image 20230707203232.png]]
这是开机自启动的命令

**除了内置服务，还可以控制部分第三方软件**
![[Pasted image 20230707203314.png]]

**对于ntp**
![[Pasted image 20230707203735.png]]
注意在Ubuntu系统中service 需要搜索ntp而不是centOS中的ntpd
![[Pasted image 20230707203837.png]]
注意需要管理员权限才能run这个程序
![[Pasted image 20230707203938.png]]
这样程序就run了
![[Pasted image 20230707204029.png]]
这样就停止了

![[Pasted image 20230707204119.png]]
这样就是wsl下的开关开机启动

**对于httpd**
Ubuntu下载过程中无法找到这个包，操作有点复杂现在不太好进行
当你看到 `Package 'httpd' has no installation candidate` 这个错误信息时，意味着包管理器无法在它的仓库中找到这个包 。这可能是因为这个包不在默认仓库中，或者它已经被重命名了 。

你可以尝试更新你的系统，看看是否能解决这个问题，运行 `sudo apt update && sudo apt upgrade` 。如果还是不行，你可能需要添加一个包含这个包的第三方仓库 。你也可以使用命令 `apt-cache search PACKAGE_NAME` 来搜索具有类似名称的可用包 。

要添加一个包含这个包的第三方仓库，你需要找到这个仓库的地址。你可以在网上搜索这个包的名称，看看是否有第三方仓库提供它。

找到仓库地址后，你可以使用以下命令将其添加到 Ubuntu 的软件源中：

```
sudo add-apt-repository REPOSITORY_PPA
```

其中 `REPOSITORY_PPA` 是你找到的仓库地址。

添加完仓库后，你需要刷新本地的 Apt 实例，以便包含新仓库中的所有包。要做到这一点，运行以下命令：

```
sudo apt update && sudo apt upgrade
```

然后你就可以安装新仓库中提供的包了。

**如何手动添加后续章节讲解**

![[Pasted image 20230707204648.png]]
