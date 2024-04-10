**逗号分隔值（comma-separated values）**
CSV 有时也称为字符分隔值，因为分割字符可以不是逗号，其文件以纯文本形式储存表格数据（数字和文本），需要利用open函数读取文件，根据分隔符特点进行处理

**案例**
ID 用户名 头像
下载图片并用用户名作为前缀

```python
import os  
import requests  
  
 with open('file/mv.csv',mode='r',encoding='utf=8') as file_object:  
     file_object.readline() # 忽略表头  
     for line in file_object:  
         # 默认会有一个换行符  
         user_id, username, url = line.strip().split(',')  
         print(username, url)  
         # 根据url下载图片  
         res = requests.get(  
             url = url,  
             headers = {  
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"  
            }  
         )  
         # 检查是否存在一个image目录储存数据  
         if not os.path.exists("images"):  
             # 创建image目录  
            os.makedirs('images')  
  
         # 将图片内容写入到文件  
         with open(f'images/{username}.png',mode='wb') as img_object:  
             img_object.write(res.content)
```

![[Pasted image 20230711154648.png]]
这是因为账号名字上面有特殊字符/所以会检测到目录错误
