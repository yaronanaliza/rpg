from doctest import master

from core.player import *
from random import choice


class Game:
    def __init__(self):
        self.player = Player("uri")


    def choose_random_monster(self)->Orc|Goblin:
        if choice(["orc","goblin"]) == "orc":
            return Orc("orci")
        else:
            return Goblin("goblini")

    def show_menu(self)-> bool:
        while(True):
            user_choice = input("Select 1: Battle  2: Exit\n")
            if user_choice in ["1","2"]:
                if user_choice == "1":
                    return True
                else:
                    return False



    def start(self):
       if self.show_menu():
            self.game_monster = self.choose_random_monster()
            print(f"my monster name {  self.game_monster.name}")
            self.battle(self.player, self.game_monster)


    def switch_players(self,player1,player2):
        player1, player2 = player2,player1

    def battle(self,player:Character, monster:Monster)->None:
            result = []
            attacker = player
            defender = monster
            for game_player in [player,monster]:
                result.append(game_player.calc_dice_and_speed())

            if result[1] > result[0]:
                self.switch_players(attacker,defender)

            while True:
                atc_success = attacker.attack(attacker,defender)
                if  not atc_success:
                    return None
                self.switch_players(attacker, defender)
