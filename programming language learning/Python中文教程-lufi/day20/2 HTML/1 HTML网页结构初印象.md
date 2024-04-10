
HTML简介
HTML网页结构

## 什么是HTML

HTML是用来描述网页的一种语言

- HTML指的是超文本标记语言：HyperText Markup Language
- HTML不是一种编程语言，而是一种标记语言
标记语言没有逻辑，数据类型这些东西，只是用来描述内容的，像是文本是否加粗，或者是几级标题等等
- HTML标记语言是一套**标记标签markup tag**
- HTML用标记标签来**描述**网页
- HTML文档包含了HTML**标签**以及**文本**内容
- HTML文档也叫**web页面**


### HTML标签

需要有开始声明和结束声明
也需要有head和body的部分，页面上看到的内容只是body的内容
head的作用是写标签页的标题的，还定义了页面的字符集，字符编码，还有搜索引擎可以搜索到的关键词

运营中有seo和sem，searching engine marketing 谷歌或者百度排名
searching engine optimization 搜索引擎优化
如何做到seo就是使用header的部分
搜索引擎再用爬虫爬到标题的时候，就会搜索到header中的关键字，然后进行显示

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset='utf-8'>
		<title>路飞学城</title>
	</head>
	<body>

		<h1>我的第一个标题</h1>
		<p>我的第一个段落</p>
	</body>
</html>
```

- <!DOCTYPE html>h5声明为HTML5文档
- `<html> `元素是HTML页面的根元素
- `<head>`标签用于定义文档的头部，是所有头部元素的容器，head中的元素可以引用脚本，指示浏览器在哪里找到样式表，提供元信息等等
- `<meta>`元素包含文档的元数据，如定义网页编码格式为utf-8，关键词等等
- `<title>` 元素里描述了文档的标题
- `<body>` 元素里包含了可见的页面内容
- `<h1>`定义了一个大标题
- `<p>`定义了一个段落

注：在浏览器的页面上使用F12可以开启调试模式，可以看到组成标签


```html
<html>
	<head>
		<title> 页面标题 </title>
	</head>
	<body>
		<h1>这是一个标题</h1>
		<p>这是一个段落</p>
		<p>这是另一个段落</p>
	</body>
</html>
```
通过尖括号包裹文本，只是用来标记文本的语言

