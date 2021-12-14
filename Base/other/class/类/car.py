class Car():
    """模拟汽车"""

    def __init__(self,make,model,year):
        '''初始化汽车属性值'''
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("This car has " +str(self.odometer_reading) +" miles on it")

    def update_odometer(self,mileage):
        """通过方法修改指定属性值
            限制属性值往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This Car has gas tank")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

# 直接修改属性值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 方法修改属性值
my_new_car.update_odometer(34)
my_new_car.read_odometer()

# 使用方法增加里程属性
my_new_car.increment_odometer(10)
my_new_car.read_odometer()