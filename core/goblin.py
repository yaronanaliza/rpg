from core.character import *

class Goblin(Monster):
    def __init__(self, name,armor_rating:int= 1,  hp: int=20,type:str ="goblin", speed: int = randint(0, 5), power: int = randint(10, 15)
                , weapon:str= choice(["knife", "sword", "axe"])):

        super().__init__(name,armor_rating, hp,type, speed, power, weapon)
        


    @staticmethod
    def attack(player: Character, monster:Monster):
        monster_dice = monster.roll_dice(20) + monster.speed
        if monster_dice > player.armor_rating:
            return True
        else:
            return False

    @staticmethod
    def roll_dice(sides: int):
        return randint(1, sides)