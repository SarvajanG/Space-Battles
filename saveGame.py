import json

def saveGame(player, inventory, filename="savegame.json"):
    gameState = {
        "name": player.name,
        "health": player.health,
        "attack": player.attack,
        "inventory": inventory.items,
        "wallet": player.wallet,
        "shield": player.shield,
        "starEnergy": player.starEnergy,
        "ultimates": player.ultimates
    }
    with open(filename, 'w') as file:
        json.dump(gameState, file)
        print("Game saved successfully")

def loadGame(filename="savegame.json"):
    with open(filename, 'r') as file:
        gameState = json.load(file)
        print("Game loaded successfully")
        return gameState