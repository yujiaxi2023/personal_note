```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>小米官网</title>  
    <style type="text/css">  
        #menu {  
            background-color: yellow;  
            height: 80px;  
        }/*前边加#就是用id来选择元素标签*/  
        #sidebar {  
            height: 500px;  
            width: 20%;  
            background-color: orange;  
            float: left;  
        }  
        #content_box {  
            height: 800px;  
            width: 80%; /*必须要是加起来100才能够在一行排列*/  
            background-color: greenyellow;  
            float: left;  
        } /*css里的float属性 可以设置从左往右排列*/  
        #sub_content_box{  
            background-color: navajowhite;  
            height: 90%;  
            width: 30%;  
            float: right;  
        }  
        #footer {  
            background-color: black;  
            height: 100px;  
            clear: both;  
        } /*clear是清除前边的排列规则*/  
    </style>  
</head>  
<body>  
    <div id="menu">  
        <p>HOMEPAGE</p>  
        <p>TELEVISION</p>  
    </div>  
    <div id="sidebar">  
        <ul>            <li>phone</li>  
            <li>tv</li>  
            <li>IOT</li>  
        </ul>    </div>    <div id="content_box">  
        <h2>ad</h2>  
        <div id="sub_content_box">  
            <p>sb</p>  
        </div>    </div>    <div id="footer">  
        <h3>footer...</h3>  
    </div></body>  
</html>
```

- `#`可以指定div的id
- float代表设置浮动属性，可以设置排列方式，但是需要注意的是加起来不可以超过100%，不然会自动换行

