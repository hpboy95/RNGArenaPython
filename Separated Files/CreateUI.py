
from random import *

class CreateUI():
    
    def __init__(self):

        self.game = Engine("C:\\Users\\HP\\Desktop\\Code\\RNGArenaPython\\Game")
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
        print("Ability 1: " + str(self.game.getAbilityName(1)) + " Damage: " + str(self.game.getAbilityDamage(1)))
        print("Ability 2: " + str(self.game.getAbilityName(2)) + " Damage: " + str(self.game.getAbilityDamage(1)))
        print("Ability 3: " + str(self.game.getAbilityName(3)) + " Damage: " + str(self.game.getAbilityDamage(1)))
        print("Ability 4: " + str(self.game.getAbilityName(4)) + " Damage: " + str(self.game.getAbilityDamage(1)))
    

    
    def aiTurn(self):
        randNum = randint(1, 4)
        self.game.dealDamage(randNum)
        tmpAbility = self.game.currentMonster.getAbility(randNum)
        print(self.game.getCharacterName + " cast " +  self.game.getAbilityName(randNum) +
            " for "  + self.game.getAbilityDamage(randNum) +  "damage")
         
    def start(self):
        self.starting = False
        self.aiTurn()

    def choiceNum(self):
        print("No Implement")
        
    def error(self):
        print("Error: Nonvalid Operation type help for list of valid operations")

    SUPPORTED_FUNCTIONS = {"start": start,
                           "1": choiceNum, "2": choiceNum, "3": choiceNum, "4": choiceNum,
                           "error": error}

    def run(self, action):
        if not action:
            return
        if action in self.SUPPORTED_FUNCTIONS:
            running = self.SUPPORTED_FUNCTIONS[action]
            running(self)
        else:
            self.SUPPORTED_FUNCTIONS["error"]()
            
    
def main():


    tmp = CreateUI()
    if (tmp.starting == True):
        print("Welcome to RNGArena please type 'start' to begin")   
    more_input = True
    while more_input:
        gameIn = str.lower(raw_input("RNGArena>>"))
        if (gameIn == "q"):
            more_input = False
            print('Exiting RNGArena')
        elif (gameIn == "help"):
            print(tmp.SUPPORTED_FUNCTIONS.keys())
        else: 
            result = tmp.run(gameIn)
            
if __name__ == '__main__':
    main()
