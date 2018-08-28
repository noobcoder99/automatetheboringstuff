# prac project from textbook
inventory = {' rope': 1, ' torch': 1, ' gold coin': 10}
def display_inventory(inventory):
    print("Inventory:")
item_total = 0
for k, v in inventory.items():
    print(str(v) + '' + k)
    item_total += v
    print("Total number of items: " + str(item_total))
