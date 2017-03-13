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
from RAMonster import *
from RACharacter import *
from RAAbility import *
from RAPlayer import *

"""
Put Complete Paths here for testing
C:\\Users\\HP\Desktop\\Code\\RNGArenaPython\\Game
C:\\Users\\Rollie Valdez\\Desktop\\code\\RNGArenaPython\\Game
"""

class Engine():
    
    def __init__(self, path):
        fullPath = path + "\\Data.plist"
        datalist = readPlist(fullPath)
        self.score = 0
        self.highScore = 0
        self.currentMonster = ""
        self.player = None
        self.levelData = "empty"
        self.monsterNames = datalist.get("MonsterNames")
        self.abilityNames = datalist.get("AbilityNames")
        
    def dealDamage(self, isPlayer, abiityNumber):
        if(isPlayer):
            tmp = player.getAbility(abilityNumber)
            player.take_damage(tmp, currentMonster)
        else:
            tmp = currentMonaster.getAbility(abilityNumber)
            currentMonster.take_damage(tmp. player)
    
    def startPlayer(self):
        tmp = Player(self.abilityNames)
        self.player = Player(self.abilityNames)
        self.player.setPlayer()

    def getNewMonster(self):
        self.currentMonster = Monster(self.monsterNames, self.abilityNames)
        self.currentMonster.setMonster()
        
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

        