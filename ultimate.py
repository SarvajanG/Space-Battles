class Ultimate:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def useUltimate(self, player, target):
        if player.starEnergy > 0:
            player.starEnergy = 0
            target.takeDamage(self.strength)
            print(f'{self.name} used, {target.name} took {self.strength} damage')
        else:
            print(f'Star energy depleted for this battle')

flameBeam = Ultimate("Flame Beam", 100)
iceShards = Ultimate("Ice Shards", 120)