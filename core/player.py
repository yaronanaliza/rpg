from random import randint ,choice
from tkinter.font import names
from tty import ISPEED
from game import *
from core.orc import *
from core.goblin import *

class Character:

    def __init__(self, name: str,armor_rating: int, hp: int=50, speed: int = randint(5, 10), power: int = randint(5, 10) ):
        self.name = name
        self.armor_rating = armor_rating
        self.hp = hp
        self.speed = speed
        self.power =power

    def speak(self):
        pass

    def attack(self):
        pass








class Player(Character):
    def __init__(self,name,hp,speed,power,armor_rating,profession:str=choice(["warrior","Healer"])):
        suppr().__init_(name,hp,speed,power,armor_rating)
        self.profession = profession
        if self.profession == "warrior":
            self.power += 2
        self.armor_rating = randint(5,15)

    def speak(self,message)->None:
        print(f"{self.name} say {message}")

    @staticmethod
    def attack(player: Player, monster: Orc|Goblin)->bool:
        player_dice = player.roll_dice(20) + self.speed
        if player_dice > monster.armor_rating:
            return True
        else:
            return False





