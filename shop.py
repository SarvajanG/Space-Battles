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
        
    def displayShop(self, player):
        while True:
            print("Shop Items:")
            shopIndex = 1
            for item in self.items:
                print(f'{shopIndex}. {item.name}: {item.cost} solons')
                shopIndex += 1
            print("1. Buy")
            print("2. Exit")
            choice = int(input())
            if choice == 1:
                while True:
                    item = int(input("Enter item number: "))
                    if item > 0 and item <= len(self.items):
                        self.buyItem(player, self.items[item - 1])
                        break
                    else:
                        print("Item not available in this sector of the universe")
            elif choice == 2:
                print("Exited shop")
                break
            else:
                print("Invalid Option")

    def buyItem(self, player, item):
            cost = item.cost
            if player.wallet >= cost:
                player.wallet -= cost
                if cost >= 200:
                    player.ultimates.append(item.name)
                    print(f'{item.name} purchased and added to ultimates')
                else:
                    player.inventory.addItem(item.name)
                    print(f'{item.name} purchased and added to inventory')
            else:
                print("Insufficient solons")
            