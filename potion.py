class Potion:
    def __init__(self, name, strength, type):
        self.name = name
        self.strength = strength
        self.type = type

    def usePotion(self, player):
        if self.type == "health":
            player.health += self.strength
            print(f'Consumed {self.name}, health increased by {self.strength}')
        elif self.type == "attack":
            player.attack += self.strength
            print(f'Consumed {self.name}, attack increased by {self.strength}')

healthPotion = Potion("Health Potion", 50, "health")
attackPotion = Potion("Attack Potion", 25, "attack")