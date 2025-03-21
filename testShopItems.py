import unittest
from item import Item

class TestItem(unittest.TestCase):

    def testItem(self):
        item = Item("Test Sword", 3000)

        # Test if given item name is item name
        self.assertEqual(item.name, "Test Sword")

        # Test if non-given item name is not item name
        self.assertNotEqual(item.name, "Not Test Sword")

        # Test if given item cost is item cost
        self.assertEqual(item.cost, 3000)

        # Test if non-given item cost is not item cost
        self.assertNotEqual(item.cost, 1234532765)

unittest.main()