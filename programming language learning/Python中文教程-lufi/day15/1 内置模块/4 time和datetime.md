## 时间处理

- UTC/GMT: 世界时间
- 本地时间: 本地时区的时间
python中关于时间处理的模块有两个,分别是time和datetime

### time
```python
import time  
  
# 获取当前时间戳（自1970-1-1 00：00）  
v1 = time.time() # 1698322087.7289875  
print(v1)  
  
# 分区  
v2 = time.timezone  
print(v2) # -32400 秒数  
print(v2/60/60) # -9.0 东9区  
  
# 地区时间戳  
v3 = v1 + v2  
print(v3) # 1698292414.8705702  
  
print("start")  
time.sleep(3) # 等3秒钟执行  
print("end")  
  
# 调试的时候，需要给人反应时间，所以会增加这个功能  
while True:  
    time.sleep(1)  
    print(123)
```

### datetime
平时开发过程中的事件一般是以如下三种格式存在:
- datetime
```python
from datetime import datetime, timedelta, timezone  
  
v1 = datetime.now() # 当前本地事件  
print(v1, type(v1)) # 2023-10-26 21:57:37.931804 <class 'datetime.datetime'>  
# 获得的是东9区的事件  
  
v2 = datetime.utcnow() # utc时间  
print(v2) # 2023-10-26 12:58:27.636202  
  
tz = timezone(timedelta(hours=8)) # 当前东8区的时间  
v3 = datetime.now(tz)  
print(v3) # 2023-10-26 20:59:35.499915+08:00  
  
# 时间的加减  
v4 = v1 + timedelta(days=140, hours=5, minutes=5, seconds=1992)  
print(v4) # 2024-03-15 03:50:25.193931  
# 两周内免登录，内部本质上是获取当前的时间戳，获得两周后的时间戳，确定用户过期的时间  
  
# datetime时间相减，计算间隔（不能相加）  
data = v1 - v2  
print(data.days, data.seconds / 60 / 60, data.microseconds) # 0 9.0 0  
  
# datetime类型 + timedelta类型 这个是可以相加的  
# datetime类型跟datetime类型只能支持减法，不能支持加法
```

- 字符串
```python
# 字符串  
# 字符串格式的时间 ----> 转换为datetime格式的时间  
text = '2021-11-11'  
v1 = datetime.strptime(text, '%Y-%m-%d') # %Y 年 -%m 月 -%d 天  
print(v1, type(v1)) # 2021-11-11 00:00:00 <class 'datetime.datetime'>  
  
# datetime格式 -----> 转换为字符串格式  
v1 = datetime.now()  
val = v1.strftime("%Y-%m-%d %H:%M:%S")  
print(val, type(val),type(v1)) # 2023-10-26 22:23:51 <class 'str'> <class 'datetime.datetime'>
```

- 时间戳
```python
# 时间戳  
# 时间戳格式 -----> 转换为datetime格式  
ctime = time.time()  
v1 = datetime.fromtimestamp(ctime)  
print(v1) # 2023-10-26 22:26:23.481230  
  
# datetime格式 -----> 转换为时间戳格式  
v1 = datetime.now()  
val = v1.timestamp()  
print(val) # 1698326783.48123
```

一般来说是使用datetime进行时间的 + - 比较
所以是字符串和时间戳跟datetime是可以互相转换
但是时间戳和字符串是不支持
![[Pasted image 20231026222914.png]]

### 练习题

```python
# 1. 日志记录，将用户输入的信息写入到文件，文件名格式为 年-月-日-时-分.txt  
from datetime import datetime  
  
while True:  
    text = input("please input content(q/Q):")  
    if text.upper() == "Q":  
        break  
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M")  
    file_name = f"{current_datetime}.txt"  
    with open(file_name, mode='a', encoding='utf-8') as file_object:  
        file_object.write(text)  
        file_object.flush()  

```

```python
# 2. 用户注册,将用户信息写入到excel,其中包含有:用户名,密码,注册时间 三列  
# 内置模块  
import os  
import hashlib  
from datetime import datetime  
# 第三方模块  
from openpyxl import load_workbook  
from openpyxl import workbook  
  
# 全局变量大写  
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_NAME = 'db.xlsx'  
  
def md5(origin):  
    hash_object = hashlib.md5("ladjfjadjqejnga".encode('utf-8'))  
    hash_object.update(origin.encode('utf-8'))  
    return hash_object.hexdigest()  
  
  
def register(username, password):  
    db_file_path = os.path.join(BASE_DIR, FILE_NAME)  
    # 文件存在  
    if os.path.exists(db_file_path):  
        # 打开文件  
        wb = load_workbook(db_file_path)  
        # 找到sheet  
        sheet = wb.worksheets[0]  
        # 读取现在有多少行,在后边1行开始写  
        next_row_position = sheet.max_row + 1  
    # 文件不存在  
    else:  
        wb = workbook.Workbook()  
        sheet = wb.worksheets[0]  
        next_row_position = 1 # 从这里开始写  
        # 当excel不存在的时候,应该是从1开始而不是从0开始  
  
    # 第n行第1列写用户名  
    user = sheet.cell(next_row_position, 1)  
    user.value = username  
    # 第n行第2列写密码  
    pwd = sheet.cell(next_row_position, 1)  
    pwd.value = md5(password)  
    # 第n行第3列写注册时间  
    ctime = sheet.cell(next_row_position, 3)  
    ctime.value = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 当前时间字符串格式化称为字符串  
  
    wb.save(db_file_path)  
  
  
  
def run():  
    while True:  
        username = input("please input username:")  
        if username.upper() == "Q":  
            break  
        password = input("please input password:")  
        register(username, password)  
  
  
if __name__ == '__main__':  
    run()
```