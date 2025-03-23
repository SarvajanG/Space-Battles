from player import Player
from alien import Alien
from display import displayChoices, displayStats, displayInventory
from shop import Shop
from saveGame import saveGame, loadGame

playerName = input("Enter your name: ")
player = Player(playerName, 500, 50)
alien = Alien(1, 10000, 20)
shop = Shop()

while(player.isAlive() and alien.isAlive()):
    displayStats(alien)
    displayStats(player)
    displayChoices()
    choice = int(input())
    if choice == 1:
        alien.takeDamage(player.attack)
        player.takeDamage(alien.attack)
    elif choice == 2:
        displayInventory(player.inventory)
    elif choice == 3:
        shop.displayShop(player)
    elif choice == 4:
        saveGame(player)
    elif choice == 5:
        loadGame(player)
    elif choice == 6:
        print("Thanks for playing, the universe awaits your return!")
        break
if player.isAlive():
    print("Victory")
else:
    print("Defeat")
