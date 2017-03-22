# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        Engine.swift, RACharacter.swift, RAAbility.Swift, RAMonster.swift
#              RAPlayer.swift
# Purpose:     RNG Arena Game Engine
#
# Author:  Hezekiah Valdez on 11/1/16
#
# Copyright © 2016 Hezekiah Valdez. All rights reserved.
# -----------------------------------------------------------------------------

from plistlib import *
from random import *

"""
Put Complete Paths here for testing
C:\\Users\\HP\Desktop\\Code\\RNGArenaPython\\Game
C:\\Users\\Rollie Valdez\\Desktop\\code\\RNGArenaPython\\Game
"""

#A class dictating what a character does.
class Ability():
    def __init__(self, title, dmg):
        self.name = title
        self.dmg = dmg

""""
test = Ability("bob", 10)
print(test.name)
"""


# A Class to define the properties of a character
class Character:
    def __init__(self, health, isPlayer):
        # Blank initializer for players
        if (isPlayer):
            self.level = 0
            self.hp = health
            self.name = "Chuck Norris"
            self.ability1 = None
            self.ability2 = None
            self.ability3 = None
            self.ability4 = None
        # Setting monsters a random level and basing remaining stats on random level
        else:
            self.level = randint(1, 10)
            self.hp = health * self.level
            self.name = "League of Legends Sucks"

    # Sets the name of the character
    def setName(self, newName):
        self.name = newName

    # modifiys the current character health
    def modHP(self, newHP):
        self.hp = self.hp - newHP
        if(self.hp < 0):
            self.hp = 0

    # Returns the current HP of a character
    def getCurrentHP(self):
        return self.hp

    # Sets one of the abilities of a character
    def setAbility(self, ability, number):
        if (number == 1):
            self.ability1 = ability
        elif (number == 2):
            self.ability2 = ability
        elif (number == 3):
            self.ability3 = ability
        else:
            self.ability4 = ability

    def getAbility(self, number):
        if (number == 1):
            return self.ability1
        elif (number == 2):
            return self.ability2
        elif (number == 3):
            return self.ability3
        else:
            return self.ability4

#A class defining the characteristics of a character
class Monster(Character):
    def __init__(self, names, abilityData):
        Character.__init__(self, 20, False)
        self.names = names
        self.abilityData = abilityData

    def setMonster(self):
        rand1 = randint(1, len(self.abilityData) - 1)
        rand2 = randint(1, len(self.abilityData) - 1)
        rand3 = randint(1, len(self.abilityData) - 1)
        rand4 = randint(1, len(self.abilityData) - 1)

        rand5 = randint(0, len(self.names) - 1)

        # Set the name of the current monster


        self.name = self.names[rand5]

        # Get the data instances from the

        data1 = self.abilityData[rand1]
        data2 = self.abilityData[rand2]
        data3 = self.abilityData[rand3]
        data4 = self.abilityData[rand4]

        self.setAbility(data1, 1)
        self.setAbility(data2, 2)
        self.setAbility(data3, 3)
        self.setAbility(data4, 4)

class Player(Character):
    def __init__(self, abilityData):
        Character.__init__(self, 100, True)
        self.abilityData = abilityData

    def setPlayer(self):
        rand1 = randint(1, len(self.abilityData) - 1)
        data1 = self.abilityData[(rand1)]

        ability1 = Ability(data1["Name"], data1["Damage"])
        blankAbility = Ability("None", 0)
        self.setAbility(ability1, 1)
        self.setAbility(blankAbility, 2)
        self.setAbility(blankAbility, 3)
        self.setAbility(blankAbility, 4)


class Engine():

    def __init__(self, path):
        fullPath = path + "\\Data.plist"
        datalist = readPlist(fullPath)
        self.playerTurn = False
        self.gameOver = False
        self.monsterDead = False
        self.score = 0
        self.highScore = 0
        self.currentMonster = ""
        self.player = ""
        self.levelData = "empty"
        self.monsterNames = datalist.get("MonsterNames")
        self.abilityNames = datalist.get("AbilityNames")

    def dealDamage(self, ability):
        if(self.playerTurn):
            self.currentMonster.hp = self.currentMonster.hp - ability.Damage
            if(self.currentMonster.hp <= 0):
                self.currentMonster.hp = 0
                self.monsterDead = True
                self.score += 1
            self.playerTurn = False
        else:
            self.player.hp = self.player.hp - ability.Damage
            if(self.player.hp <= 0):
                self.gameOver = True
            self.playerTurn = True

    def startPlayer(self):
        tmp = Player(self.abilityNames)
        self.player = Player(self.abilityNames)
        self.player.setPlayer()

    def getNewMonster(self):
        self.currentMonster = Monster(self.monsterNames, self.abilityNames)
        self.currentMonster.setMonster()
        self.monsterDead = False

    def addAbility(self, skill, abilityNumber):
        self.player.setAbility(skill, abilityNumber)

    #Fill the loot array with three random abilities and return the array
    def chooseThree(self):
        selectArray = []
        count = 0
        while (count < 3):
            rand1 = randint(0, len(self.abilityNames) - 1)

            #Access random ability position
            data1 = self.abilityNames[rand1]

            #Create the ability instance
            ability1 = Ability(data1["Name"], data1["Damage"])
            selectArray.append(ability1)

            count += 1
        return selectArray


'''
game = Engine("C:\\Users\\Rollie Valdez\\Desktop\\code\\RNGArenaPython\\Game")
game.startPlayer()
game.getNewMonster()
randNum = randint(1, 4)
game.dealDamage(randNum)
tmpAbility = game.currentMonster.getAbility(randNum)
print(game.player.hp)
'''

'''
#gameIn = raw_input("Please Type the location of your game folder>>")
game = Engine("C:\\Users\\Rollie Valdez\\Desktop\\code\\RNGArenaPython\\Game")
game.startPlayer()
game.getNewMonster()
choosing = False
helping = False

def gameState():

    print("Score: 0      Your Health: " +  str(game.player.hp))
    print("Enemy Name: " + str(game.currentMonster.name))
    print("Enemy Health: " + str(game.currentMonster.hp))
    print("Ability 1: " + str(game.player.ability1.name) + " Damage: " + str(game.player.ability1.dmg))
    print("Ability 2: " + str(game.player.ability2.name) + " Damage: " + str(game.player.ability2.dmg))
    print("Ability 3: " + str(game.player.ability3.name) + " Damage: " + str(game.player.ability3.dmg))
    print("Ability 4: " + str(game.player.ability4.name) + " Damage: " + str(game.player.ability4.dmg))

def help():
    print("Supported functions are:")
    print("help")
    print("Type a number 1-4 to choose an ability or loot")


def choiceNum():
    bob="lol"


SUPPORTED_FUNCTIONS = {"help": help, "1": choiceNum, "2": choiceNum, "3": choiceNum, "4": choiceNum}



def run(action):
    if not action:
        return
    if action in SUPPORTED_FUNCTIONS:
        return SUPPORTED_FUNCTIONS[action]
    else:
        error()


def error():
    print("Error: Nonvalid Operation type help for list of valid operations")


more_input = True
while more_input:
    gameIn = raw_input("RNGArena>>")
    if (gameIn == "q"):
        more_input = False
        print('Exiting RNGArena')
    else:
        result = run(gameIn)
        result()
'''
