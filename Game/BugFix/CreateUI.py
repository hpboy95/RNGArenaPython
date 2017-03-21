from RAEngine import Engine
from random import *
import sys

class CreateUI():
    
    def __init__(self):
        self.fullPath = "C:\Users\Ray\Desktop\CS156_Project\RNGArenaPython-master\Game"
        self.game = Engine(self.fullPath)
        self.game.startPlayer()
        self.game.getNewMonster()
        self.starting = True
        self.choosing = False
        self.isDead = False

    def gameState(self):

        print("Score: " + str(self.game.score))
        print("Your Health: " + str(self.game.player.hp))
        print("Enemy Name: " + str(self.game.currentMonster.name))
        print("Enemy HP: " + str(self.game.currentMonster.hp))

    def seeAbs(self):

        tmp1 = self.game.player.getAbility(1)
        tmp2 = self.game.player.getAbility(2)
        tmp3 = self.game.player.getAbility(3)
        tmp4 = self.game.player.getAbility(4)

        print("Ability 1: Name - " + tmp1.name + " Damage - " + str(tmp1.dmg))
        print("Ability 2: Name - " + tmp2.name + " Damage - " + str(tmp2.dmg))
        print("Ability 3: Name - " + tmp3.name + " Damage - " + str(tmp3.dmg))
        print("Ability 4: Name - " + tmp4.name + " Damage - " + str(tmp4.dmg))

    def aiTurn(self):
        randNum = randint(1, 4)
        tmpAbility = self.game.currentMonster.getAbility(randNum)
        self.game.dealDamage(tmpAbility)

        #Monster Cast
        print(self.game.currentMonster.name +  " cast " + tmpAbility.Name
              + " for " + str(tmpAbility.Damage))
        if self.game.gameOver:
            self.gameOver()
        #Player Status
        else:
            print("You have " + str(self.game.player.hp) + " hp remaining")
         
    def start(self):
        self.starting = False
        if self.game.gameOver:
            self.game = Engine(self.fullPath)
            self.game.startPlayer()
            self.game.getNewMonster()
        self.aiTurn()

    def gameOver(self):
        print("Game Over")
        print("Score: " + str(self.game.score))
        #import sys
        userIn = str.lower(raw_input("Type 'start' for a new game:")) # Fixed this so it doesn't allow you to spam commands other than start after a game.
        if(userIn != 'start'):
            sys.exit(0)
        else: self.game.score = 0
        #print("Type 'start' for a new game")

    def choiceNum(self, number):
        tmpAbility = self.game.currentMonster.getAbility(number)
        self.game.dealDamage(tmpAbility)
        self.game.playerTurn = False

        print ("You used " + tmpAbility.Name +  " for " + str(tmpAbility.Damage) + " damage")
        if self.game.monsterDead:
            print(self.game.currentMonster.name + "is defeated!")
            self.game.getNewMonster
            print (self.game.currentMonster.name + " entered the battle!")
            self.game.monsterDead = False
        else:
            print(self.game.currentMonster.name + " has " + str(self.game.currentMonster.hp) + " hp left" )
            self.aiTurn()


        
    def error(self):
        print("Error: Nonvalid Operation type help for list of valid actions")

    SUPPORTED_FUNCTIONS = {"start": start, "error": error, "status": gameState, "abilities": seeAbs}

    SUPPORTED_CHOICES = { "1": choiceNum, "2": choiceNum, "3": choiceNum, "4": choiceNum }
    def run(self, action):
        if not action:
            return
        if action in self.SUPPORTED_FUNCTIONS:
            running = self.SUPPORTED_FUNCTIONS[action]
            running(self)
        elif action in self.SUPPORTED_CHOICES:
            running = self.SUPPORTED_CHOICES[action]
            running(self, int(action))
        else:
            self.SUPPORTED_FUNCTIONS["error"](self)
            
    
def main():


    tmp = CreateUI()
    if (tmp.starting == True):
        print("Welcome to RNGArena please type 'start' to begin")   
    more_input = True
    def help():
        if (tmp.game.playerTurn):
            print("Type 'status' for current state")
            print("Type 'abilities' to get a list of your current abilities")
            print("Type a number 1-4 to select a skill to use")
        else:
            print("Please type 'start to begin or 'q' to quit")
    while more_input:
        gameIn = str.lower(raw_input("RNGArena>>"))
        if (gameIn == "q"):
            more_input = False
            print('Exiting RNGArena')
        elif (gameIn == "help"):
            help()
        else: 
            result = tmp.run(gameIn)
            
if __name__ == '__main__':
    main()
