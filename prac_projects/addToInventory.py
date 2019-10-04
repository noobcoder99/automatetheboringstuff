dragonLoot = ['gold coin', 'dagger']

def addToInventory(inventory, addItems):
    inv = ['gold coin', 'dagger']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
    
