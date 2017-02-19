# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        Engine.swift 
# Purpose:     RNG Arena Game Engine 
# 
# Author:  Hezekiah Valdez on 11/1/16 
# 
# Copyright © 2016 Hezekiah Valdez. All rights reserved. 
# -----------------------------------------------------------------------------

class Engine(): 
    
    def __init__(self):
        self.score = 0
        self.highScore = 0
        self.currentMonster = Monster()
        self.player = Player()
        self.levelData = "empty"
        self.monsterNames = []
        self.abilityNames = {}
        
    def dealDamage(isPlayer, abiityNumber):
        if(isPlayer):
            tmp = player.getAbility(abilityNumber)
            player.take_damage(tmp, currentMonster)
        else:
            tmp = currentMonaster.getAbility(number: abilityNumber)
            currentMonster.take_damage(tmp. player)
