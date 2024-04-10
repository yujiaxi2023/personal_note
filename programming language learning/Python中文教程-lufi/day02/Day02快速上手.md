课程目标：学习python最基础的语法知识，可以用代码快速实现简单的功能
课程概要：
初识编码（密码本）
编程
输出
初识数据类型
变量
注释
输入
条件语句


**1.编码（密码本）**
计算机所有数据都是用01来储存的

计算机中有很多种编码
```text
	每种编码有自己的一套密码本，都维护自己的一套规则
	utf-8编码
	gbk编码等
```

注意事项：
以某个编码形式保存的文件，以后就用该种形式打开，不然可能出现乱码

**2.编程**
编码必须保持：保存和打开是一样的
默认python解释器以utf-8的编码形式打开文件，如果想要修改Python的默认解释器编码，可以
```python
# -*- coding:utf-8 -*-  
  
print("I am your grandfather")
```

**3.输出**
将结果或者内容想要呈现给用户
```python
print("                               **")
print("                             _ooOoo_")  
print("                            o8888888o")  
print("                            88  .  88 ")  
print("                            (| -_- |)")  
print("                             O\ = /O")  
print("                         ____/`---'\____")  
print("                       .   ' \\| |// `.")  
print("                        / \\||| : |||// \ ")  
print("                      / _||||| -:- |||||- \ ")  
print("                        | | \\\ - /// | |")  
print("                      | \_| ''\---/'' | |")  
print("                       \ .-\__ `-` ___/-. /")  
print("                 ."" '< `.___\_<|>_/___.' >'"".")  
print("                | | : `- \`.;`\ _ /`;.`/ - ` : | |")  
print("                  \ \ `-. \_ __\ /__ _/ .-` / /")  
print("          ======`-.____`-.___\_____/___.-`____.-'======")  
print("                             `=---='")  
print("                                                        ")  
print("          .............................................")  
print("                   佛祖保佑             永无BUG")  
print("           佛曰:")  
print("                   写字楼里写字间，写字间里程序员；")  
print("                   程序人员写程序，又拿程序换酒钱。")  
print("                   酒醒只在网上坐，酒醉还来网下眠；")  
print("                   酒醉酒醒日复日，网上网下年复年。")  
print("                   但愿老死电脑间，不愿鞠躬老板前；")  
print("                   奔驰宝马贵者趣，公交自行程序员。")  
print("                   别人笑我忒疯癫，我笑自己命太贱；")  
print("                   不见满街漂亮妹，哪个归得程序员？")

%%输出后面会自动加换行%%
```

想要不换行
```python
print("五花马", end=",")
print("千金裘", end=",")
print("呼儿将出换美酒", end="。")
```

**4.初识数据类型**

**4.1 整形（int）**
整形 整数 integer
```python
print(666)  
print(2 + 10)  
print(10 / 2)  
print(2 ** 4)  
print(10 % 3)
#%是计算余数
#**代表乘方
```

**4.2 字符串（Str）**
```python
print("I am human")  
  
print('China HuBei Province')
%%文本中想表达双引号，两边应该用单引号%%

print("""China  
hubei province  
wuhan city  
dong xihu district  
""")
%%文本可以表示多行字符串，此处的双引号也可以换成三个单引号%%
```
对于字符串：
加，两个字符串可以用加号拼接
```python
print("I"+"am"+"your"+"grand"+"father")
```
乘，让整形和字符串进行相乘，以实现让字符串重复出现N次拼接起来
```python
print(3*"I want eat breakfast")
```

**4.3 布尔类型（bool）**
布尔类型中共有两个值：ture or false
```python
1>2
1==1
print(1 > 2)
print(False)

print(1 == 1)
print(True)
```
```python
name = input("请输入账户")  
  
if name == "yuyumeng":  
    print("用户登录成功")  
else:  
    print("用户登陆失败")
```

补充：
```python
1 > 2
1 == 3
"A" == "B"
1 == "A"

# 1 > "A"是无法进行比较的
```

**4.4 类型转化**
int，整型定义，必须是数字且无引号
str，字符串定义，必须是用双引号括起来，例如“A”
bool，布尔值定义时，只能写True False
不同的数据类型有不同的功能，例如：整型可以加减乘除 而 字符串只能加（拼接）和乘法
如果想转换可以遵循一个基本的原则，想转换什么就让他包裹一些
例如：ste(666) = "666"是将整形转换为字符串， int("888")是将字符串转换为888

转换为整形：
```python
#字符串转换为整形
int("666")
int("999")

"8" + "9"的结果应该是"89"
int("8") + int("9")的结果应该是"17"

"I am fish"是无法转换为整形
int("I am fish")会报错

#布尔类型转换为整形
int(True)转换为1
int(False)转换为0
```

转换为字符串：
```python
#整形转字符串
str(345)
str(999) + str(388) 结果为999388

#布尔类型转换为字符串
str(True) "True"
str(False) "False"
```

转换为布尔类型
```python
#整形转布尔类型
bool(1)True
bool(2)True
bool(0)False
bool(-19239)True

#字符串转布尔类型
bool("ABYH")True
bool("oiayhdsiuh")True
bool("")False
```


总结：
其他所有类型转换为布尔类型，除了空字符串，0以外，其他都是True
字符串转整形时候，只有数字才可以转换成整形
想要转换成什么类型，就用这种类型的英文包裹一下
```python
str(...)
int(...)
bool(...)
```

**5. 变量**
变量，其实就是我们生活中起别名和外号，让变量名指向某一个值，格式为：【变量名=值】，以后可以通过变量名来操作其对应的值

```python
name = "tony"
print (name) # tony

age = 18
name = "A"
flag = 1 > 19
adress = "beijing" + "shahe"
addr = "beijing" + "shahe" + name #beijingshaheA
print(addr)
print(flag)


```

注意：
给变量赋值 age = 18
	让age代指值 age = 18

**5.1 变量名的规范**
```text
age = 18
name = "alex"
flag = 1 > 18
address = "beijing" + "changping"
```

三个规范：
变量名只能由字母，数字，下划线
不能以数字开头
```text
na9me9 = "alex"
```
不能用python内置的关键字
```text
def = "alex"
break = 123
```
{"and","as","assert","break","class","continue","def","del","elif","else","except","exec"."finally","far",
”from","global","if","import","in","is","lambda","not","or","pass","print","raise","return","try","while",
"with","yield"}

练习题
```text
name = "tony"
name0 = "tony"
name_1 = "duncan"
_coach = "popovic"
_ = "kawayi"
1_year = "1900" # 错误 不能以数字开头
year_1_ = "1900"
_1_year = "1900"
nba-team = "spurs" # 错误 不能以字母数字下划线之外的符号
new*name  = "leonard" # 错误 不能以字母数字下划线之外的符号
```

两个建议：
下划线连接命名(小写)
```text
father_name = "yu"
brother_age = 19
```
名字意思对应可以理解
```text
age = 18
color = "red"
current_user_name = "xxx"
n1 = 123
n2 = 456
```

**5.2 变量内存指向关系**
内存指向(在电脑的内存中是怎样储存的)

情景1
```python
name = "some"
```
在计算机的内存中创建一块区域保存字符串"some", name变量名指向这块区域
![[Pasted image 20230207132449.png]]

情景2
```python
name = "some"
name = "some1"
```
在计算机的内存中创建一块区域保存字符串“some”， name变量名指向这块区域，然后又在内存中创建了一块区域保存字符串“some1”，name变量名则指向“some1“所在的区域，不再指向”some“所在的区域（无人指向的数据会标记为垃圾，由解释器自动化回收）
![[Pasted image 20230207132858.png]]

情景3
```python
name = "some"
new_name = name
```
在计算机的内存中创建一块区域保存字符串”some“，name变量名则指向这块区域。new_name指向name变量保存的内存区域
![[Pasted image 20230207133142.png]]

情景4
```python
name = "some"
new_name = "some"
name = "some1"
```
在计算机的内存中创建一块区域保存字符串“some”，name变量名则指向这块区域（灰色线），然后new_name指向name所指向的内存区域，然后创建一块区域存放“some1”，让name变量指向“some1”所在的区域。
![[Pasted image 20230207133459.png]]

情景5
```python
num = 18
age = str(num)
```
在计算机的内存中创建一块区域保存整型18，name变量名指向这块区域，通过类型转换依据整型18在内存中创建一个字符串“18”，age指向保存这个字符串的内存区域
![[Pasted image 20230207133809.png]]

更多还有内存管理，垃圾回收，驻留机制等问题

**练习题**
1. 看代码知结果
```python
alex_length = 3
wupeiqi_length = 18
total = alex_length + wupeiqi_length
print(total)
```

```answer
21
```
2. 按要求写代码
```python
# 假设age是小明的年龄
age = 18
# 问：已知小李比小明大三岁，计算小李年龄赋值给ming_age变量并输出
# 问：已知大刘比小明和小李年龄的和还要大五岁，计算大刘的年龄赋值并给liu_age变量并输入
```

```python
ming_age = 18
li_age = ming_age + 3
liu_age = li_age + ming_age + 5

print(ming_age)
print(liu_age)
```

3. 看代码写结果
```python
nickname = "18cm"
username = nickname

username = "little brother"
print(nickname)
print(username)
```

```answer
18cm
little brother
```

4. 看代码写结果
```python
nickname = "18cm"
username = nickname
nickname = "little brother"

print(nickname)
print(username)
```

```answer
little brother
18cm
```

5. 看代码写结果
```python
nickname = "18cm"
username = "little brother"
text = username + nickname
print(text)
```

```answer
little brother18cm
```

6. 看代码写结果
```python
nickname = "18cm"
username = nickname
nickname = "little brother"
text = username + nickname
print(text)
```

```answer
18cmlittle brother
```

7. 看代码写结果
```python
string_number = "20"
num = int(string_number)

data = string_number * 3
print(data)

value = num * 3
print(value)
```

```answer
202020
60
```

**6. 注释**
写代码的时候，如果想要对某些内容进行注释处理，即：解释器忽略不会按照代码去运行
单行注释
```text
#声明一个name变量
name = "alex"

age = 19 #这表示当前用户的年龄

注意：快捷键control+？
```

多行注释
```text
#声明一个name变量
#声明一个name变量
#声明一个name变量
name = "alex"

"""
多行注释
多行注释 
多行注释
"""

name = """
多行注释内容
多行注释内容
多行注释内容
"""

```


**7. 输入**
输入，可以实现程序和用户之间的交互
```python
#1.右边input("请输入用户名")是让用户输入内容，
#2.将用户输入的内容赋值给name变量
name = input{"请输入用户名:"}

if name == "alex":
	print("登录成功")
else:
	print("登录失败")
```

```python
data = input(">>>")  
print("data")
```
特别注意：用户输入的任何内容本质上是字符串

1.提示输入姓名，然后给姓名后边拼接一个”烧饼“，最终打印结果
```python
name = input("请输入用户名:")
text = name + "烧饼"

print(text)
```
2.提示输入 姓名/位置/行为，然后做拼接并打印，xx在xxx做xx
```python
name = input("请输入用户:")
address = input("请输入地址:")
action = input("请输入行为:")

text = name + "在" + address + action
print(text)
```
3.提示输入两个数字，计算两个数字的和。
```python
num1 = input("请输入一个数字:") #字符串
num2 = input("请输入一个数字:")

value = int(num1) + int(num2)
print(value)

#如果num都写成num1，下面的数字会替代上边的数字，最后计算会只计算后输入的值
```

**8. 条件语句**
```python
if 条件 ：
    条件成立之后的代码···
	条件成立之后的代码···   
	条件成立之后的代码···    
	条件成立之后的代码···
else:
	条件不成立之后的代码···
	条件不成立之后的代码···
	条件不成立之后的代码···

```

```python
name = input("请输入用户名:")
if name == "alex":
	print("sb")
else:
	print("db")
```
提醒：缩进问题。后续的同级代码应该缩进一致（一般都是使用四个空格）tab键

**8.1 基本条件语句**
示例1
```python
print("start")
if True:
	print("123")
else:
	print("456")
print("结束")

#输出结果
开始
123
结束
```

示例2
```python
print("开始")
if 5==5:
	print("123")
else:
	print("456")
print("结束")
```

示例3
```python
num = 19
if num > 10:
	print("num变量对应值大于10")
else:
	print("num变量对应值不大于10")
```

示例4
```python
username = "yuyumeng"

if username == "yuyumeng" or username == "gaopotato"
	print("VIP membership")
else:
	print("普通用户")
```

示例5
```python
username = "yuyumeng"
password = "666"
if username == "yuyumeng" and password == "666":
	print("恭喜你，登录成功")
else:
	print("登录失败")
```

示例6
```python
number = 19
if number%2 == 1:
	print("number是奇数")
else:
	print("number是偶数")
```

```python
number = 19
data = number%2 == 1
if data:
	print("number是奇数")
else:
	print("number是偶数")
```

示例7
```python
if 条件:
	成立
else:
	不成立
```

```python
print("开始")
if 5 == 5:
	print("5等于5")
print("结束")
```

**8.2 多条件判断**
```python
if 条件A:
	A成立，执行此缩进的所有代码
	···
elif 条件B:
	B成立，执行词缩进中的所有代码
	···
elif 条件C:
	C成立，执行此缩进中所有代码
	···
else:
	上述ABC都不成立
```
```python
num = input("请输入数字")
data = int(num)
if data > 6:
	print("太大了")
elif data == 6:
	print("刚刚好")
else:
	print("太小了")
```
```python
score = input("请输入分数:")
data = int(score)

if data > 90:
	print("优")
elif data > 80:
	print("良")
elif data > 70:
	print("中")
elif data > 60:
	print("差")
else:
	print("不及格")
```

**8.3 多条件嵌套**
```python
if 条件A:
	···
elif 条件B:
	···
```
```python
if 条件A:
	if 条件A1:
		····
	else:
		····
elif 条件B:
	···
```

模拟10086客服
```python
print("欢迎致电10086，我们提供如下服务：1. 话费相关；2. 业务办理；3. 人工服务")

choice = input("请选择服务序号")

if choice == "1":
	print("话费相关业务")
	cost = input("查询话费请按1；交话费请按2")
	if cost == "1":
		print("查询话费余额为100")
	elif cost == "2":
		print("交话费")
	else:
		print("输入错误")
elif choice == "2":
	print("业务办理")
elif choice == "3":
	print("人工服务")
else:
	print("序号输入错误")
```

**总结**
1 什么是编码？打开文件为什么会出现乱码？
	有可能是文件编码和解释器编码的形式不一致
2 pycharm 如何设置文件编码
3 python解释器打开代码文件，默认使用的编码是什么，如何修改
4 print 输入
5 各数据类型格式 以及相关之间如何实现转换？
6 变量的命名规范
7 用户通过input输入内容均为字符串类型
8 条件语句

作业
1 谈谈你了解的编码以及为什么会出现乱码现象？
```answer
出现乱码是因为编码时候采用的规范与编辑器的读取规范不一致，例如编码时候采用的是utf-8，但是读取的时候用是gbk的读取方式，或者数据出现丢失，例如101010010101中间丢了个1，编码就是利用编码规范写语句，达成某项功能
```
2 python解释器默认编码是什么？如何修改？
```answer
python解释器的默认编码是utf-8,修改操作可以在pycharm的右下角进行修改
-*- coding:utf-8 -*- 也可以输入上述的代码让解释器按照输入的编码规则阅读
```
3 用print打印出下面的内容:
```text
文能提笔安天下，
武能上马定乾坤。
心存谋略何人胜，
古今英雄唯是君。
```
```python
print("文能上马安天下,")
print("武能上马定乾坤。")
print("心存谋略何人胜，")
print("古今英雄唯是君。")
```
```python
print("文能提笔安天下", end="，")
print("武能上马定乾坤", end="。")
```
```python
text = """
ADAGA
ADFASDF
ADFSD
"""

print(text)
```
4 变量名的命名规范和建议
```answer
变量命名的规范是，不能由数字，字母，下划线之外的东西，并且 数字不能作为开头，而且不可以使用python已经规范的，例如if，else，elif，and，end等等，三个规范
建议是变量命名尽量能看到名称知道它的意思，用下划线作为单词之间的连接线，两个建议
```
5 如下哪个变量名是正确的
```text
name = "wupeiqi"
_ = "alex"
_9 = "老男孩"
9name = "baolang"
oldboy(edu = 666
 ```
```answer
123是对的
后面两个一个是数字开头，一个是用了括号
```
 6 设定一个理想数字比如：666，让用户输入数字，如果比666大，显示结果大了，如果比666小，显示结果小了，只有等于666，显示猜测结果正确
```python
num = input("请输入数字：")
new_num = int(num)
if new_num > 666:
	print("结果大了")
elif new_num == 666:
	print("猜对了")
else:
	print("结果小了")
#其中三个顺序可以变化
```
 7 提示用户输入，“爸爸”， 判断用户输入正确与否，如果正确，则提示真聪明，错误就是你是傻逼吗
```python
me = input("猜猜我是谁？")
if me == "爸爸":
	print("真聪明")
else:
	print("你是不是傻")

```
 8 写程序，成绩由ABCDE5个等级，与分数对应的关系如下
```text
A 90-100
B 80-90
C 70-80
D 60-70
E 0-60
``` 
要求用户输入0-100后可以正确打印对应的成绩
```python
grade = input("请输入您的成绩")
new_grade = int(grade)
if 100 > new_grade > 90:
	print("A")
elif 90 > new_grade > 80:
	print("B")
```
```python
#老师的写法，其实规范写法就是我写的那样子
score = input("请输入分数")
data = int(score)\

if data >= 90 and data <= 100:
	print("A")
elif data >= 80 and data <90:
	print("B")
else:
	print("mistake")
```


