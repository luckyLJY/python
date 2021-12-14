#  将Battery类作为ElectricCar的实例

class Battery():
    '''电动汽车'''
    def __init__(self,battery_size = 70):
        # 初始化电瓶属性
        self.battery_size = battery_size

    def describe_battery(self):
        # 打印电瓶容量信息
        print("This car hs a "+ str(self.battery_size)+'-KWH battery')

    def get_range(self):
        # 打印电瓶续航里程
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)