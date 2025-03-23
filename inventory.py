class Inventory:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)
        print(f'Added {item} to inventory')

    def deleteItem(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f'Deleted {item} from inventory')
        else:
            print(f'{item} not in inventory')

    def clear(self):
        self.items.clear()