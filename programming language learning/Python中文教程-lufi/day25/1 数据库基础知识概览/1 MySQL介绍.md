## 数据库相关概念

1. 数据库服务器
2. 数据库管理软件
3. 库
4. 表
5. 记录
6. 数据

### 数据

数据是描述事物特征的符号

#### 记录

事物一系列的典型的特征

#### 表

```
#name,sex,age,school
yu,mail,25,osaka
```

#### 库

创建库就是创建一个文件夹
为的是让表分类

#### 数据库管理软件

mysql oracle db2 slqserver

数据库其实就是一个套接字服务端

#### 数据库服务器

实际上是一台计算机，是专门用来运行数据库管理软件的

# MySQL介绍

MySQL是一个关系型数据库管理系统，由瑞典公司MySQL AB公司开发，目前属于Oracle
MySQL是最流行的关系型数据库管理系统，在WEB应用方面MySQL是最好的RDBMS（Relational Database Management System）之一

**mysql是什么**
mysql就是一个基于socket编写的C/S架构的软件

客户端软件
MySQL自带：例如mysql命令，mysqldump命令等
python模块：例如pymysql

**数据库管理软件分类**
分为两类：
关系型：例如sqlliter，db2， oracl，access，sql server，mysql，注意sql语句是通用的
非关系型：例如monogodb redis memcache

可以简单理解为：
关系型数据库需要有表结构（字段，数据类型）
非关系型数据库是key-value存储的，没有表结构


