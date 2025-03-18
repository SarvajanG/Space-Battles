class Alien:
    def __init__(self, powerLevel, health, attack):
        self.powerLevel = powerLevel
        self.health = health
        self.attack = attack
        self.name = "Alien"

    def isAlive(self):
        return self.health > 0

    def takeDamage(self, damage):
        self.health -= damage
        print(f'Alien has taken {damage} damage')