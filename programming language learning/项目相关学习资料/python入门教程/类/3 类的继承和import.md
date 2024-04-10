使用自定义的类的时候，需要保证在同一文件夹下，不然无法直接使用

```python
from superclass.Animal import Animal  
  
class Dog(Animal):  
    def __init__(self, name, age, type):  
        super().__init__(name, age)  
        self.type = type  
  
    def sit(self):  
        print(self.name.title() + " is now sitting. ")  
  
    def get_character(self):  
        if self.type == 'teddy':  
            print(self.name + ' is cute. ')  
  
    def eat(self, food):  
        forbidden_foods = ['milk', 'chocolate']  
  
        if food in forbidden_foods:  
            print(' Dog can not eat ' + food + '.')  
        else:  
            print(self.name + ' is now eatting ' + food + '.')  
  
  
my_dog = Dog('Hua', 2, 'teddy')  
my_dog.eat('apple')  
my_dog.eat('milk')  
my_dog.eat('chocolate')  
my_dog.get_character()
```

调用方式是写出文件夹名称，然后调用内部的有class 的文件

但是如果是直接使用import导入
```python
import Animal  
  
class Dog(Animal.Animal):  
    def __init__(self, name, age, type):  
        super().__init__(name, age)  
        self.type = type  
  
    def sit(self):  
        print(self.name.title() + " is now sitting. ")  
  
    def get_character(self):  
        if self.type == 'teddy':  
            print(self.name + ' is cute. ')  
  
    def eat(self, food):  
        forbidden_foods = ['milk', 'chocolate']  
  
        if food in forbidden_foods:  
            print(' Dog can not eat ' + food + '.')  
        else:  
            print(self.name + ' is now eatting ' + food + '.')  
  
  
my_dog = Dog('Hua', 2, 'teddy')  
my_dog.eat('apple')  
my_dog.eat('milk')  
my_dog.eat('chocolate')  
my_dog.get_character()
```

我们就需要在这个class中指定class才能调用的准确

在todo的时候def的函数可以直接写pass就不会报错

