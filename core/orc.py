
from random import randint,choice
from core.character import *


class Orc(Monster):

    def __init__(self, name,armor_rating:int= randint(2,8) , hp: int=50,type:str ="orc", speed: int = randint(0, 5), power: int = randint(10, 15)
                 , weapon:str= choice(["knife", "sword", "axe"])):
        super().__init__(name,armor_rating, hp,type, speed, power,weapon)
        
