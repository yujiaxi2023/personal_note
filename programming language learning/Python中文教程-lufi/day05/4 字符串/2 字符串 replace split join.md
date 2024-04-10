**7. 字符串内容替换，得到一个新的字符串**
```python
data = "you are a good man"

value = data.replace("good man","bitch")
print(data) # you are a good man
print(value) # you are a bitch
```
```python
# example
video_file_name = "love action movies.mp4"

new_file_name = video_file_name.replace("mp4","avi") # "love action movies.avi"
final_file_name = new_file_name.replace("action","reaction") # "love reaction movies.avi"
print(final_file_name)
```
```python
# example
video_file_name = "high resolution love action movies,mp4"
new_file_name = video_file_name.replace("mp4","avi") # "high resolution love action movies.avi"
final_file_name = video_file_name.replace("high","low") # "low resolution love action movies.mp4"
print(final_file_name)
```
```python
# example
content = input("please comment") # alex is fucking dog
v1 = content.replace("fucking","**") # alex is ** dog
v2 = v1.replace("dog","**") # alex is ** **
print(content)
# 这里变量起名太多了
content = input("please input comment") # alex is a fucking dog
content = content.replace("fucking","**") # alex is a ** dog
content = content.replace("dog","**") # alex is a ** **
content = content.replace("dog","**") # alex is a ** **
content = content.replace("dog","**") # alex is a ** **
content = content.replace("dog","**") # alex is a ** **
print(content) # alex is a ** **
```
```python
# example
char_list = ["dick","fuck","pig"]

content = input("please input comment")
for item in char_list:
	# item = "fuck"
	content = content.replace(item,"**")

print(content)
```

**8. 字符串的切割**
```python
data = "wupeiqi|root|wupeiqi@qq.com"
result = data.split('|') # 列表状态 ["wupeiqi","root","wupeiqi@qq.com"]
print(data) # "wupeiqi|root|wupeiqi@qq.com"
print(result) # output ["wupeiqi","root","wupeiqi@qq.com"] 根据特定字符其开后保存在列表中，方便以后的操作
```
```python
# example: identify the pwd of account correct or not
info = "wupeiqi|root" # 备注：字符串中储存了用户名和密码
user_list = info.split('|') # 得到了一个包含2个元素的列表 [ "wupeiqi","root"]
user_list[0] # 获取列表中的第一个元素
user_list[1] # 获取列表中的第2个元素

user = input("please input name:")
pwd = input("please input pwd:")

if user == user_list[0] and pwd == user_list[1]:
	print("success")
else:
	print("wrong")
```
扩展：
```python
data = "wupeiqi|root|wupeiqi@qq.com"  
v1 = data.split("|")  # ['wupeiqi'.'root','wupeiqi@qq.com']  
print(v1)  
  
v2 = data.split("|", 1)  # ['wupeiqi','root|wupeiqi@qq.com']  
print(v2)
# 如果加数字就是切割几个
```
扩展：
```python
# 从右向左切割
data = "wupeiqi,root,wupeiqi@qq.com"  
  
v1 = data.rsplit(',', 1) # ['wupeiqi,root', 'wupeiqi@qq.com']  
print(v1)
```
常用场景是有人给了你字符串，字符串是一个文件路径
```python
file_path = "xxx/xxxx/xxx/xxx.mp4"

data_list = file_path.rsplit(",",1) # ["xxx/xxxx/xx.xx/xxx","mp4"]
data_list[0]
data_list[1] # 就是扩展名
```

**9.字符串的拼接，得到一个新的字符串**
```python
data_list = ["alex","is","big guy"]

v1 = "*".join(data_list) # alex*is*big guy *起到连接符的作用
print(v1)
```


