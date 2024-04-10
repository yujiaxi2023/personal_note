## 1.4 动态参数

动态参数，定义函数的时候在形参位置使用`* 或者**`可以接 任意的参数
```python
def func(*args, **kwargs):  
    print(args, kwargs)  
  
  
func("baoqiang", "jielun", nl="alex", n2="eric")
```

在定义函数的时候可以用`*和**`，其实在执行函数的时候也可以使用
- 形参固定，实参用`*和**`
```python
# 定义函数的时候可以用*和**，执行函数的时候也可以使用  
# 形参固定，实参用*和**  
def func(a1, a2):  
    print(a1, a2)  
  
  
func(11, 22)  
func(a1=1, a2=2)  
  
func(*[11, 22])  
func(**{"a1": 11, "a2": 22})
```
`*`在这里是按照位置参数传入到a1和a2
`**` 在这里是打散字典，通过关键字传递给参数


- 形参用`*和**`实参也用`*和**`
```python
# 形参用*和**，实参也用*和**  
def func(*args, **kwargs):  
    print(args, kwargs)  
  
  
func(11, 22)  
func(11, 22, name="wupeiqi", age=18)  
# 这样传参是会将这个直接传入args，得到一个元组，然后后边是一个空字典
func([11, 22, 33], {"k1": 1, "k2": 2})  

# 这样传参是将列表数据循环拷贝到args，如果是字典会循环拷贝键值到kwargs
func(*[11, 22, 33], **{"k1": 1, "k2": 2})
```

`*`传到args
`**`传到kwargs


所以在使用format字符串格式化的时候，可以这样：
```python
# 在执行format的时候  
v1 = "I am {}, age{}".format("wupeiqi",18)  
v2 = "I am {name}, age {age}".format(name="wupeiqi",age=18)  
print(v1, v2)  
  
v3 = "I am {}, age: {}.".format(*["wupeiqi",18])  
v4 = "I am {name}, age: {age}.".format(**{"name":"wupeiqi","age":18})
```

练习题
1. 写结果
```python
def func(*args,**kwargs):  
    print(args,kwargs)  
  
params = {"k1":"v2","k2":"v2"}  
func(params) # ({"k1":"v2","k2":"v2"}), {}  
func(**params) # () {"k1":"v2","k2":"v2"}
```

2. 读取文件中的url和标题，根据url下载视频到本地（标题作为文件名）
```python
import requests  
  
def download_video(title,url):  
    """  
    下载并保存视频  
    Parameters    ----------    title 视频标题  
    url 视频url  
  
    Returns    -------  
    """  
    res = requests.get(  
        url=url,  
        headers={  
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10 15 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88Safari/537.36 FS"  
        }  
    )  
    with open(f"{title}.mp4", mode="wb") as f:  
        f.write(res.content)  
  
  
# 读取文件  
  
with open("db.csv",mode='r',encoding='utf-8') as file_object:  
    for line in file_object:  
        line = line.strip()  
        row_list = line.split(",")  
        download_video(*row_list)
```

