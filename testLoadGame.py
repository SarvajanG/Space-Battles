import unittest
from player import Player
from saveGame import saveGame, loadGame


class TestLoadGame(unittest.TestCase):

    def testLoadGame(self):
        # Create a player with item in inventory then save game
        player = Player("Test Player", 200, 80)
        player.inventory.addItem("Test Item")
        saveGame(player)

        # Re-initialize player to reset stats
        player = Player("Not Test Player", 500, 22)

        # Load the game save
        loadGame(player)

        # Test if player name is retrieved from loadGame
        self.assertEqual(player.name, "Test Player")

        # Test if player health is retrieved from loadGame
        self.assertEqual(player.health, 200)

        # Test if player attack is retrieved from loadGame
        self.assertEqual(player.attack, 80)

        # Test if player's inventory is retrieved from loadGame
        self.assertEqual(player.inventory.items, ["Test Item"])

unittest.main()