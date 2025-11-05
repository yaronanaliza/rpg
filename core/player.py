from random import randint ,choice
from core.orc import Orc,Monster
from core.goblin import Goblin
from core.character import *


class Player(Character):
    def __init__(self, name: str,armor_rating: int=randint(5,15), hp: int=50, speed: int = randint(5, 10), power: int = randint(5, 10),profession:str=choice(["warrior","Healer"])):
        super().__init__(name,armor_rating,hp,speed,power)
        self.profession = profession
        if self.profession == "warrior":
            self.power += 2


    @staticmethod
    def attack(player: Character, monster: Monster)->bool:
        # player_dice = player.roll_dice(20) + player.speed
        player_dice = player.roll_dice(30) + player.speed
        if player_dice > monster.armor_rating:
            return True
        else:
            return False

    @staticmethod
    def roll_dice(sides: int):
        return randint(1, sides)



