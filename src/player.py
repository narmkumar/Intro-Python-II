# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, present_room):
        self.name = name
        self.present_room = present_room

    def move(self, command):
        if command == "n":
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
        else:
            print("Please input n,s,e,w to move a direction or q to quit")