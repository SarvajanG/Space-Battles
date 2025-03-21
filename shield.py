from item import Item

class Shield(Item):
    def __init__(self, name, cost, strength):
        super().__init__(name, cost)
        self.strength = strength

    def useShield(self, player):
        player.shield += self.strength
        print(f'{self.name} applied, shield strength increased by {self.strength}')
