from core.player import  *
from random import randint
class Monster(Character):
    def __init__(self, name, hp, type, speed, power, armor_rating, weapon: str = choice(["knife", "sword", "axe"])):
        suppr().__init_(name, hp, speed, power, armor_rating)
        self.weapon = weapon

    @staticmethod
    def attack(player: Player, monster: Orc | Goblin):
        monster_dice = monster.roll_dice(20) + self.speed
        if monster_dice > player.armor_rating:
            return True
        else:
            return False


class Orc(Monster):
    def __init__(self, name, hp, type, speed, power, armor_rating, weapon):
        suppr().__init_(name, hp, speed, power, armor_rating,weapon)
        self.type = "orc"
        self.speed = randint(0,5)
        self.power = randint(10, 15)
        self.armor_rating = randint(2,8)

    def speak(self):
        print(f"The {self.type} {self.name} is Furious! ")


