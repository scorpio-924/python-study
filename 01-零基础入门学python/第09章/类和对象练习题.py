class Phone:
    def __init__(self,model,price):
        self.model = model
        self.price = price

    def describe(self):
        return f"这是{self.model}手机，价格是{self.price}元"

    def call_friend(self,friend_name):
        print(f"我在用手机{self.model}打电话给{friend_name}")

iphone13 = Phone("iphone13",6000)
huaweip50 = Phone("huaweip50",4000)

print(iphone13.describe())
iphone13.call_friend("xiaoming")

print(huaweip50.describe())
huaweip50.call_friend("xiaozhang")

