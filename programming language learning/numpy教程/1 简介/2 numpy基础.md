# numpy基础
## ndarray数组

用np.ndarray类的对象保存n维度数组
```python
import numpy as np
ary = np.array([1,2,3,4,5,6])
print(type(ary))
```

# 内存中的numpy
## 元数据（metadata）
储存对目标数组的描述信息，如：dim count，dimensions，dtype，data等等
![[Pasted image 20230822161431.png]]
假如创建了一个数据是右边的样子
这个时候，实际数据是按照这个顺序进行存储的
这里面元数据的样子是这样的
如果我需要修改元数据中的各种信息
例如将shape进行转换，我就可以进行直接修改shape，然后他就会根据实际data的顺序自动的进行替换
![[Pasted image 20230822161607.png]]
元数据就是代表是一种读取方式

dtype代表的是数组中的每个元素是32个二进制表示一个整数
这样就不会变数据类型，除非变为long类型数据，但是long也会最开始存储为64位代表一个数
## 实际数据
寻址操作比较耗时
![[Pasted image 20230822162323.png]]
在普通的数据储存中是这样的

如果是在ndarray中储存是
![[Pasted image 20230822162353.png]]
这样一种很整齐的储存方式

如果使用python原生代码中的for循环，遍历list中的数据
这样就涉及到一个寻址操作，首先是根据下表找到这个数据所在的内存位置，然后进行寻址操作找到存储位置读取数据

将实际数据和元数据分开存放，提高了内存空间的使用效率，减少对实际数据的访问频率提高性能

# ndarray数组对象的特点
1. numpy数组是通知数组，所有元素的数据类型必须相同
2. numpy数组的下标从0开始，最后1个元素的下标位数组长度-1

# ndarray数组对象的创建
np.array（任何可被解释为numpy数组的逻辑结构）
```python
import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
```

np.arange(起始值(0)，终止值，步长(1))
```python
import numpy as np
a = np.arange(0,5,1)
print(a)
b = np.arange(0,10,2)
print(b)
```

np.zeros(数组元素个数，dtype = ‘类型’)
```python
import numpy as np
a = np.zeros(10)
print(a)

b = np.zeros_like(a)
print(b) # 像a的shape的zeros
```

np.ones(数组元素个数，dtype=‘类型‘)
```python
import numpy as np
a = np.ones((2,3), dtype='float32')
print(a, a.shape, a.dtype)

b = np.ones(5) / 5
print(b)
```

