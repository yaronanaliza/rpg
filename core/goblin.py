from core.orc import *
class Goblin(Monster):
    def __init__(self, name, hp, type, speed, power, armor_rating, weapon):
        suppr().__init_(name, hp, speed, power, armor_rating,weapon)
        self.hp = 20
        self.type = "goblin"
        self.armor_rating = 1

    def speak(self):
        print(f"The {self.type} {self.name} is Furious! ")

