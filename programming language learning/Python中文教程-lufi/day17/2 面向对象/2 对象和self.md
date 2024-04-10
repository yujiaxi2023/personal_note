每个类中都可以定义一个特殊的：`__init__`初始化方法，在实例化类创建对象的时候自动执行，即`对象=类()`
```python
class Message:
	def __init__(self,content):
		self.data = content

	def send_email(self, email):
		data = f"给{email}发邮件，内容是{self.data}"
		print(data)
	def send_wechat(self, vid):
		data = f"给{vid}发微信，内容是{self.data}"
		print(data)

msg_object = Message("successful")
msg_object.send_email("eupeiqi@live.com")
msg_object.send_wechat("吴佩奇")
```
![[Pasted image 20231029222403.png]]

定义的初始化方法，固定写法就是上面代码的第一个函数，然后第一个参数是self，后边的参数是可以随意设置

这个方法是实例化对象的时候自动执行的一个方法
使用 类名()的时候回自动执行__init__方法

self代表当前调用的方法的对象
这里的执行步骤：
- 1 创建一个根据类的对象，一块内存区域，里面默认什么也没有
- 2 执行init方法，默认会将创建的这块区域的内存地址，当做self参数传递进去，所以self代表的是这个方法所在的内存地址，向这个区域data = successful

这里的self代表的是实例化的对象所在的内存地址
所以这里如果用self. 一定会自动出来一个data的，self是代指的message_object,这就跟传进来一个message_object的config文件一样

类实例化的过程就类似于创建一个区域,可以存储数据,并可以调用类中的方法,将数据传入到方法中,

通过上述示例,你会发现:
- 对象,让我们可以在他的内部先封装一部分数据,以后想要使用的时候,再去里面获取
- self,类中的方法需要由这个类的对象来触发并执行(对象,方法名),且在执行的时候会自动将对象当做参数传递给self,以供方法中获取对象中已经封装的值
注意: 除了self默认参数之外,方法中的参数的定义和执行和函数是相同

当然,根据类也可以创建多个对象并执行其中的方法, 例如:
```python
class Message:
	def __init__(self,content):
		self.data = content

	def send_email(self, email):
		data = f"给{email}发邮件，内容是{self.data}"
		print(data)

	def send_wechat(self, vid):
		data = f"给{vid}发微信，内容是{self.data}"
		print(data)

msg_object = Message("register successful")
msg_object.send_email("eupeiqi@live.com")
msg_object.send_wechat("吴佩奇")

login_object = Message("log in successful")
login_object.send_email("eupeiqi@live.com")
login_object.send_wechat("吴佩奇")
```

面向对象的思想，将一些数据封装到对象中，在执行方法的时候，再去对象中获得
函数式的思想，函数内部需要的数据均通过参数的形式进行传递

![[Pasted image 20231029222403.png]]

- self，本质上就是一个参数，这个参数是python内部提供的，本质上是调用当前方法的那个对象，谁调用的这个方法，谁就是这个self的对象，就比如说msg_object调用了send_email方法，当然这个必须是在msg_object实例化之后，那这里self就是msg_object，如果是login_object调用了send_wechat方法，这里self就是login_object
- 对象，基于类实例化出来的一块内存区域，默认里面没有数据，只有经过类的初始化__init__方法，可以在这块内存中初始化一些数据

**什么时候适合用面向对象：**
- 仅仅做数据封装
- 封装数据+方法再对数据进行加工处理
- 根据模板创建同一类的数据，且同类数据可以有相同的功能（方法）

更规范的实现我们的功能
