ini文件时initialization file的缩写，平时用于储存软件的配置文件，例如MySQL数据库的配置文件
```ini
[mysqld]
datadir = /var/lib/mysql
socket = /var/lib/mysql/mysql.sock
log-bin = py-mysql-bin
character-set-server = utf8
collation-server = utf8_general_ci
log-error = /var/log/mysqld.log
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links = 0

[mysqld_safe]
log-error = /var/log/mariadb/mariadb.log
pid-file = /var/run/mariadb/mariadb.pid

[client]
default-character-set = utf8
```
使用键值对的方式储存的数据
中括号是一个节点的意思
这种格式是可以直接用open出来，自己处理比较麻烦。使用python的lib比较容易

- 读取 所有节点
```python
import configparser  
  
config = configparser.ConfigParser()  
config.read('file/my.ini', encoding='utf-8')  
# config.read('C:\Users\student\PycharmProjects\day09\file\my.ini', encoding='utf-8')
```

- 获得节点下的 键值
```python
result = config.sections()  
print(result) # ['mysqld', 'mysqld_safe', 'client']
```

- 获得某个节点下的键对应的值
```python
result = config.items('mysqld_safe')  
print(result) # [('log-error', '/var/log/mariadb/mariadb.log'), ('pid-file', '/var/run/mariadb/mariadb.pid')]  
# 将获得的元组提取出来  
for key,value in config.items('mysqld_safe'):  
    print(key,value)    # log - error / var / log / mariadb / mariadb.log    # pid - file / var / run / mariadb / mariadb.pid
```

- 其他功能
```python
# 获取某个节点下键对应的值  
result = config.get('mysqld', 'collation-server')  
print(result)  # utf8_general_ci  
  
# 其他功能  
# 是否存在某个节点  
v1 = config.has_section('client')  
print(v1)  
  
# 添加一个节点  
config.add_section("group")  
# 只添加到内存里面，没有到文件中写  
config.write(open('file/my.ini', mode='w', encoding='utf-8'))  
# 将内容写到指定的文件，文件必须是一个文件对象  
  
# 添加键值  
config.set('group','name','wupeiqi')  
config.write(open('file/my.ini', mode='w', encoding='utf-8'))  
# 同样需要写道文件中去  
config.set('client','name','wupeiqi')  
  
# 删除节点或者键值  
config.remove_section('client')  
config.remove_option('mysqld','datadir')  
config.write(open('file/new.ini', mode='w', encoding='utf-8'))
```