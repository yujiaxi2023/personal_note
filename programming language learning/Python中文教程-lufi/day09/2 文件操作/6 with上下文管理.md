之前对文件进行操作，每次都需要打开和关闭文件，比较繁琐并且容易忘记关闭文件
之后进行操作可以使用with进行自动开关文件
```python
with open('info', mode='rb') as f:  
    data = f.read()  
    print(data)
```

python2.7之后支持同时打开多个文件进行上下文管理
```python
with open('info', mode='rb') as f1, open('t1.txt', mode='rb') as f2:
	pass
```