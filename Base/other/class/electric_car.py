# 继承
'''
导入多个模块：import car
导入模块所有类：from module_name import *
'''
from car import Car
from battery import Battery

class ElectricCar(Car):
    "电动汽车"
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        '''初始化自身属性'''
        self.battery_size = 70
        # 类作为实例
        self.battery = Battery()

    def describe_battery(self):
        '''打印一条电瓶描述信息'''
        print("This is has a " + str(self.battery_size)+ " -kwh battery")

    def fill_gas_tank(self):
        # 重新父类方法
        print("This Car doesn't need a gas tank")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 类实例调用类属性
my_tesla.battery.describe_battery()

# 类实例调用类属性的方法
my_tesla.battery.get_range()