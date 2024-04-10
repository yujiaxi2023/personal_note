可扩展标记语言，一种简单的数据存储语言，XML被设计用来传输和储存数据
- 存储，可以用来存放配置文件，例如：java的配置文件
- 传输，网络传输时候以这种格式存在，例如：早期ajax传输的数据 soap协议等
微信开发时候会用XML格式
收发消息，传送语音等需要用到XML格式

java对接的也是需要XML格式文件
![[Pasted image 20230711162950.png]]
分层data开始/data结束
子层country /country作为一层
在下面子层 rank /rank

一种数据储存格式，这些也可以进行增删改查操作
```xml
<data>
	<country name="Liechtenstein">
		<rank updated="yes">2</rank>
		<year>2023</year>
		<gdppc>141100</gdppc>
		<neighbor direction="E" name="Australia" />
	</country>
	<country name="Singapore">
		<rank updated="yes">5</rank>
		<year>2026</year>
		<gdppc>59900</gdppc>
		<neighbor direction="N" name="Malaysia" />
	</country>
	<country name="Panama">
		<rank updated="yes">69</rank>
		<year>2026</year>
		<gdppc>13600</gdppc>
		<neighbor direction="E" name="Colombia" />
	</country>
</data>
```

**1. 读取文件和内容**
```python
from xml.etree import ElementTree as ET  
  
# 直接解析xml文件  
tree = ET.parse('file/xo.xml')  
  
# 获取根标签  
root = tree.getroot()  
  
print(root) # <Element 'data' at 0x000001DBC70FAA20>
```

通过网络请求也可以打开获取根标签,通过网络获取的文本

```python
from xml.etree import ElementTree as ET  
  
content = """  
<data>
	<country name="Liechtenstein">
		<rank updated="yes">2</rank>
		<year>2023</year>
		<gdppc>141100</gdppc>
		<neighbor direction="E" name="Australia" />
	</country>
	<country name="Singapore">
		<rank updated="yes">5</rank>
		<year>2026</year>
		<gdppc>59900</gdppc>
		<neighbor direction="N" name="Malaysia" />
	</country>
	<country name="Panama">
		<rank updated="yes">69</rank>
		<year>2026</year>
		<gdppc>13600</gdppc>
		<neighbor direction="E" name="Colombia" />
	</country>
</data> 
"""  
  
root = ET.XML(content)  
print(root)
```
读取根节点名称之后,还需要获得节点内的数据

**2. 读取节点数据**
```python
from xml.etree import ElementTree as ET  
  
content = """  
<data>
	<country name="Liechtenstein">
		<rank updated="yes">2</rank>
		<year>2023</year>
		<gdppc>141100</gdppc>
		<neighbor direction="E" name="Australia" />
	</country>
	<country name="Singapore">
		<rank updated="yes">5</rank>
		<year>2026</year>
		<gdppc>59900</gdppc>
		<neighbor direction="N" name="Malaysia" />
	</country>
	<country name="Panama">
		<rank updated="yes">69</rank>
		<year>2026</year>
		<gdppc>13600</gdppc>
		<neighbor direction="E" name="Colombia" />
	</country>
</data>
"""  
  
root = ET.XML(content)

# 获得第一个country标签  
country_object = root.find("country")  
print(country_object.tag, country_object.attrib)  
# 获得gdppc节点的标签，数据 和 内容  
gdppc_object = country_object.find("gdppc")  
print(gdppc_object.tag, gdppc_object.attrib, gdppc_object.text)
```
这是简单的读取第一个根节点下的子节点,然后读子节点下的第一个节点,以及节点的内容

接下来是输出所有的节点内容,这里我们使用了for循环
```python
from xml.etree import ElementTree as ET  
  
content = """  
<data>
	<country name="Liechtenstein">
		<rank updated="yes">2</rank>
		<year>2023</year>
		<gdppc>141100</gdppc>
		<neighbor direction="E" name="Australia" />
	</country>
	<country name="Singapore">
		<rank updated="yes">5</rank>
		<year>2026</year>
		<gdppc>59900</gdppc>
		<neighbor direction="N" name="Malaysia" />
	</country>
	<country name="Panama">
		<rank updated="yes">69</rank>
		<year>2026</year>
		<gdppc>13600</gdppc>
		<neighbor direction="E" name="Colombia" />
	</country>
</data>
"""  
  
root = ET.XML(content)  
# 获取了根标签,data  
# 获得子标签  
for child in root:  
    print(child.tag, child.attrib)  
    # child.tag = country 获得root标签下的两个子标签  
    # child.attrib = {} 生成一个字典，获得标签的所有属性  
    # 同理node获得的是child下属子标签  
    for node in child:  
        print(node.tag, node.attrib, node.text)
```

接下来是读iter,就是找包含有字符串的标签
```python
from xml.etree import ElementTree as ET  
  
content = """  
<data>
	<country name="Liechtenstein">
		<rank updated="yes">2</rank>
		<year>2023</year>
		<gdppc>141100</gdppc>
		<neighbor direction="E" name="Australia" />
	</country>
	<country name="Singapore">
		<rank updated="yes">5</rank>
		<year>2026</year>
		<gdppc>59900</gdppc>
		<neighbor direction="N" name="Malaysia" />
	</country>
	<country name="Panama">
		<rank updated="yes">69</rank>
		<year>2026</year>
		<gdppc>13600</gdppc>
		<neighbor direction="E" name="Colombia" />
	</country>
</data>
"""  

root = ET.XML(content)  

for child in root.iter('year'):
	print(child.tag, child.text)
```
这样就可以找出所有包含有year的标签

```python
from xml.etree import ElementTree as ET  
  
content = """  
<data>
	<country name="Liechtenstein">
		<rank updated="yes">2</rank>
		<year>2023</year>
		<gdppc>141100</gdppc>
		<neighbor direction="E" name="Australia" />
	</country>
	<country name="Singapore">
		<rank updated="yes">5</rank>
		<year>2026</year>
		<gdppc>59900</gdppc>
		<neighbor direction="N" name="Malaysia" />
	</country>
	<country name="Panama">
		<rank updated="yes">69</rank>
		<year>2026</year>
		<gdppc>13600</gdppc>
		<neighbor direction="E" name="Colombia" />
	</country>
</data>
""" 

root = ET.XML(content)  
v1 = root.findall('country')
print(v1)

v2 = root.findall('country').find('rank')
print(v2)
```

**3. 修改和删除标签**
```python
from xml.etree import ElementTree as ET  
  
content = """  
<data>
	<country name="Liechtenstein">
		<rank updated="yes">2</rank>
		<year>2023</year>
		<gdppc>141100</gdppc>
		<neighbor direction="E" name="Australia" />
	</country>
	<country name="Singapore">
		<rank updated="yes">5</rank>
		<year>2026</year>
		<gdppc>59900</gdppc>
		<neighbor direction="N" name="Malaysia" />
	</country>
	<country name="Panama">
		<rank updated="yes">69</rank>
		<year>2026</year>
		<gdppc>13600</gdppc>
		<neighbor direction="E" name="Colombia" />
	</country>
</data>
"""
root = ET.XML(content)  
  
# 修改节点内容和属性  
rank = root.find('country').find('rank')  
rank.text = "999"  
# 需要赋值为字符串不能是整型  
rank.set('update', '2023-07-12')  
# rank上添加一个属性 update 2023-07-12print(rank.text, rank.attrib)  
# 现在只在内存中储存有数据  
  
# 删除节点  
root.remove(root.find("country"))  
# 删除掉country标签，只剩下1个标签  
print(root.findall("country"))  
  
# 保存文件  
tree = ET.ElementTree(root)  
tree.write('newnew.xml', encoding='utf-8')
```

**4. 构建文档**
从0开始构建一个xml格式的数据
有几种方法可以形成
```python
from xml.etree import ElementTree as ET  
  
# 创建根标签  
root = ET.Element("home")  
  
# 创建第一层子标签  
son_1 = ET.Element("son", {"name": "son1"})  
# 创建第一层第二个子标签  
son_2 = ET.Element("son", {"name": "son2"})  
  
# 创建第二层子标签位于第一层第一个子标签下  
grandson_1 = ET.Element("grandson", {"name": "grandson1"})  
grandson_2 = ET.Element("grandson", {"name": "grandson2"})  
son_1.append(grandson_1)  
son_2.append(grandson_2)  
  
# 将第一层子标签添加到root标签下  
root.append(son_1)  
root.append(son_2)  
  
tree = ET.ElementTree(root)  
tree.write("file/oooo.xml", encoding="utf-8", short_empty_elements=False)  
# 写入到指定的文档中 这里直接生成了一行数据，而不是我们容易读的多行数据  
# short_empty_elements = False 代表是否使用短标签  
# 中间没有值的标签写法和长标签不一样，短标签可以没有结尾的部分  
# 例如<grandson name="grandson1" /> 这样写就可以  
# 如果是长标签写法就是 <grandson name="grandson1">name对应的值</grandson>
```

另一种方式makeelement方法
这个makeelement必须是跟某一层的子标签相关联的创建,但是创建出来却没有关联信息,需要后边添加
```python
from xml.etree import ElementTree as ET  
  
# 创建根节点  
root = ET.Element("family")  
  
# 创建子标签 刚创建的时候跟root没关系  
son_1 = root.makeelement("son", {"name": "son1"})  
son_2 = root.makeelement("son", {"name": "son2"})  
  
# 第一个子标签下子标签 刚创建的时候跟son标签没关系  
grandson_1 = root.makeelement("grandson", {"name": "grandson1"})  
grandson_2 = root.makeelement("grandson", {"name": "grandson2"})  
  
# 第二层子节点添加到第一层中  
son_1.append(grandson_1)  
son_1.append(grandson_2)  
  
# 子标签添加到根节点  
root.append(son_1)  
root.append(son_2)  
  
tree = ET.ElementTree(root)  
tree.write("ooooo.xml", encoding="utf-8")
```

另一种方法
使用SubElement方法创建, 这个可以直接创建子标签和母标签相连
```python
from xml.etree import ElementTree as ET  
# 创建根节点  
root = ET.Element("family")  
  
# 创建子标签  
son_1 = ET.SubElement(root, "son", attrib={"name": "son1"})  
son_2 = ET.SubElement(root, "son", attrib={"name": "son2"})  
  
# 子标签继续向下层创建  
grandson_1 = ET.SubElement(son_1, "age", attrib={"name": "grandson1"})  
grandson_1.text = "grandson"  
  
et = ET.ElementTree(root) # 生成文档对象  
et.write("test.xml", encoding="utf-8")
```

最后一种方式
腾讯的xml格式不一样
![[Pasted image 20230712154007.png]]
这里使用了把值包裹起来的写法
最基础简单的方式
```python
from xml.etree import ElementTree as ET  
# 创建根节点  
root = ET.Element("user")  
root.text = "<![CDATA[nihao]]"  
# 直接写一个值进去  
  
et = ET.ElementTree(root)  
et.write("test.xml", encoding="utf-8")
```

**案例**
从微信获得了一个xml的数据
```xml
<xml>
	<ToUserName><![CDATA[toUser]]></ToUserName>
	<FromUserName><![CDATA[fromUser]]></FromUserName>
	<CreateTime>1348831860</CreateTime>
	<MsgType><![CDATA[text]]></MsgType>
	<Content><![CDATA[你好]]></Content>
	<MsgId>1234567890123456</MsgId>
</xml>
```

```python
from xml.etree import ElementTree as ET  
  
info = {}  
root = ET.XML(content)  
for node in root:  
    print(node.tag, node.text)  
    info[node.tag] = node.text  
  
print(info)
```
这种应用场景很少
