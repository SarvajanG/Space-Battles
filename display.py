from inventory import Inventory
from player import Player

def displayChoices():
    print("Select an option:")
    print("1. Attack")
    print("2. View Inventory")
    print("3. View Shop")
    print("4. Save Game")
    print("5. Load Game")
    print("6. Quit Game")

def displayStats(entity):
    print(f'{entity.name}:')
    print(f'Health: {entity.health}', end="")
    if type(entity) == Player:
        print("--", end="")
        print(f'Shield: {entity.shield}', end="")
    print(" -------------------------------- ", end="")
    if type(entity) == Player:
        print(f'Attack: {entity.attack}', end="")
        print("--", end="")
        print(f'Solar Energy: {entity.starEnergy}')
    else:
        print(f'Attack: {entity.attack}')

def displayInventory(inventory):
    if inventory:
        print("*****INVENTORY*****")
        for item in inventory.items:
            print(item)
        print("*******************")
    else:
        print("No items in inventory")