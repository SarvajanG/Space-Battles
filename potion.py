from item import Item

class Potion(Item):
    def __init__(self, name, cost, strength, type):
        super().__init__(name, cost)
        self.strength = strength
        self.type = type

    def usePotion(self, player):
        if self.type == "health":
            player.health += self.strength
            print(f'Consumed {self.name}, health increased by {self.strength}')
        elif self.type == "attack":
            player.attack += self.strength
            print(f'Consumed {self.name}, attack increased by {self.strength}')

