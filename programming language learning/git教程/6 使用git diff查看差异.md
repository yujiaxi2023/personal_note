可以用于查看工作区，暂存区，本地仓库之间的差异
查看不同版本的差异
查看不同分支的差异

```bash
git diff # 默认查看工作区和暂存区的内容
```
显示发生更改的文件和更改的详细信息
![[Pasted image 20240719173858.png]]
第一行是发生变更的文件
第二行是将文件变成一个40位的哈希值 100644是文件的权限
+后边是添加的内容

![[Pasted image 20240719174057.png]]
只要add之后就不会出现差异

但是add并没有commit到仓库中
所以此时
```bash
git diff HEAD
```
还是会显示出差异

比较暂存区和版本库的差异
```bash
git diff --cached
```

也可以比较两个版本之间的差异
```
git log --oneline
git diff #版本1 #版本2
```

HEAD是最新提交的分支节点
```
HEAD
```

比较当前版本和上一个版本的差异
```bash
git diff HEAD~ HEAD
git diff HEAD^ HEAD
git diff HEAD~2 HEAD # 提交之前的两个版本
```

只查看一个文件的差异内容
```bash
git diff HEAD~3 HEAD file3.txt
```

