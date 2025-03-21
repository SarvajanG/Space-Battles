from item import Item
from potion import Potion
from shield import Shield
from ultimate import Ultimate

class Shop:
    def __init__(self):
        self.items = [Item("Plasma Blaster", 25),
                      Item("Chrono Sword", 100),
                      Potion("Health Potion", 50, 50, "health"), 
                      Potion("Attack Potion", 50, 25, "attack"), 
                      Shield("Mini Shield", 25, 25), 
                      Shield("Medium Shield", 50, 50),
                      Ultimate("Flame Beam", 200, 100), 
                      Ultimate("Ice Shards", 250, 120)]
        
    def displayShop(self):
        print("Shop Items:")
        for item in self.items:
            print(f'{item.name}: {item.cost} solons')

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