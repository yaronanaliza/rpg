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

    @staticmethod
    def roll_dice(sides: int):
            return randint(1, sides)
    def calc_dice_and_speed(self):
        return self.roll_dice(6) + self.speed

    def calc_dice_and_power(self):
        return self.roll_dice(6) + self.power

    def calc_damage(self):
            result = self.calc_dice_and_power()
            if hasattr(self, "weapon"):
                match game_player.weapon:
                    case "knife":
                        result *= 0.5
                    case "axe":
                        result *= 1.5
            return result


    def check_hp(self,game_player)->bool:
        if game_player.hp <= 0:
            return False
        else:
            return True

    def after_attac(self, attaker, defender) -> bool:
        damage = self.calc_damage()
        defender.hp -= damage
        attaker.speak()
        print(f"{attaker.name} have life {attaker.hp}")
        defender.speak()
        print(f"{defender.name} have life {defender.hp}")
        if not self.check_hp(defender):
            print(f"{attaker.name} won")
            return False
        return True



    def attack(self,attacker, defender)->bool:
        attcker_dice = attacker.roll_dice(20) + attacker.speed
        if attcker_dice > defender.armor_rating:
            if not self.after_attac(attacker, defender):
                return False
        return True



class Monster(Character):
    def __init__(self, name,armor_rating, hp, type, speed, power, weapon: str = choice(["knife", "sword", "axe"])):
        super().__init__(name, armor_rating,hp, speed, power)
        self.weapon = weapon
        self.type = type
    def speak(self):
        print(f"i am monster name  {self.name} ")