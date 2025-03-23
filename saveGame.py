import json

def saveGame(player, filename="savegame.json"):
    gameState = {
        "name": player.name,
        "health": player.health,
        "attack": player.attack,
        "inventory": player.inventory.items,
        "wallet": player.wallet,
        "shield": player.shield,
        "starEnergy": player.starEnergy,
        "ultimates": player.ultimates
    }
    with open(filename, 'w') as file:
        json.dump(gameState, file)
        print("Game saved successfully")

def loadGame(player, filename="savegame.json"):
    with open(filename, 'r') as file:
        gameState = json.load(file)
        print("Game loaded successfully")

        player.name = gameState["name"]
        player.health = gameState["health"]
        player.attack = gameState["attack"]
        player.wallet = gameState["wallet"]
        player.shield = gameState["shield"]
        player.starEnergy = gameState["starEnergy"]
        player.ultimates = gameState["starEnergy"]

        player.inventory.clear()
        for item in gameState["inventory"]:
            player.inventory.addItem(item)

        return gameState