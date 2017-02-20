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
datalist = readPlist("C:\Users\Rollie Valdez\Desktop\code\RNGArenaPython\Game\Data.plist")

tmp1 = len(datalist.get("MonsterNames"))
print (tmp1)
"""

class Character: 
         
        def __init__(self, health, isPlayer):
            #Blank initializer for players
            if (isPlayer):
                self.level = 0
                self.hp = 100
                self.name = "Chuck Norris"
                self.ability1 = None
                self.ability2 = None
                self.ability3 = None
                self.ability4 = None
            #Setting monsters a random level and basing remaining stats on random level
            else:
                self.level = randint(1, 10)
                self.hp = health * self.level
                self.name = "League of Legends Sucks"
            
        def setName(self, newName):
            self.name = newName
         
        def modHP(self, newHP):
            self.hp = self.hp - newHP
            
        def getCurrentHP(self):
            return self.hp
            
        def setAbility(self, ability, number):
            if (number == 1):
                self.ability1 = ability
            elif(number == 2):
                self.ability2 = ability
            elif(number == 3):
                self.ability3 = ability
            else:
                self.ability4 = ability

class Ability():
    
    def __init__(self, title, dmg):
        self.name = title 
        self.dmg = dmg
        
    #char1 deals damage to char 2    
    def deal_damage(self, char1):
        char1.modHP(self.dmg)

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
       
        #Set the name of the current monster
        
        
        self.name = self.names[rand5]
       
        #Get the data instances from the
        
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
         Character.__init__(self, 69, True)
         self.abilityData = abilityData
         
    def setPlayer(self):
        rand1 = randint(1, len(abilityData))
        data1 = abilityData[str(rand1)]

class Engine(): 
    
    def __init__(self, path):
        fullPath = path + "\\Data.plist"
        datalist = readPlist(fullPath)
        self.score = 0
        self.highScore = 0
        self.currentMonster = None
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
    
    def setPlayer(self):
        abilityNames = self.abilityNames
        self.player = Player(abilityNames)
        

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


gameIn = input("Please Type the location of your game folder>>")
print(gameIn)
#game = Engine(gameIn)

"""
more_input = True
while more_input:
    expression = "RNGArena>>"
    if (expression == "q"):
        more_input = False
        print('Exiting RNGArena')
    else: 
        run(gameIn)
"""
        