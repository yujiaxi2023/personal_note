windows下面的搜索非常垃圾，有的时候就非常难搜索到

linux上面进行搜索

### find 普通查找
```
# 文件查找
例子1 普通查询
find    /etc    -maxdepth 1 -type f -name "*pa*"
命令     目录     查找深度     类型     文件名称
```

```
[root@localhost nginx-1.24.0]# find /etc -maxdepth 1 -name "pa*"
/etc/passwd
/etc/passwd-
/etc/pam.d
[root@localhost nginx-1.24.0]# find /etc -maxdepth 2 -name "pa*" -type f
/etc/passwd
/etc/passwd-
/etc/security/pam_env.conf
/etc/pam.d/passwd
/etc/pam.d/password-auth-ac
```


### find按照文件大小查找
```
例子2：按照文件大小查找
查找大于100M的文件
find / -type f -size +100M

# 按照kb查找
find / -type f -size +100k
# 注意是小写k

# 按照字节查找
find / -type f -size -100 # 100字节之内

# 按照GB查找
find / -type f -size -1G # 小于1G

# 查找大于50M小于100M
find / -type f -size +50M -and -size -100M

# 查找小于20M和大于200M的
find / -type f -size -20M -or -size +200M
```
遇到proc的报错可以忽略掉，因为proc是进程，进程打开消失的都非常快

#### -iname 忽略大小写
```
例子3：忽略大小写
find /etc -type d目录 f是文件 l是软连接 -iname "pa*"
```
这样就可以搜索出大写的PA出现的文件

访问时间：每查看一次文件内容，时间就会更新
修改时间：文件的内容变化了，时间就会更新
改变事件：文件的属性变化了，时间就会更新
文件属性：文件权限，文件的用户和用户组，文件大小

#### 按照时间查找atime mtime ctime amin mmin cmin
应用场景：
如果我们电脑收到了木马袭击，我们这时候如何查找到这个木马文件呢
最简单的就是找它的时间

```
例子4
根据修改时间查找文件
时间参数：atime mtime ctime amin mmin cmin
# 时间单位是天
find /opt -type f -mtime -1 # -1代表1天以内 +1是1天之前
# 时间单位是分钟
find /root -type f -mmin -20 # 代表20min以内

stat 文件路径
# 就可以显示3种时间
```


#### 取反
```
例子5
取反
touch {1..5}.txt
ll
find /root -type -name "3.txt"
find /root -type ! -name "3.txt"
# 这就是取反，其他所有的文件就会显示出来
```

#### 根据用户查找
```
find / -user dms
# 就可以查找所有是dms用户的文件
find / -group dms
# 查找所有属于dms用户组的文件
```

#### 根据权限来查privilege permission deny
```
find --help
find / -type f -perm 644
# 可以查找所有的644权限的文件
```

#### 对找出的文件进行处理-exec
```
find /root -type f -mmin -3 -size +10k -user dms -perm 644 -exec rm {} \;
```

比如我要找到一个文件，然后删除掉
删除目录好像需要把-rf去掉
```
find /root -type d -name "dms*"
find /root -type d -name "dms*" -exec rm {} \;
```

```
find /root -type f -name "*.txt"
find /root -type f -name "*.txt" -exec rm -rf {} \;
```

除了删除，可以对它进行任何有对象的操作
```
find /root -type f -name "*.cfg" -exec cp {} /tmp \;
```
还要注意的是，一定要把占位符写入{}，占位符代表着需要执行文件应该在的位置，是被动的还是主动的都应该纳入考虑

## linux的;
在linux中如果  ;  不进行转义的话，就是代表前后两条命令一起执行
```
ls -l;id
```
linux 空格一下就是命令参数之间的

比如我在linux需要对某个有空格的文件进行操作
```
rm -fr winhex\ \ 20.5.zip
```
这里需要转义符对空格进行转义
