- background 背景属性
- Border边框 和 轮廓Outline属性
- 内边距padding属性
- margin属性
- position定位属性
- 字体font属性
- 文本text属性

[CSS 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-tutorial.html)

常见的css指令查询


## background 背景属性

- background是复合属性，可以输入多个内容
```html
body
{
 background: #00ff00 url('similey.gif') no-repeat fixed center;
}
```
- background-color
- background-image
- background-position
- background-repeat
- background-size
- background-clip  指定图像向外裁剪的区域
- background-origin s设置或者检索背景图计算background-position的时候的参考原点（位置）

## border和outline
- border也是一样的复合属性，设置对象的样式
还有很多属性可以调整

border还可以设置虚线外框，阴影等等内容

## 定位position

有点像excel中间的冻结窗格

有几个属性
- absolute
- fixed
- relative
- static
- sticky
- inherit

### fixed
生成固定定位的元素，相对于浏览器窗口进行定位，元素的位置通过left top right以及bottom属性进行规定

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
  
    <style type="text/css">  
        #box_1 {  
            border: 10px solid black;  
            width: 500px;  
            height: 500px;  
            padding: 50px; /*这个时候会发现box整体大了*/  
            /*这时候我们可以打开审查元素。可以看到可视化的盒子模型，设置的时候生成的是内容的长宽，设置padding是在content外设置的*/  
            margin: 50px; /*四面都是多了50px*/  
  
            position: fixed; /*相对浏览器的定位，确定定位的模式*/  
            top: 50px;  
            left: 50px;  
        }  
        #box_2 {  
            border: 10px solid blue;  
            width: 500px;  
            height: 500px;  
        }  
    </style>  
</head>  
<body>  
  
<div id="box_1">  
  
    <p>hello</p>  
  
</div>  
  
<div id="box_2">  
  
</div>  
  
</body>  
</html>
```

相对浏览器的左边50，上边50
跟margin很类似，但是margin类似于是将box的边距变大了，依然是贴在浏览器的边缘的
这里position fixed就是实在的把位置移动了

如果做了定位之后就等于把这个元素放在一个新的图层中了
就跟ps一样，这两个图层互相没有关系，所以box1和box2都是相对于它们所在的图层进行定位的

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
  
    <style type="text/css">  
        #box_1 {  
            border: 10px solid black;  
            width: 500px;  
            height: 500px;  
            padding: 50px; /*这个时候会发现box整体大了*/  
            /*这时候我们可以打开审查元素。可以看到可视化的盒子模型，设置的时候生成的是内容的长宽，设置padding是在content外设置的*/  
            margin: 50px; /*四面都是多了50px*/  
  
            position: fixed; /*相对浏览器的定位，确定定位的模式*/  
            top: 50px;  
            left: 50px;  
        }  
        #box_2 {  
            border: 10px solid blue;  
            width: 500px;  
            height: 500px;  
        }  
        #box_3 {  
            border: 10px solid rebeccapurple;  
            width: 500px;  
            height: 1500px;  
        }  
    </style>  
</head>  
<body>  
  
<div id="box_1">  
  
    <p>hello</p>  
  
</div>  
  
<div id="box_2">  
  
</div>  
  
<div id="box_3">  
  
</div>  
  
</body>  
</html>
```
这样写可以让黑色方框永远固定在浏览器的固定位置不会因为滑窗进行移动


### relative
相对定位
```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
  
    <style type="text/css">  
        #box_1 {  
            border: 10px solid black;  
            width: 500px;  
            height: 500px;  
            padding: 50px; /*这个时候会发现box整体大了*/  
            /*这时候我们可以打开审查元素。可以看到可视化的盒子模型，设置的时候生成的是内容的长宽，设置padding是在content外设置的*/  
            margin: 50px; /*四面都是多了50px*/  
  
            position: fixed; /*相对浏览器的定位，确定定位的模式*/  
            top: 50px;  
            left: 50px;  
        }  
        #box_2 {  
            border: 10px solid blue;  
            width: 500px;  
            height: 500px;  
        }  
        #box_3 {  
            border: 10px solid rebeccapurple;  
            width: 500px;  
            height: 1500px;  
        }  
        #box_1 p {  
            color: red;  
            position: relative;  
            left: 100px;  
        }  
    </style>  
</head>  
<body>  
  
<div id="box_1">  
  
    <p>hello</p>  
  
</div>  
  
<div id="box_2">  
  
</div>  
  
<div id="box_3">  
  
</div>  
  
</body>  
</html>
```
如果我们想要对一个元素进行移动，有几种可能性，
- 相对于浏览器的边界移动
- 相对于border进行移动
- 相对于当前位置移动

***使用了relative的情况是相对于自己原来的位置进行了移动***

### static
默认值，代表没有定位，如果使用了static，就会把所有的bottom等等的东西都忽略掉，所有的东西position都是默认用这个定位


## text
- color
- text-decoration 装饰加线等等
很多的方法都可以去官网进行尝试，并且渲染

## font
- font 是一个声明，可以添加所有字体属性
- font-family 字体系列
- font-size 大小
- font-style 斜体等

