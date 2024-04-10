# HTML区块元素

大多数HTML元素被定义为**块级元素** 或者 **内联元素**
块级元素在浏览器显示的时候，通常会以新行来开始（和结束）

实例 `<h1> <p> <ul> <table>`

# HTML内联元素
内联元素在显示的时候不会以新行开始
实例 `<b> <td> <a> <img>` 
b就是加粗
```html
<li><b>costa</b></li>
```
这个也不会出现换行效果

# HTML div 元素

HTML div 元素是块级元素，可以用于组合其他HTML元素的容器
div没有特定的含义，如果和css一起使用，div元素可以用于对大的内容块设置样式属性
![[Pasted image 20231113131146.png]]
div元素的另一个常见用途是文档布局，取代了使用表格定义布局的老式方法，使用table元素进行文档布局不是表格的正确用法

![[Pasted image 20231113131400.png]]
这里页面布局就是一块一块的，常见HTML来说就是从上到下来写网页内容，显示也是从上到下显示
而我们见到过的网页都是分很多块的，其中每一块都可以对其设置不同的样式属性来进行设计排版

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
<div style="border:1px dashed #00a2ca;width: 500px;margin-bottom: 100px;position: relative;left: 600px">  
    <ol>        <li>Coffee</li>  
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
# span元素

html span元素是内联元素，可以用作文本的容器
span元素也没有特定的含义，当和css一同使用的时候，span元素可以用于为部分文本设置样式属性

比如我在div这个包裹的内容中，我想要在其中一部分文本设置颜色，那就需要span元素来改变样式

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
<div style="border:1px dashed #00a2ca;width: 500px;margin-bottom: 100px;position: relative;left: 600px">  
    <ol>        <li>Cof<span style="color:red">fee</span></li>  
        <li>Tea</li>  
        <li>Milk</li>  
    </ol>  
    <ol start="50">  
        <li>Coffee</li>  
        <li>Tea</li>  
        <li>Milk</li>  
    </ol></div>  
  
</body>  
</html>
```