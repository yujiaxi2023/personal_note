# 什么是celery

celery是一个简单灵活可靠的，处理大量消息的分布式系统，专注于实时处理的异步任务队列，同时也支持任务调度

#### 分布式系统
将系统组件架构在不同组件，然后将不同的服务器通信来组成一个大的系统叫做分布式系统
避免单点故障，负载平衡的优点

异步任务
就是执行IO操作的时候，这时候CPU转换到别的任务运行，IO操作结束后将返回值储存到数据库中，等到需要调用的时候进行调用即可

![[Pasted image 20240214193421.png]]
celery就是需要将分布式系统进行异步任务的一个工具

### celery的架构

三部分组成：消息中间件（message broker），任务执行单元（worker）和任务执行结果储存（task result store）

#### 消息中间件

celery不提供消息服务，但是可以方便的和第三方提供的消息中间件继承，包括RabbitMQ，Redis等等

#### 任务执行单元

Worker是Celery提供的任务执行单元，worker并发的运行在分布式的系统节点中

#### 任务结果储存

Task result store用来储存Worker执行的任务的结果，Celery支持以不同的方式储存任务的结果，包括AMQP，redis等

另外Celery还支持不同的并发和序列化的手段
- 并发：Prefork，Eventlet，gevent，threads/single threaded
- 序列化：pickle，json，yaml，msgpack，zlib，bzip2，Cryptographic message signing等等

一定要学习RabbitMQ和Reddis之后才能真正理解Celery

