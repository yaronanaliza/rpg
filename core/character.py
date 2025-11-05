from random import randint,choice
class Character:

    def __init__(self, name: str,armor_rating: int, hp: int=50, speed: int = randint(5, 10), power: int = randint(5, 10) ):
        self.name = name
        self.armor_rating = armor_rating
        self.hp = hp
        self.speed = speed
        self.power =power

    def speak(self):
        print(f"i am player name {self.name} ")

    def attack(self):
        pass


class Monster(Character):
    def __init__(self, name,armor_rating, hp, type, speed, power, weapon: str = choice(["knife", "sword", "axe"])):
        super().__init__(name, armor_rating,hp, speed, power)
        self.weapon = weapon
        self.type = type
    def speak(self):
        print(f"i am monster name  {self.name} ")