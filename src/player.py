# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, present_room):
        self.name = name
        self.present_room = present_room
        self.items = []

    def command(self, command):
        #Pick up and drop commands
        x = command.split()
        if x[0] == "pickup":
            for item in self.present_room.items:
                if item.name == x[1]:
                    self.pickup_item(item)
        elif x[0] == "drop":
            for item in self.items:
                if item.name == x[1]:
                    self.drop_item(item)

        #Movement
        elif command == "n":
            if self.present_room.n_to is not None:
                self.present_room = self.present_room.n_to
            else:
                print("Can't go this way")
        elif command == "s":
            if self.present_room.s_to is not None:
                self.present_room = self.present_room.s_to
            else:
                print("Can't go this way")
        elif command == "e":
            if self.present_room.e_to is not None:
                self.present_room = self.present_room.e_to
            else:
                print("Can't go this way")
        elif command == "w":
            if self.present_room.w_to is not None:
                self.present_room = self.present_room.w_to
            else:
                print("Can't go this way")

        elif command == "q":
            print("Goodbye!")
            exit()
        elif command == "i":
            print("My items:")
            for item in self.items:
                print(f"-- {item}")
        else:
            print("**Please input n,s,e,w to move a direction or q to quit"
                  "\n**To perform an action, type take or drop followed by item name"
                  "\n**To view your items, type i")

    def pickup_item(self, item):
        self.items.append(item)
        self.present_room.picked_item(item)
        print(f"Picked up {item.description}")

    def drop_item(self, item):
        self.items.remove(item)
        self.present_room.add_item(item)
        print(f"Dropped {item.description}")