课程目标：掌握Python基础中必备的语法知识。
课程概要：
·循环语句
·字符串格式化
·运算符（面试题）

**1.循环语句**
· while 循环
· for 循环

```python
while 条件:
    ···
    ···
    ···
# 三句语句执行完成后会循环，条件成立就进行代码，然后返回再查找条件，成立接着执行
```
```python
print("123")
while 条件:
	···
	···
	···
print("456")
```

**1.1 循环语句基本使用**
示例1：
```python
print("start")
while True:
	print("alex is a pig")
print("end")

#输出
start
alex is a pig
···
```

示例2：
```python
print("start")
while 1 > 2:
	print("男儿当自强")
print("end")

#输出：
start
end
```

示例3：
```python
data = True
print("start")
while data:
	print("男儿当自强")
print("end")

#输出：
start
男儿当自强
男儿当自强
···
```

示例4：
```python
print("start")
flag = True
while flag:
	print("long river")
	flag = False
print("end")

#输出
start
long river
end
```

示例5：
```python
print("start")
num = 1
while num < 3:
	print("long river")
	num = 5
print("end")

#输出：
start
long river
end
```

示例6：
```python
print("start")
num = 1
while num < 5:
	print("life")
	num = num + 1
print("end")

#输出：
start
life
life
life
life
end
```

```practice
repeat 3 times I love you
```

```python
num = 1
while num < 4:
	print("I love you")
	num = num + 1
print("end")
```

**1.2 综合小案例**
请实现一个用户登录系统，如果密码错误则反复提示让用户提示重新输入，直到输入正确停止

```python
# 实现一个用户登录系统  
  
print("start lufei system")  
  
flag = True  
  
while flag:  
    user = input("please input user name")  
    pwd = input("please input password")  
    if user == "yu" and pwd == "luffy":  
        print("success")  
        flag = False  
    else:  
        print("wrong")  
  
print("system end")
```

练习题
1 补充代码实现
	猜数字，设定一个理想数字66，一直提示让用户输入数字，如果大于66，显示结果大，如果小于66，显示结果小，只有显示等于66，显示正确，然后退出循环
```python
number = 66
flag = True
while flag:

```
2 使用循环语句输出1-100 所有整数
3 使用循环输出1234568910，除了7之外
4 输出1-100所有奇数
5 求1-100所有整数的和
7 输出10-1所有整数

1
```python
number = 66  
flag = True  
while flag:  
    num = input("please input number")  
    new_num = int(num)  
    if new_num > number:  
        print("over")  
    elif new_num == number:  
        print("right")  
        flag = False  
    else:  
        print("less")  
  
print("system end")

# teacher answer
data = True
while data:
	num = input("num")
	num = int(num)
	if num > 66:
		print("over")
	elif num < 66:
		print("less")
	else:
	
		print("right")
		data = False
```

2
```python
print("are you willing to start loop?")  
toggle_01 = input("input your answer")  
if toggle_01 == "yes":  
    num = 1  
    while num <= 100:  
        print(num)  
        num = num + 1  
else:  
    print("system end")
```

3
```python
num = 1  
while num <= 10:  
    if num == 7:  
        pass  
        # nothing happen  pass means nothing happen
    else:  
        print(num)  
    num = num + 1

# another way
num = 1  
while num <= 10:  
    if num != 7:  # "!=" means unequal
        print(num)  
    num = num + 1
```

4
```python
num = 1  
while num <= 100:  
    if num % 2 == 1:  
        print(num)  
    num = num + 1
```

5
```python
num = 1  
while num <= 100:  
    if num % 2 == 0:  
        print(num)  
    num = num + 1
```

6
```python
total = 0  
num = 1  
while num < 101:  
    total = total + num  
    num = num + 1  
print(total)
```

7
```python
num = 10  
while num > 0:  
    print(num)  
    num = num - 1
```

思考题：求1-100以内所有整数这样的结果： 1-2+3-4+5-6

```python
total = 0  
num = 1  
while num < 101:  
    if num % 2 == 1:  
        total = total + num  
    else:  
        total = total - num  
    num = num + 1  
print(total)
```

**1.3 break**
break 用于在while循环中帮助你终止循环的
```python
print("start")
while True:
	print("1")
	break
	print("2")
print("end")

#  输出
start
1
end
```

示例1
```python
print("start")
while True:
	print("red flag")
	break
	print("sword thunder")
	print("warriors")
print("end")

# 输出
start
red flag
end
```

示例2
```python
print("start")
i = 1
while True:
	print(i)
	i = i + 1
	if i == 101:
		break
print("end")

# 输出
start
1
2
···
100
end
```

示例3
```python
print("start system")
while True:
	user = input("input user name:")
	pwd = input("input pwd:")
	if user == "yu" and pwd == "oldguy":
		print("success")
		break
	else:
		print("wrong pwd")
print("system end")

# 输出
start
>>>input user name
>>>input pwd
success
system end

wrong
re login
```

**1.4 continue**

Continue是用来实现，在循环中用于结束本次循环，开启下次循环
```python
print("start")
while True:
	print(1)
	continue
	print(2)
print("end")

# 在continue后面就不再继续这个while里面的代码了 返回到while的地方开始
```

示例1
```python
print("start")
while True:
	print("flag flying")
	continue
	print("sword out")
	print("warriors win")
print("end")

#输出
start
flag flying
flag flying
···
```

示例2
```python
print("start")
i = 1
while 1 < 101:
	if i == 7:
		i = i + 1
		continue
	print(i)
	i = i + 1
print("end")

#输出 其中的7没有输出是因为当i == 7的时候continue 后面的print没有执行
start
1
2
3
4
5
6
8
9
···
100
end
```

示例3
```python
print("start")
i = 1
while True:
	if i == 7:
		i = i + 1
		continue
	print(i)
	i = i + 1
	if i == 101:
		break
print("end")

# 输出
start
1
2
3
4
5
6
8
9
···
100
end
```
break和continue都是控制循环过程的，能够用break continue的可以尽量不要使用if else语句，因为使用这两个代码可以简化编写流程，其中continue是停止本次循环，break是停止所有循环

**1.5 while else**
```python
while requirement:
	code
else:
	code
```
当while中的code不成立，else中的代码会执行
```python
while False:
	pass
else:
	print(12)
```
```python
num = 1
while num < 5:
	print(num)
	num = num + 1
else:
	print(444)

#输出
1
2
3
4
444
```
```python
while True:
	print(123)
	break
else:
	print(666)

# 输出 break会把else也终止
123
```


**2. 字符串格式化**

字符串格式化，使用更加便捷的形式实现字符串的拼接

**2.1 %**
2.1.1 基本格式化操作
```python
name = "yujiaxi"
# 占位符
text = "my name is %s, student desu"  %"yujiaxi"

text = "my name is %s, student desu"  %name
```
```python
name = "yujiaxi"
age = 18

text = "my name is %s, %s years old" %("yujiaxi",18)
text = "my name is %s, %s years old" %(name,age)# 此处对应的是前面已经有了name和age变量的定义，但是这一行并不专业
text = "my name is %s, %d years old" %(name,age)# %d是专门给整型的占位符
```
```python
message = "%(name)s你什么时候过来 %(user)s不在家" %{"name":"死鬼","user":"alex"}
```

2.1.2 百分比的表示
```python
text = "bro, i almost finished 90%"
print(text)
```
```python
text = "%s, i almost finished 90%" %"bro"
print(text)# 此处会报错 正确格式如下，需要再%后面添加一个%
text = "%s, i almost finished 90%%" %"bro"
print(text)
```
一旦字符串格式化中存在%的形式，一定要加两个%实现输出一个%

**2.2 format（推荐）**
```python
text = "my name is xx, 18 years old"
text = "my name is (0), 18 years old".format("yujiaxi")
text = "my name is (0), (1) years old".format("yujiaxi",18)
text = "my name is (0), (1) years old, real name is (0)".format("yujiaxi",18)
```
```python
text = "my name is {}, 18 years old".format("uikoaxo")
text = "my name is {}, {} years old".format("yujiaxi",18)
text = "my name is {}, {} years old, real name is {}".format("yujiaxi",18,"yujiaxi")
```
```python
text = "my name is {ni}, 18 years old".format(ni="yujiaxi")
text = "my name is {ni}, {age} years old".format(ni="yujiaxi",age=18)
text = "my name is {ni}, {age} years old, real name is {ni}".format(ni="yujiaxi",age=18)
```
```python
text = "my name is {0}, {1} years old"
data01 = text.format{"yujiaxi",18}
data02 = text.format{"ahog",1123}
```
```python
text = "my name is %s,  %d years old"
data1 = text %("yujiaxi",20)
data2 = text %("adf",2)
```


**2.3 f**

发展到python 3.6版本，出现了f作为字符串格式化的功能，以前的版本都是不可实现的
```python
text = f"sister likes {'run'}, she is sweaty."
```
```python
action = "run"
text = f"sister like {action}, she is sweaty."
```
```python
name = "miao"
age = 19
text = f"sister's name is {name}, {age} years old."
print(text)
```
```python
text = f"嫂子的名字叫喵喵，今年{19 + 2}岁"
print(text)
```
```python
# python3.8引用的
text = f"嫂子的名字叫喵喵，今年{19 + 2=}岁"
print(text)
```
```python
# 进制转换
v1 = f"嫂子今年{22}岁"
print(text)

v2 = f"嫂子今年{22:#b}岁"#转换成二进制
print(text)

v3 = f"嫂子今年{22:#o}岁"#转换为八进制
print(text)

v4 = f"嫂子今年{22:#x}岁"#转换为十六进制
print(text)
```
```python
# 执行函数
text = "我是{'alex'}，我爱大铁锤"

name = "alex"
text = f"我是{name}，我爱大铁锤"

name = "alex"
text = f"我是{name,upper()}，我爱大铁锤"
print(text)
```

**3.运算符**
**算数运算符**
![[Pasted image 20230322202453.png]]
```python
print( 9//2 )
```
**比较运算符**
![[Pasted image 20230322202712.png]]
```python
if 1 > 2:
	pass
while 1 > 2:
	pass

data = 1 == 2
```
**赋值运算**
![[Pasted image 20230322202847.png]]
```python
num = 1
while num < 100:
	print(num)
	num = num + 1

# 可以写成
num = 1
while num < 199:
	print(num)
	num += 1
```
**成员运算**
![[Pasted image 20230322203100.png]]
```python
vl = "le" in "alex" # True/False 
# 让用户输入一段文本，检测里面有没有敏感词
text = input("please input:")
if "aoisora" in text:
	print("NSFW")
else:
	print(text)
```
**逻辑运算**
![[Pasted image 20230322203814.png]]
```python
if username == "alex" and pwd = "123":
	pass

data = 1 > 2
if not data:
	pass
```

![[Pasted image 20230402194538.png]]
**运算符优先级**
先做算数再比较,先比较再进行逻辑and or not
逻辑运算符中是not>and>or
拿不准就加括号()先计算括号里面再计算括号外边

**3.2 面试题**
逻辑运算中的and 和 or
```python
v1 = name == "alex" and pwd == "123"
# v1 = True and False

if name == "alex" and pwd == "123"
	pass
```
```python
v2 = "wupeiqi" and "alex"

# 第一步：将逻辑运算符前后的值转换为布尔值 True and True
# 第二步：判断本次操作取决于谁？由于前面为True 所以本次逻辑判断取决于后边的值
# 所以后面的值等于多少最终结果等于多少
# 所以本次结果是v2 = “alex”
```
```python
v3 = "" and "alex"
# 第一步：判断and前后的布尔值为False and True
# 第二步：判断本次操作取决于谁？前面的是False。所以取决于前边的值
# 所以，前面的值等于多少最后结果就是多少
# 所以v3 = “”
```
```python
v4 = 1 or 8
# 第一步：将and前后的值转换为bool True and True
# 第二步：判断操作取决于谁？ 前面是True，所以本次取决于前面的值
# 所以本次v4 = 1
```
```python
v5 = 0 or 8
# 第一步: 将or前后的值转换为False or True
# 第二部：取决于因为前面是False，所以取决于后边的值
# v5 = 8
```
```python
v1 = 1 or 2
v2 = -1 or 3
v3 = 0 or -1
v4 = 0 or 100
v5 = "" or 10
v6 = "wupeiqi" or ""

print(v1,v2,v3,v4,v5,v6)
# or，看第一个值，如果第一个值为真，结果就应该是第一个，否则就是第二个
```
```python
v1 = 4 and 8
v2 = 0 and 6
v3 = -1 and 88
v4 = "" and 7
v5 = "吴佩琦" and ""
v6 = "" and 0
v7 = 0 and "中国"

print(v1,v2,v3,v4,v5,v6,v7)
# and，看第一个值，如果第一个值为真，结果就应该是第二个值，否则结果就是第一个值
```
```answer
v1 = 1
v2 = -1
v3 = -1
v4 = 100
v5 = 10
v6 = wupeiqi

v1 = 8
v2 = 0
v3 = 88
v4 = “”
v5 = “”
v6 = “”
v7 = 0
```

**面试题**
```python
v1 = 0 or 4 and 3 or 7 or 9 and 6
     0 or 3 or 7 or 9 and 6
     0 or 3 or 7 or 6
     3 or 7 or 6
     3 or 6
     3
     
v2 = 8 or 3 and 4 or 2 and 0 or 9 and 7
     8 or 4 or 2 and 0 or 9 and 7
     8 or 4 or 0 or 9 and 7
     8 or 4 or 0 or 7
     8
     
v3 = 0 or 2 and 3 and 4 or 6 and 0 or 3
     0 or 4 or 0 or 3
     4 or 0 or 3
     4
```
有多个and和or就先计算and再计算or
```python
v4 = not 8 or 3 and 4 or 2
     False or 3 and 4 or 2
     False or 4 or 2
     4 or 2
     4
```
最先算not再计算and再or
not 8 相当于not True

**总结**
1.while循环语句
2.break和continue关键字的作用
3.三种字符串格式化
4.基本运算符

**作业**
1.判断下列逻辑语句的True,False
```python
1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
```
2.求出下列逻辑语句的值
```python
8 or 3 and 4 or 2 and 0 or 9 and 7
0 or 2 and 3 and 4 or 6 and 0 or 3
```
3.下列结果是什么
```python
6 or 2 > 1
3 or 2 > 1
0 or 5 < 4
5 < 4 or 3
2 > 1 or 6
3 and 2 > 1
0 and 3 > 1
2 > 1 and 3
3 > 1 and 0
3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
```
4.实现用户登录系统,并且要支持连续三次输错后直接退出,并且,每次输入错误的时候显示错误次数
5.猜年龄
要求用户最多尝试3回,不行的话直接退出,猜对了打印恭喜并退出
6.猜年龄
要求最多尝试3回,每次3词之后,没有猜对,就问用户是否希望继续,如果回答Y,就可以再猜3次,以此往复,如果回答N,就退出程序,猜对了就直接退出

```answer
1.
1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
False or True or False and True and True or False
False or True or False and True or False
False or True or False or False
True

not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
not True and True or False and True and True or False
False and True or False and True and True or False
False or False and True or False
False or Fasle or False
False
```
```answer
2.
8 or 3 and 4 or 2 and 0 or 9 and 7
8 or 4 or 0 or 7
8

0 or 2 and 3 and 4 or 6 and 0 or 3
0 or 3 and 4 or 0 or 3
0 or 4 or 0 or 3
4
```
```answer
3.
6 or 2 > 1
6

3 or 2 > 1
3

0 or 5 < 4
False

5 < 4 or 3
3

2 > 1 or 6
True

3 and 2 > 1
True

0 and 3 > 1
0

2 > 1 and 3
3

3 > 1 and 0
0

3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
True and 2 or True and 3 and 4 or True
2 or 3 and 4 or True
2 or 4 or True
2
```

4.自己的代码,写不下去了
```python
print("system start")
num = 1
while num < 3:
	user = input("input your user name:")
	pwd = input("input your pwd:")
	if user == "wupeiqi" and pwd == "123":
		print("log in success") 
	else:
		print("wrong")
		num = num + 1
```
4.正确答案
```python
count = 0
while count < 3:
	count += 1 # 设定count = 0后,让while循环中的count<3,然后每次while循环count自己+1
	user = input("input your user name")
	pwd = input("input your pwd")
	if user == "wupeiqi" and pwd == "123":
		print("success")
		break # 保证在输入成功之后break掉while循环
	else:
		message = f"user name or pwd wrong, remain {3 - count} times" # 格式化字符串
		print(message)
```
```python
count = 3
while count > 0:
	count -= 1 # 设定count = 3后,让while循环中的count>0,然后每次while循环count自己-1
	user = input("input your user name")
	pwd = input("input your pwd")
	if user == "wupeiqi" and pwd == "123":
		print("success")
		break # 保证在输入成功之后break掉while循环
	else:
		message = f"user name or pwd wrong, remain {count} times" # 格式化字符串
		print(message)
```

5.正确答案
```python
count = 0
while count < 3:
	count += 1
	age = input("please input age:")
	age = int(age)
	if age == 73:
		print("Congratulations")
		break
	else:
		print("wrong")

print("system end")
```

6.正确答案
```python
count = 0
while count < 3:
	count += 1
	age = input("please input age:")
	age = int(age)
	if age == 73:
		print("Congratulations")
		break
	else:
		print("wrong")

	if count == 3:
		choice = input("if you want play(Y/N)?")
		if choice == "N":
			break
		elif choice == "Y":
			count = 0
			continue
		else:
			print("mistake")
			break

print("system end")
```

