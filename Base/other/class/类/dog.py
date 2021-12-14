# 类的创建
class Dog():
    def __init__(self,name,age):
        """初始化属性值"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟蹲方法"""
        print(self.name.title() + "is now siitting.")

    def roll_over(self):
        '''模拟打滚方法'''
        print(self.name.title() + " rollled over!")


# 创建实例
my_dog = Dog('wolf',6)

# 属性的访问
print("my dog name is:"+ my_dog.name.title()+" age is:"+ str(my_dog.age) +" years lod")

# 方法调用
my_dog.sit()
my_dog.roll_over()