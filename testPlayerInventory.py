from player import Player
from inventory import Inventory

player = Player("Test Player", 88, 34)

# Check the type of player's inventory attribute
assert type(player.inventory) is Inventory

player.inventory.addItem("Test Sword")

# Check if an added item is in the inventory
assert "Test Sword" in player.inventory.items

# Check if a non added item is not in the inventory
assert "Fake Sword" not in player.inventory.items

player.inventory.deleteItem("Test Sword")

# Check if item is deleted from inventory
assert "Test Sword" not in player.inventory.items