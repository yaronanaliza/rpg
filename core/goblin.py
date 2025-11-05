from core.character import *

class Goblin(Monster):
    def __init__(self, name,armor_rating:int= 1,  hp: int=20,type:str ="goblin", speed: int = randint(0, 5), power: int = randint(10, 15)
                , weapon:str= choice(["knife", "sword", "axe"])):

        super().__init__(name,armor_rating, hp,type, speed, power, weapon)
