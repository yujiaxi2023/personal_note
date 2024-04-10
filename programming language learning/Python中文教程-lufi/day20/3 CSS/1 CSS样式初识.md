CSS（Cascading style sheets）用于渲染HTML元素标签的样式

CSS可以通过以下方式添加到HTML中：
- 内联样式，说白了直接在元素里面写，这样用的很少，因为这样就写的比较死，并不好 - 在HTML元素中使用‘style’属性
- 内部样式表- 在HTML文档头部`<head>`区域使用`<style>`元素来包含CSS
- 外部引用-使用CSS文件

- 内部样式表
在head中间写一个style
如果给body加样式表，就直接body后边写一个描述，属性和值对应

CSS的规则主要是由两个主要部分构成：选择器，和一条或者多条声明：
![[Pasted image 20231121212551.png]]
```html
<head>
	<style type="text/css">
		body {background-color:yellow;}
		p {color:blue;}
	</style>
<head>
```
这种就叫内部样式表

这是一个示例
```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
  
    <style type="text/css">   
div {  
            border: 1px dashed red;  
            width: 500px;  
            margin-bottom: 50px;  
            position: relative;  
            left: 600px;  
        }  
    </style>  
  
</head>  
<body>  
<div>  
    <ol>        <li>Cof<span style="color:red">fee</span></li>  
        <li>Tea</li>  
        <li>Milk</li>  
    </ol>  
    <ol start="50">  
        <li>Coffee</li>  
        <li>Tea</li>  
        <li>Milk</li>  
    </ol></div>  
<ul>  
    <li>Coffee</li>  
    <ul>        <li>Starbucks</li>  
        <ol>            <li>latte</li>  
        </ol>        <li>Costa</li>  
    </ul>    <li>Tea</li>  
    <li>Milk</li>  
</ul>  
  
</body>  
</html>
```


- 外部样式表
创建一个css文件
把样式写进文件里面
```css
div {  
    border: 1px dashed red;  
    width: 500px;  
    margin-bottom: 50px;  
    position: relative;  
    left: 600px;  
}  
p {  
    background-color: yellow;  
    font-size: 18px;  
    font-family: "fangsong";  
}
```
着用就可以通过一个css文件控制多个html文件