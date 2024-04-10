
# HTML常用元素入门

- HTML标题
- HTML段落
- 超链接
- 显示图片
- HTML表格
- 列表
- Div区块元素


## HTML标题

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
<h1>this is title1</h1>  
<h2>this is title2</h2>  
<h3>this is title3</h3>  
<h4>this is title4</h4>  
<h5>this is title5</h5>  
<h6>this is title6</h6>  
  
</body>  
</html>
```
![[Pasted image 20231122154044.png]]
## HTML段落

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
  <p>this is a paragraph</p>  
  <p>this is a paragraph</p>  
  <p>this is a paragraph</p>  
  
</body>  
</html>
```
这里p结束的时候就换一行，理解为这里包含一个换行符
![[Pasted image 20231122154055.png]]

## 超链接

当前页面跳转超链接
```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
  <a href="https://www.luffycity.com/play/61618">这是一个链接使用了href属性</a>  
  
</body>  
</html>
```
![[Pasted image 20231122154110.png]]

想打开一个新页面
```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
  <a href="https://www.luffycity.com/play/61618" target="_blank">这是一个链接使用了href属性</a>  
  
</body>  
</html>
```
注意a标签结束不会直接换行

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
    <a href="https://www.luffycity.com/play/61618">这是一个链接使用了href属性</a>  
    <br>  
</body>  
</html>  
  
  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
    <a href="https://www.luffycity.com/play/61618" target="_blank">这是一个链接使用了href属性</a>  
    <br>  
</body>  
</html>
```
需要换行就需要加br

## 显示图片

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
<img src="earthquake.jpg" width="1920" height="1274">  
  
</body>  
</html>
```
图片也是不会自己换行的

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
<img src="earthquake.jpg" width="1920" height="600">  
  
</body>  
</html>
```
如果设定和原比例不一样就会压缩

## HTML表格

想在HTML中做表格

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
  <table border="1">  
    <tr>        <td>row 1, cell 1</td>  
        <td>row 1, cell 2</td>  
    </tr>    <tr>        <td>row2, cell 1</td>  
        <td>row2, cell 2</td>  
    </tr>  
    </table>  
</body>  
</html>
```
这里的border代表1像素宽的边框
td就是table data
这个表格没有表头

### 表格的表头

表格的表头使用th标签进行定义
table head
```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
  <table border="1">  
    <tr>        <th>姓名</th>  
        <th>age</th>  
        <th>address</th>  
    </tr>    <tr>        <td>row 1, cell 1</td>  
        <td>row 1, cell 2</td>  
    </tr>    <tr>        <td>row2, cell 1</td>  
        <td>row2, cell 2</td>  
    </tr>  </table>  
</body>  
</html>
```

还可以加边距
```html
<table border="1" cellpadding="10">
```
cellpadding就是设置边距为10pixel


## 列表

分为有序列表和无序列表

### 有序列表

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
  <ol>    
	<li>Coffee</li>  
    <li>Tea</li>  
    <li>Milk</li>  
  </ol>  
  <ol start="50">  
    <li>Coffee</li>  
    <li>Tea</li>  
    <li>Milk</li>  
  </ol>  
</body>  
</html>
```
ol就是ordered list，在ol中包裹的就是按照顺序进行

start就是指定开始的位置

### 无序列表

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>   
  <ul>    
	<li>Coffee</li>  
    <li>Tea</li>  
    <li>Milk</li>  
  </ul>  
</body>  
</html>
```
这里可以将这里显示的黑点改为红点或者其他的东西，但是那是css的内容

列表是可以嵌套的

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
<ol>  
    <li>Coffee</li>  
    <li>Tea</li>  
    <li>Milk</li>  
</ol>  
  
<ol start="50">  
    <li>Coffee</li>  
    <li>Tea</li>  
    <li>Milk</li>  
</ol>  
  
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


