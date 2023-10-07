# 父类
class Car:
	def __init__(self,model,price):
		self.model = model
		self.price = price

	def info(self):
		print(f"车型是{self.model}价格是{self.price}万元")


class OilCar(Car):     # 用括号的方式，指定继承的父类
	def __init__(self,model,price,box_size):
		super().__init__(model,price)    # super()代表父类对象，父类也需要初始化
		self.box_size = box_size

	def add_oil(self,money):
		print(f"老板，加{money}元的汽油")

	def info(self):   #  子类可以直接调用父类的方法，也可以覆盖方法，只要名字和参数一样
		super().info()
		print("我是油车，跑起来比电动车动力更足")


class ElectricCar(Car):
	def __init__(self,model,price,battery_size):
		super().__init__(model,price)
		self.battery_size = battery_size

	def add_electric(self,money):
		print(f"车值{self.price}万元，充电花了{money}元")
		# 子类代码或者对象中是可以直接使用父类方法和属性的

ocar01 = OilCar("路虎",60,50)
print(ocar01.model,ocar01.price,ocar01.box_size)
ocar01.info()
ocar01.add_oil(200)

ecar01 = ElectricCar("特斯拉",100,200)
print(ecar01.model,ecar01.price,ecar01.battery_size)
ecar01.info()
ecar01.add_electric(200)