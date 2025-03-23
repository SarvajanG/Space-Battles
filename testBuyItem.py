import unittest
from shop import Shop
from player import Player


class TestBuyItem(unittest.TestCase):

    def testBuyItem(self):
        shop = Shop()
        player = Player("Test Player", 10, 10,)

        # Test if player can buy an item with 0 wallet funds
        player.wallet = 0
        shop.buyItem(player, shop.items[3])
        self.assertEqual(player.inventory.items, [])

        # Test if player can buy an item with sufficient wallet funds
        player.wallet = 1000
        shop.buyItem(player, shop.items[3])
        self.assertEqual(player.inventory.items[-1], shop.items[3].name)

        # Test if ultimates are added to ultimates on purchase
        player.wallet = 1000
        shop.buyItem(player, shop.items[6])
        self.assertEqual(player.ultimates[-1], shop.items[6].name)

        # Test if ultimates are not added to inventory
        player.wallet = 1000
        shop.buyItem(player, shop.items[7])
        self.assertNotEqual(player.inventory.items[-1], shop.items[7].name)



unittest.main()