from random import *

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

    def setName(self, newName):
        self.name = newName

    def modHP(self, newHP):
        self.hp = self.hp - newHP

    def getCurrentHP(self):
        return self.hp

    def setAbility(self, ability, number):
        if (number == 1):
            self.ability1 = ability
        elif (number == 2):
            self.ability2 = ability
        elif (number == 3):
            self.ability3 = ability
        else:
            self.ability4 = ability


class Ability():
    def __init__(self, title, dmg):
        self.name = title
        self.dmg = dmg

    # char1 deals damage to char 2
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