from core.player import *
from core.orc import *
from core.goblin import *
from random import choice


class Game:
    def __init__(self):
        self.player = Player("uri")

    def start(self):
       if show_menu():
            monster = self.choose_random_monster()
            if monster_selected == "orc":
                self.game_monster = Orc("orci")
            else:
                self.game_monster = Goblin("goblini")
            self.battle(self.player, self.game_monster)

    def calc_dice_and_speed(self,game_player:Player|Orc|Goblin):
        return self.roll_dice(6) + game_player.speed

    def calc_dice_and_power(self,game_player:Player|Orc|Goblin):
        return self.roll_dice(6) + game_player.power


    def calc_damage(self,game_player:Player|Orc|Goblin):
            result = calc_dice_and_power(game_player)
            if game_player.__name__ != "Player":
                match game_player.weapon:
                    case "knife":
                        result *= 0.5
                    case "axe":
                        result *= 1.5
            return result





    def battle(player:Player, monster:Orc|Goblin):
        result = []
        for game_player in [self.player,self.monster]:
            result.append(calc_dice_and_speed(game_player))

        if result[1] > result[0]:
            currurn_turn = "monster"
        else:
            currurn_turn = "player"
        while player.hp > 0 and monster.hp > 0:
            if currurn_turn == "player":
                atc_success = player.attack(self.player,self.monster)
                if  atc_success:
                    calc_damage()


                    currurn_turn = "monster"
                else:
                    calc_damage()


    @staticmethod
    def roll_dice(sides:int):
        return randint(1, sides)

    def show_menu()-> bool:
        while(True):
            user_choice = input("Select 1: Battle  2: Exit")
            if user_choice in ["1","2"]:
                if user_choice == 1:
                    return True
                else:
                    return False
            battle(player, monster)

    def choose_random_monster():
        return choice(["orc","goblin"])





