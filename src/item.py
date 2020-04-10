class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name}"

    # def take(self):
    #     print(f"You have picked up {self.name}.")
    #
    # def drop(self):
    #     print(f"You have dropped {self.name}.")



"""Create a file called item.py and add an Item class in there.

The item should have name and description attributes.

Hint: the name should be one word for ease in parsing later.
This will be the base class for specialized item types to be declared later.

Add the ability to add items to rooms.

The Room class should be extended with a list that holds the Items that are currently in that room.

Add functionality to the main loop that prints out all the items 
that are visible to the player when they are in that room.

Add capability to add Items to the player's inventory. 
The inventory can also be a list of items "in" the player, similar to how Items can be in a Room."""