from random import *
from RAAbility import Ability

# A Class to define the properties of a character
class Character:
    def __init__(self, health, isPlayer):
        # Blank initializer for players
        if (isPlayer):
            self.level = 0
            self.hp = 100
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

    #Sets the name of the character
    def setName(self, newName):
        self.name = newName
    #modifiys the current character health
    def modHP(self, newHP):
        self.hp = self.hp - newHP

    #Returns the current HP of a character
    def getCurrentHP(self):
        return self.hp

    #Sets one of the abilities of a character
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

    def take_damage(self, ab, char1):
        if ab is Ability:
            ab.deal_damage(char1)
