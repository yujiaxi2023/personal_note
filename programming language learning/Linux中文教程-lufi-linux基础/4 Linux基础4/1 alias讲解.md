## 命令别名

```
# 别名
alias
例子1：

```
```
[root@localhost ~]# alias
alias cp='cp -i'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l.='ls -d .* --color=auto'
alias ll='ls -l --color=auto'
alias ls='ls --color=auto'
alias mv='mv -i'
alias rm='rm -i'
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
```
使用别名跟使用正常命令是一样的
注意这里
```
alias ls='ls --color=auto'
```
ls本来是没有颜色的，但是我们这里设定了一个别名，把ls变为了自动显示颜色

还有就是cp
```
alias cp='cp -i'
```
这个就是在cp的时候遇到同名文件显示是否需要覆盖文件

#### 删除别名
```
unalias ls
alias
ls /
ls --color=auto /
```
最原始的ls就是黑白的

```
unalias cp
cp /etc/passwd .
```
这个样子就会直接覆盖掉

#### 定义别名
```
alias rm='echo 禁止删除文件'
# 这个时候删除文件
rm passwd
# 就会显示
禁止删除文件 passwd
```

**alias的优先级要高**
会优先查看别名中是否有命令
然后执行别的指令

如果alias了一个不存在的指令
就会报错bash找不到这个未知指令

注意这个修改别名不是永久的，重启就失效了
如果希望永久生效
```
vi .bashrc
# 在这个文件中更改
```