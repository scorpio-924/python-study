import animal

class Sheep(animal.Animal):
    def __init__(self,name):
        super().__init__(name)

    def eat_grass(self):
        print("我是羊我在吃草")
