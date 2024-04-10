python中提供了re模块,可以处理正则表达式并对文本进行处理

- findall,获取匹配到的所有数据
```python
# findall 获得匹配到的所有数据  
text = "das130429191912015219k13042919591219521Xkk"  
data_list = re.findall("(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)", text)  
print(data_list) # [('130429', '1919', '12', '01', '521', '9'), ('130429', '1959', '12', '19', '521', 'X')]
```

- match,从起始位置开始匹配,匹配成功返回一个对象,未匹配成功返回None
```python
# match 从其实位置开始匹配,匹配成功返回一个对象,未匹配成功返回None  
text = "大小逗2B最逗3B换了"  
data = re.match("逗\dB", text)  
print(data) # None
```
只能返回匹配成功的第一个对象
而且必须开头要是能匹配上,这里用逗开头,而句子是大开头,所以返回值一定是None
下面的例子就能返回对的内容
```python
text = "逗2B最逗3B换了"  
data = re.match("逗\dB", text)  
if data:  
    print(data.group()) # 逗2B
```
采集数据的时候并不是很好用
一般适用于监测用户输入的数据是否是我们需要的格式

- search,浏览整个字符串去匹配第一个,未匹配成功就返回None
```python
# search 浏览整个字符串匹配第一个,未匹配成功返回None  
text = "大小逗2B最逗3B换了"  
data = re.search("逗\dB", text)  
if data:  
    print(data.group()) # 逗2B
```
只匹配第一个,但是并不强制要求开头一定是检索内容的开头

- sub,替换匹配成功的位置
```python
# sub 替换匹配成功的位置  
text = "逗2B最逗3B换了"  
data = re.sub("\dB","沙雕",text)  
print(data) # 逗沙雕最逗沙雕换了
```
sub比replace更好用,因为可以指定动态的值
就像图中一样,可以选择不同的数字等等
```python
# sub 替换匹配成功的位置  
text = "逗2B最逗3B换了"  
data = re.sub("\dB","沙雕",text,1)  
print(data) # 逗沙雕最逗沙雕换了
```
也支持选择替换几个

- split,根据匹配成功的位置分割
```python
# split 根据匹配成功的位置分割  
text = "逗2B最逗3B换了"  
data = re.split("\dB",text)  
print(data) # ['逗', '最逗', '换了']  
  
text = "逗2B最逗3B换了"  
data = re.split("\dB",text,maxsplit=1)  
print(data) # ['逗', '最逗3B换了']
```
可以选择从第几个开始分割,从左到右匹配到了就从这里分割

- finditer
```python
# finditer  
text = "逗2B最逗3B换了"  
data = re.findall("\dB", text)  
print(data) # ['2B', '3B']
```
跟find类似
如果你findall,就会一下提取出所有的元素出来,会占用内存
finditer得到的结果是一个迭代器,可调用的迭代器
```python
data = re.finditer("\dB",text)  
for item in data:  
    print(item.group())
```
.group就可以把匹配的文本拿到
还是使用findall多,因为字符串一般不会特别大

finditer还可以进行可命名的分组
(?P<名称>正则)
```python
text = "das130429191912015219k13042919591219521Xkk"  
data_list = re.findall("\d{6}(\d{4})(\d{2})(\d{2})\d{3}[\dX]", text)  
print(data_list) # [('1919', '12', '01'), ('1959', '12', '19')]  
# 分组得到的数据是以元组存在的,如果我可以给这些元组都起别名  
  
text = "das130429191912015219k13042919591219521Xkk"  
data_list = re.findall("\d{6}(?P<YEAR>\d{4})(?P<MONTH>\d{2})(?P<DAY>\d{2})\d{3}[\dX]", text)  
print(data_list) # [('1919', '12', '01'), ('1959', '12', '19')]  
#使用findall结果是一样的  
  
  
text = "das130429191912015219k13042919591219521Xkk"  
data_list = re.finditer("\d{6}(?P<YEAR>\d{4})(?P<MONTH>\d{2})(?P<DAY>\d{2})\d{3}[\dX]", text)  
for item in data_list:  
    print(item.groupdict()) # group可以获取一些正则表达式的捕获组  
"""  
{'YEAR': '1919', 'MONTH': '12', 'DAY': '01'}  
{'YEAR': '1959', 'MONTH': '12', 'DAY': '19'}  
"""
```

要注意group和groupdict的用法
`group` 方法是 Python 中正则表达式对象（`re` 模块）的一个方法，它用于获取正则表达式匹配的文本。正则表达式通常会定义一些捕获组（capturing groups），`group` 方法可以用来访问这些捕获组。
具体来说，`group` 方法通常用于 `re` 模块的正则表达式对象的匹配结果，如 `match` 或 `search`。你可以使用 `group` 方法来获取匹配的文本，也可以提供一个捕获组的索引，以获取特定的捕获组的文本。

`groupdict` 方法是 Python 正则表达式中的一个方法，用于获取捕获组的字典。正则表达式通常包含多个捕获组，`groupdict` 方法会将这些捕获组的名称和对应的文本以字典的形式返回。

捕获组（capture group）是正则表达式中的一种概念，它不是指内存地址，而是指正则表达式中用括号括起来的部分。捕获组的主要作用是捕获（或提取）与特定模式匹配的文本，以便进一步处理或检索。

当您在正则表达式中使用括号，例如 `( ... )`，括号内的部分会被视为一个捕获组。这允许您标识并获取匹配这个模式的文本片段。