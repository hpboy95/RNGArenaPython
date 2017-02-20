# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        Character.swift, Ability.Swift, Monster.Swift, Player.Swift 
# Purpose:     RNG Arena Game Engine 
# 
# Author:  Hezekiah Valdez on 11/3/16 
# 
# Copyright © 2016 Hezekiah Valdez. All rights reserved. 
# -----------------------------------------------------------------------------

from random import *
from RAAbility import *

class Character: 
        
        #Setting u a random level and basing remaining stats on random level
        
        #Blank initializer for players
        def __init__(self):
            self.level = 0
            self.hp = 100
            self.name = "Chuck Norris"
            self.ability1 = None
            self.ability2 = None
            self.ability3 = None
            self.ability4 = None
            
        def __init__(self, health):
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
         Character.__init__(self, 20)
         self.names = names
         self.abilityData = abilityData

    def setMonster(self):
        rand1 = randint(1, len(abilityData))
        rand2 = randint(1, len(abilityData))
        rand3 = randint(1, len(abilityData))
        rand4 = randint(1, len(abilityData))
        rand5 = randint(0, len(names) - 1)
        
        #Set the name of the current monster
        self.name = names[rand5]
        
        #Get the data instances from the
        
        data1 = abilityData[str(rand1)]
        data2 = abilityData[str(rand2)]
        data3 = abilityData[str(rand3)]
        data4 = abilityData[str(rand4)]
        
        data1.deal_damage
         
        self.setAbility(data1, 1)
        self.setAbility(data2, 2)
        self.setAbility(data3, 3)
        self.setAbility(data4, 4)

class Player(Character):
    
    def __init__(self, abilityData):
         Character.__init__(self)
         self.abilityData = abilityData
         
    def setPlayer(self):
        rand1 = randint(1, len(abilityData))
        
        data1 = abilityData[str(rand1)]
        
        
        


      
ability1 = Ability("name1", 10)
ability2 = Ability("name2", 20)
ability3 = Ability("name3", 30)
ability4 = Ability("name4", 40)

name1 = "test1"
name2 = "test2"
name3 = "test3"
name4 = "test4"


names = [name1, name2, name3, name4]
abilityData = {"1": ability1, "2": ability2, "3": ability3, "4": ability4}

mon = Monster(names, abilityData)
mon.setMonster()
print(mon.hp)
mon.ability1.deal_damage(mon)
print(mon.hp)