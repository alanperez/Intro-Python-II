# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def move(self, direction):
        self.direction = direction
