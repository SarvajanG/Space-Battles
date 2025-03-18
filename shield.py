class Shield:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def useShield(self, player):
        player.shield += self.strength
        print(f'{self.name} applied, shield strength increased by {self.strength}')

miniShield = Shield("Mini Shield", 25)
mediumShield = Shield("Medium Shield", 50)