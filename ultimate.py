from item import Item

class Ultimate(Item):
    def __init__(self, name, cost, strength):
        super().__init__(name, cost)
        self.strength = strength

    def useUltimate(self, player, target):
        if player.starEnergy > 0:
            player.starEnergy = 0
            target.takeDamage(self.strength)
            print(f'{self.name} used, {target.name} took {self.strength} damage')
        else:
            print(f'Star energy depleted for this battle')

