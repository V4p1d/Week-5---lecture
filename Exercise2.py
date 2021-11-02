'''
You are creating a fantasy video game and you were tasked with dealing with the part of the code
to manage the player inventory.
The inventory of the player is a dictionary where the key represents the object and the value
represents the quantity possessed.

Suppose that in the game the player just vanquised a dragon and the corpse loot looks like this:

dragonLoot = ["Long sword +5, vorpal", "gold coin", "gold coin", "gold coin", "potion of cure wounds"]

Write a function named addToInventory(inventory, addedItems) that returns a dictionary which represents
the updated inventory. 
Your code should look something like this:
'''
def addToInventory():

    # Write your code here
    return 

inv = {"gold coin": 42, "rope": 1, "potion of cure moderate wounds": 1}
dragonLoot = ["Long sword +5, vorpal", "gold coin", "gold coin", "gold coin", "potion of cure moderate wounds"]
inv = addToInventory(inv, dragonLoot)
print(inv)