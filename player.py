from inventory import Inventory
class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.wallet = 0
        self.shield = 0
        self.starEnergy = 1
        self.ultimates = []
        self.inventory = Inventory()

    def isAlive(self):
        return self.health > 0
    
    def takeDamage(self, damage):
        self.health -= damage
        print(f'Player has taken {damage} damage')
    
        