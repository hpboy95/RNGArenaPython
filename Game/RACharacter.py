# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        Characeter.swift 
# Purpose:     RNG Arena Game Engine 
# 
# Author:  Hezekiah Valdez on 11/3/16 
# 
# Copyright © 2016 Hezekiah Valdez. All rights reserved. 
# -----------------------------------------------------------------------------
from random import *

class Character(): 
        
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
            self.level = random.randint()
            self.hp = health * Int(tmpNum)
            self.name = ""
            
            
            