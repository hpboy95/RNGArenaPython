#A class dictating what a character does.
class Ability():
    def __init__(self, title, dmg):
        self.name = title
        self.dmg = dmg

    # char1 deals damage to char 2
    def deal_damage(self, char1):
        char1.modHP(self.dmg)

""""
test = Ability("bob", 10)
print(test.name)
"""