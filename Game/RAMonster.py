from random import *
from RACharacter import Character

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