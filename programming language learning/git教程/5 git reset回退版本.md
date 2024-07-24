#### git reset 三种模式

```bash
git reset --soft
git reset --hard
git reset --mixed
```
soft 是回退到某个版本并保留工作区和暂存区的内容
hard 是回退到某个版本，并且丢弃工作区和暂存区的所有修改内容
mixed 是介于soft和hard之间，是保留工作区的内容，丢弃暂存区的内容

```bash
echo 111>file1.txt
echo 111>file2.txt
echo 111>file3.txt

git add file1.txt
git commit -m "commit1"
git add file2.txt
git commit -m "commit2"
git add file3.txt
git commit -m "commit3"

git log --oneline

# 这里会显示三次提交的一个编号

# 这三个文件都在repo文件夹下面

cp —rf repo repo-soft
cp —rf repo repo-hard
cp —rf repo repo-mixed

cd repo-soft
git log --oneline
git reset --soft #版本号码
# 接下来检查file3还在不在
ls
cat file3.txt
git ls-files # 检查暂存区的文件
git status # 现在会提示file3.txt是新文件
# file3 并没有添加进来，但是soft让其在工作缓存区域还是存在

cd repo-hard
git log --oneline
git reset --hard HEAD^ # HEAD^同样也是上一个版本的意思
git log --oneline # 现在提交历史只有两次
ls # file3不存在
git ls-files # file3也不再缓存区中

cd repo-mixed
git log --oneline
git reset HEAD^ # 这个也就是mixed命令
ls
cat file3.txt # 工作区还有这个文件
git ls-files # 此时并没有在暂存区中有file3
```

### 回溯操作

不需要担心误操作的问题，因为git所有操作都可以回溯
```bash
git reflog
git reset --hard #版本号
```
