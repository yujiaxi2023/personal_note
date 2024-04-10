python的数据类型转换为json类型,对数据类型有要求,默认只会支持
![[Pasted image 20231026204832.png]]
```python
data = [  
    {'id':1,"name":"吴佩琦",'age':19},  
    {'id':2,"name":"alex",'age':22}  
]
```

其他类型如果想要支持,需要自定义JSONEncoder才能实现,例如:
```python
import json  
from decimal import Decimal  
from datetime import datetime  
  
data = [  
    {'id':1,"name":"吴佩琦",'age':19,'size':Decimal("18.99"),'ctime':datetime.now()},  
    {'id':2,"name":"alex",'age':22,'size':Decimal("9.99"),'ctime':datetime.now()},  
]  
  
class MyJSONEncoder(json.JSONEncoder):  
    def default(self, o):  
        if type(o) == Decimal:  
            return str(o)  
        elif type(o) == datetime:  
            return o.strftime("%Y-%M-%d")  
        return super().default(o)  
  
res = json.dumps(data,cls=MyJSONEncoder)  
print(res)
```

## 其他功能
json中常用的是
- json.dumps 序列化生成一个字符串
- json.loads 反序列化生成python数据类型

- json.dump 将数据序列化写入文件(不常用)
```python
import json

data = [  
    {'id':1,"name":"吴佩琦",'age':19},  
    {'id':2,"name":"alex",'age':22}  
]

file_object = open('xxx.json', mode='w', encoding='utf-8')  
  
json.dump(data, file_object)  
file_object.close()
```
需要要给文件对象
我们可以直接从生成的字符串复制进去也可以操作成功

- json.load 读取文件中的数据并反序列化为python的数据类型(不常用)
```python
import json

file_object = open('xxx.json', mode='r', encoding='utf-8') 

data = json.load(file_object)
print(data)

file_object.close()
```