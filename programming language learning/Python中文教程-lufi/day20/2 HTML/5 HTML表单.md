- 文本框
- 文本域
- 下拉列表
- 单选，复选
- 按钮

最简单的一些用法
```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
  
<div>  
    <form action="/test/url/">  
    <!--数据提交到后台，如果有就是提交到这个文件里面，如果没有就404-->  
        User_Name: <input type="text" name="username"> <br> <!--需要指定一个变量名来明确这个input的属性-->  
        Password: <input tyep="password" name="hobby">  
        Age: <input type="number" name="password">  
        Birthday: <input type="date" name="age"> <!--后台取到的文本数据会转换为字典-->  
  
        Personal statement: <br>  
        <textarea cols="50" rows="5" placeholder="请输入不少于50字的个人介绍..."></textarea><br>  
  
        Gender: <input type="radio">man <input type="radio">woman  
  
        <input type="submit" value="注册"><br>  
        <!--提交按钮-->  
  
        爱好：  
        <input type="checkbox" name="hob" value="girl">girl  
        <input type="checkbox" name="hob" value="car">car  
        <input type="checkbox" name="hob" value="coding">coding  
        <input type="checkbox" name="hob" value="smoke">smoke  
  
        <fieldset>  
            <legend>Personality</legend>  
            Name:<input type="text"><br>  
            Email:<input type="text"><br>  
            Date of birth:<input type="text">  
        </fieldset>    </form></div>  
  
</body>  
</html>
```