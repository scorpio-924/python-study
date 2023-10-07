from animal import Animal

class Tiger(Animal):
    def __init__(self,name):
        self.name = name

    def eat_meat(self,parm_animal):
        print(f"我是老虎我在 {parm_animal.name}")