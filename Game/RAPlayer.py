from random import *
from RACharacter import Character
from RAAbility import Ability

class Player(Character):
    def __init__(self, abilityData):
        Character.__init__(self, 69, True)
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