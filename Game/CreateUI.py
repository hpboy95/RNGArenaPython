from RAEngine import *
from random import *

class CreateUI():
    
    def __init__(self):

        self.game = Engine("C:\Users\Rollie Valdez\Desktop\code\RNGArenaPython\Game")
        self.game.startPlayer()
        self.game.getNewMonster()
        self.starting = True
        self.choosing = False
        self.helping = False
        self.playerTurn = False
        self.attacking = False
        self.isDead = False
        self.gameOVer = False

    def gameState(self):
        print("Score: " + str(self.game.score))
        print("Your Health: " + str(self.game.player.hp))
        print("Enemy Name: " + str(self.game.currentMonster.name))
        print("Enemy Health: " + str(self.game.currentMonster.hp))
        print("Ability 1: " + str(self.game.player.ability1.name) + " Damage: " + str(self.game.player.ability1.dmg))
        print("Ability 2: " + str(self.game.player.ability2.name) + " Damage: " + str(self.game.player.ability2.dmg))
        print("Ability 3: " + str(self.game.player.ability3.name) + " Damage: " + str(self.game.player.ability3.dmg))
        print("Ability 4: " + str(self.game.player.ability4.name) + " Damage: " + str(self.game.player.ability4.dmg))
    
    SUPPORTED_FUNCTIONS = {"help": help, "start": start, 
            "1": choiceNum,"2": choiceNum, "3": choiceNum, "4": choiceNum}
    
    def aiTurn(self):
        randNum = randint(1, 4)
        self.game.dealDamage(False, randNum)
        tmpAbility = self.game.currentMonster.getAbility(randNum)
        print(self.game.currentMonster.name + " cast " +  tmpAbility.name + 
            " for "  + str(tmpAbility.dmg) +  "damage")
         
    def start(self):
        self.starting = False
        self.aiTurn()
    
    def help(self):
        print(SUPPORTED_FUNCTIONS.keys())
    
    
    def choiceNum(self):
        print("No Implement")
        
    def error(self):
        print("Error: Nonvalid Operation type help for list of valid operations")

    def run(self, action):
        if not action:
            return
        if action in SUPPORTED_FUNCTIONS:
            return SUPPORTED_FUNCTIONS[action]
        else:
            return self.error
            
    
def main():
    tmp = CreateUI()
    if (tmp.starting == True):
        print("Welcome to RNGArena please type 'start' to begin")   
    more_input = True
    while more_input:
        gameIn = raw_input("RNGArena>>")
        if (gameIn == "q"):
            more_input = False
            print('Exiting RNGArena')
        else: 
            result = tmp.run(str.lower(gameIn))
            result()
            
if __name__ == '__main__':
    main()
