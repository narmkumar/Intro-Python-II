from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together:

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

from item import Item
# Creating items & then adding them to rooms:
items = {
    "coins" : Item("coins", "Coins - items that are useful for accumulating wealth"),
    "sword" : Item("sword", " a Sword - a weapon you can use for defense"),
    "beer" : Item("beer", "a Beer - a drink you can have to relax"),
}


room["outside"].add_item(items["coins"])
room["foyer"].add_item(items["sword"])
room["overlook"].add_item(items["beer"])

#
# Main
#
from player import Player

# Make a new player object that is currently in the 'outside' room.
player = Player("Nar", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.




# Loop
while True:
    # Print
    print(f"{player.name}, you are currently at the {player.present_room} \n{player.present_room.description}")
    # Read
    cmd = input("--> ")
    # Eval
    player.command(cmd)