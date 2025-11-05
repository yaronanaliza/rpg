
from random import randint,choice
from core.character import *


class Orc(Monster):

    def __init__(self, name,armor_rating:int= randint(2,8) , hp: int=50,type:str ="orc", speed: int = randint(0, 5), power: int = randint(10, 15)
                 , weapon:str= choice(["knife", "sword", "axe"])):
        super().__init__(name,armor_rating, hp,type, speed, power,weapon)
        



    @staticmethod
    def attack(player: Character, monster: Monster):
        monster_dice = monster.roll_dice(20) + monster.speed
        if monster_dice > player.armor_rating:
            return True
        else:
            return False

    @staticmethod
    def roll_dice(sides:int):
        return randint(1, sides)