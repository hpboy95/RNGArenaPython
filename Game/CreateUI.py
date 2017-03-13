from RAEngine import *


class CreateUI():
    
    def __init__(self):

        self.game = Engine("C:\Users\Rollie Valdez\Desktop\code\RNGArenaPython\Game")
        self.game.startPlayer()
        self.game.getNewMonster()
        self.choosing = False
        self.helping = False

    def gameState(self):
        print("Score: 0      Your Health: " +  str(self.game.player.hp))
        print("Enemy Name: " + str(self.game.currentMonster.name))
        print("Enemy Health: " + str(self.game.currentMonster.hp))
        print("Ability 1: " + str(self.game.player.ability1.name) + " Damage: " + str(self.game.player.ability1.dmg))
        print("Ability 2: " + str(self.game.player.ability2.name) + " Damage: " + str(self.game.player.ability2.dmg))
        print("Ability 3: " + str(self.game.player.ability3.name) + " Damage: " + str(self.game.player.ability3.dmg))
        print("Ability 4: " + str(self.game.player.ability4.name) + " Damage: " + str(self.game.player.ability4.dmg))
    
    def help():
        print("Supported functions are:")
        print("help")
        print("Type a number 1-4 to choose an ability or loot")
    
    
    def choiceNum():
        print("No Implement")
    
    def run(self, action):
        SUPPORTED_FUNCTIONS = {"help": self.help, "1": self.choiceNum, "2": self.choiceNum, "3": self.choiceNum, "4": self.choiceNum}
        if not action:
            return
        if action in SUPPORTED_FUNCTIONS:
            return SUPPORTED_FUNCTIONS[action]
        else:
            error()
            
    def error():
        print("Error: Nonvalid Operation type help for list of valid operations")

def main():
    tmp = CreateUI()
    more_input = True
    while more_input:
        gameIn = raw_input("RNGArena>>")
        if (gameIn == "q"):
            more_input = False
            print('Exiting RNGArena')
        else: 
            result = tmp.run(gameIn)
            result()
            
if __name__ == '__main__':
    main()
