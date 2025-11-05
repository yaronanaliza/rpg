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



