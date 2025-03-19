from potion import healthPotion, attackPotion
from shield import miniShield, mediumShield
from ultimate import flameBeam, iceShards
class Shop:
    def __init__(self):
        self.items = {"Plasma Blaster": 25,
                      "Chrono Sword": 100,
                      healthPotion.name: 50,
                      attackPotion.name: 50,
                      miniShield.name: 25,
                      mediumShield.name: 50,
                      flameBeam.name: 200,
                      iceShards.name: 250}
        
    def displayShop(self):
        print("Shop Items:")
        for item, cost in self.items.items():
            print(f'{item}: {cost} solons')

    def buyItem(self, player, itemName):
        if itemName in self.items:
            cost = self.items[itemName]
            if player.wallet >= cost:
                player.wallet -= cost
                if cost > 200:
                    player.ultimates.append(itemName)
                    print(f'{itemName} purchased and added to ultimates')
                else:
                    player.inventory.addItem(itemName)
                    print(f'{itemName} purchased and added to inventory')
            else:
                print("Insufficient solons")
        else:
            print("Item not available in this sector of the universe")