class User:
    def __init__(self,name,password):
        self.name = name
        self.password =password
    def welcome(self):
        print(f"你好{self.name}欢迎到来")

class Admin(User):
    def __init__(self,name,password):
        super().__init__(name,password)

    def welcome(self):
        print(f"你好尊贵的Admin管理员{self.name}，欢迎归来")

    def manager(self):
        print("我在管理系统")


class Vip(User):
    def __init__(self,name,password,money):
        super().__init__(name,password)
        self.money = money
    def welcome(self):
        print(f"你好尊贵的Vip用户{self.name}，欢迎归来")

    def vip_service(self):
        print("你好给你提供会员服务")


admin01 = Admin("admin01",1234)
admin02 = Admin("admin02",2345)
vip01 = Vip("vip01",1234,1000)
vip02 = Vip("vip02",1244,2000)
user01 = User("user01",1234)
user02 = User("user02",1245)

admin01.welcome()
admin01.manager()
admin02.welcome()
admin02.manager()

vip01.welcome()
vip01.vip_service()
vip02.welcome()
vip02.vip_service()

user01.welcome()
user02.welcome()
