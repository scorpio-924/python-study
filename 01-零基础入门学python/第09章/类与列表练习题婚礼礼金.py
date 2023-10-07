"""* 婚礼接收彩礼程序
* 朋友结婚，你在门口帮忙收彩礼，需要记录来人的姓名和礼金

1. 新建一个类叫Customer，访客的姓名name和礼金money
2. 编写一个while True
	1. 输入“小明 1000”意思是小明给了1000的礼金，用这个数据构造对象
	2. 将对象放到customers这个列表里
	3. 如果输入quit就退出，退出之前遍历列表，计算打印信息：
		1. 访客总人数
		2. 访客礼金总金额、最大金额、最小金额、平均金额
		"""

class Customer:
    def __init__(self,name,money):
        self.name = name
        self.money = money
customers = []

while True:
    print("#"*20)
    info = input("请输入来人姓名和金额")
    if info == ("quit"):
        break

    name, money = info.split()
    money = int(money)
    customer = Customer(name,money)
    customers.append(customer)
print("访客总人数：",len(customers))
moneys = [i.money for i in customers]
print("总金额：",sum(moneys))
print("最大金额：",max(moneys))
print("最小金额：",min(moneys))
print("平均金额：",sum(moneys)/len(moneys))
