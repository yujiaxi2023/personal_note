id/class选择器
元素名选择器
组合选择器
盒子模型
常用CSS属性

## id选择器

id就类似一个元素的身份证地址，可以在网页里面，**唯一代表某个元素**，我们可以通过这个id快速的找到它对应的元素对象
```html
<head>
	<meta charset="UTF-8">
	<title>CSS样式</title>

	<style type="text/css">
	/*直接#加标签的名字*/
		#css_test {
			background: deepskyblue;
			font-family: "Arial Black";
			color: red;
		}
	</style>
</head>
<body>
	<form action="baidu_url">
		姓名：<input id="css_test" type="text" name="name"><br>
		电话：<input type="number" name="phone"><br>
		性别：<input type="radio" name="sex" value="man">男 <input type="radio" name="sex" value="woman">女
		爱好：<input type="checkbox" name="hobby" value="girl">姑娘
```

如果想要重复id的话就会覆盖掉，但是两个id一样的就会都产生作用
浏览器解释不严谨的地方也有，css可以找到多个进行解释，但是到了后边的gs就会出问题

## class选择器

可以同时让所有标记class的同时变样式
想要给谁加样式就给谁加class
需要声明一个类来加样式
```html
<head>
	<meta charset="UTF-8">
	<title>CSS样式</title>

	<style type="text/css">
	/*直接#加标签的名字*/
		#css_test {
			background: deepskyblue;
			font-family: "Arial Black";
			color: red;
		}
		.class_test { /*类选择器*/
			background-color: orange;
			border: 2px dashed blueviolet;
		}
	</style>
</head>
<body>
	<form action="baidu_url">
		姓名：<input id="css_test" type="text" name="name"><br>
		电话：<input type="number" name="phone"><br>
		性别：<input class="class_test" type="radio" name="sex" value="man">男 <input type="radio" name="sex" value="woman">女
		爱好：<input type="checkbox" name="hobby" value="girl">姑娘
```


## 元素选择器
```html
<head>
	<meta charset="UTF-8">
	<title>CSS样式</title>

	<style type="text/css">
	/*直接#加标签的名字*/
		#css_test {
			background: deepskyblue;
			font-family: "Arial Black";
			color: red;
		}
		.class_test { /*类选择器*/
			background-color: orange;
			border: 2px dashed blueviolet;
		}
		input {
			background-color: blue;
		}
		/*这里需要考虑优先级的问题*/
	</style>
</head>
<body>
	<form action="baidu_url">
		姓名：<input id="css_test" type="text" name="name"><br>
		电话：<input type="number" name="phone"><br>
		性别：<input class="class_test" type="radio" name="sex" value="man">男 <input type="radio" name="sex" value="woman">女
		爱好：<input type="checkbox" name="hobby" value="girl">姑娘
```
- input是给所有的input标签加样式
- id&class的选择器的优先级大于元素名选择器