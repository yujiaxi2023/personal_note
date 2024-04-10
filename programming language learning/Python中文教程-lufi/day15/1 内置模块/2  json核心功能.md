## json

json模块,是python内部的一个模块,可以将python的数据格式转换为json格式的数据,也可以将json格式的数据 转换为python的数据格式

json格式,是一个数据格式(本质上是一个字符串,常用于网络数据传输)

```python
# python中的数据类型格式
data = [
	{'id': 1, 'name': 'wupeiqi', 'age': 18},
	{'id': 2, 'name': 'alex', 'age': 18},
	('wupeiqi',123)
]

# json 格式
value = '[{"id": 1, "name": "wupeiqi", "age":18},{"id":2, "name":"alex", "age":18},["wupeiqi",123]]'
```

### json核心功能

json格式的作用?
```
跨语言数据传输,例如:
A系统使用python开发,有列表类型和字典类型等.
B系统用java开发,有数组,map等类型

语言不通,基础数据类型格式都不一样

为了方便数据传输,大家约定一个格式:json格式,每种语言都是将自己的数据类型转换为json格式,也可以将json格式的数据转换为自己的数据类型
```

![[Pasted image 20231026185942.png]]

python数据类型和json格式的相互转换:
- 数据类型 -> json 一般称为: 序列化
```python
import json  
  
data = [  
    {'id':1,"name":"吴佩琦",'age':19},  
    {'id':2,"name":"alex",'age':22}  
]  
  
res = json.dumps(data)  
print(res)  
# [{"id": 1, "name": "\u5434\u4f69\u7426", "age": 19}, {"id": 2, "name": "alex", "age": 22}]  
  
res = json.dumps(data, ensure_ascii=False)  
print(res)  
# [{"id": 1, "name": "吴佩琦", "age": 19}, {"id": 2, "name": "alex", "age": 22}]
```

- json格式 -> 数据类型,一般称为: 反序列化
```python
import json

data_string = '[{"id":1,"name":"吴佩琦","age":19},{"id":2,"name":"alex","age":20}]'  
# data_string = '[{"id":1,"name":"吴佩琦","age":19},{"id":2,"name":"alex","age":20}]'  
  
data_list = json.loads(data_string)  
  
print(data_list)
```

### 练习题

1. 写网站,给用户返回json格式的数据
- 安装flask模块,协助我们快速写网站
`pip3 install flask`
- 使用flask写网站
```python
import json  
from flask import Flask  
  
app = Flask(__name__)  
  
def index():  
    return "HOMEPAGE"  
  
def users():  
    data = [  
        {'id': 1, "name": "吴佩琦", 'age': 19},  
        {'id': 2, "name": "alex", 'age': 22},  
    ]  
    return json.dumps(data)  
  
  
app.add_url_rule('/index/', view_func=index, endpoint='index')  
app.add_url_rule('/users/', view_func=users, endpoint='users')  
  
if __name__ == "__main__":  
    app.run()
```

2. 发送网络请求,获得json格式数据并处理
```python
import json  
import requests  
  
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8%sort=recommend&page_limit=5&page_start=20"  
  
res = requests.get(  
    url=url,  
    headers={  
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88Safari/537.36"  
    }  
)  
  
"""  
豆瓣电影中页面其实就是向豆瓣发送请求返回的json文件，然后使用CSS创建的网页  
"""  
# json格式  
print(res.text)  
  
# json格式转换为python数据类型  
data_dict= json.loads(res.text)  
print(data_dict)
```
