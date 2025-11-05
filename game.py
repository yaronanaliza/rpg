from doctest import master

from core.player import *
from random import choice


class Game:
    def __init__(self):
        self.player = Player("uri")

    def start(self):
       if self.show_menu():
            monster_selected = self.choose_random_monster()
            if monster_selected == "orc":
                self.game_monster = Orc("orci")
            else:
                self.game_monster = Goblin("goblini")
            print(f"my monster name {  self.game_monster.name}")
            self.battle(self.player, self.game_monster)

    def calc_dice_and_speed(self,game_player:Character):
        return self.roll_dice(6) + game_player.speed

    def calc_dice_and_power(self,game_player:Character):
        return self.roll_dice(6) + game_player.power


    def calc_damage(self,game_player:Character):
            result = self.calc_dice_and_power(game_player)
            if hasattr(game_player, "weapon"):
                match game_player.weapon:
                    case "knife":
                        result *= 0.5
                    case "axe":
                        result *= 1.5
            return result


    def check_hp(self,game_player:Character)->bool:
        if game_player.hp <= 0:
            return False
        else:
            return True

    def after_attac(self,attaker:Character,attaced:Character)->bool:
        damage = self.calc_damage(attaker)
        attaced.hp -= damage
        print(f"{attaker.name} have life {attaker.hp}")
        print(f"{attaced.name} have life {attaced.hp}")
        if not self.check_hp(attaced):
            print(f"{attaker.name} won")
            return False
        return True


    def battle(self,player:Character, monster:Monster)->None:
            result = []
            currurn_turn =""
            for game_player in [player,monster]:
                result.append(self.calc_dice_and_speed(game_player))

            if result[1] > result[0]:
                currurn_turn = "monster"
                player.speak()
            else:
                currurn_turn = "player"
                monster.speak()

            while True:
                if currurn_turn == "player":
                    atc_success = player.attack(player,monster)
                    if  atc_success:
                        if not self.after_attac(player,monster):
                            return None
                    currurn_turn = "monster"

                else:
                    atc_success = monster.attack(player, monster)
                    if atc_success:
                        if not self.after_attac(player, monster):
                            return None
                    currurn_turn = "player"







    @staticmethod
    def roll_dice(sides:int):
        return randint(1, sides)

    def show_menu(self)-> bool:
        while(True):
            user_choice = input("Select 1: Battle  2: Exit\n")
            if user_choice in ["1","2"]:
                if user_choice == "1":
                    return True
                else:
                    return False


    def choose_random_monster(self):
        return choice(["orc","goblin"])





