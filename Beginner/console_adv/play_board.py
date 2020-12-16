import numpy as np


class PlayBoard:

    def __init__(self):
        self.board = np.array([[1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]])
        self.x = 1
        self.y = 1
        self.position = self.board[self.x][self.y]

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.position = self.board[self.x][self.y]

    def move_right(self):
        if self.get_position() % 3 == 0:
            return
        else:
            self.set_position(self.x, self.y+1)

    def move_left(self):
        if self.get_position() % 3 == 1:
            return
        else:
            self.set_position(self.x, self.y-1)

    def move_up(self):
        if self.get_position() <= 3:
            return
        else:
            self.set_position(self.x-1, self.y)

    def move_down(self):
        if self.get_position() >= 7:
            return
        else:
            self.set_position(self.x+1, self.y)

    def room_description(self, room):
        room_defs = {
            1: "You are in room 1. This is the kitchen where out chef hands out.",
            2: "You are in room 2. This is the first of four bedrooms. Try to find the other one.",
            3: "You are in room 3. This is the only bathroom in the house. Weird that it's hidden in the corner of the house.",
            4: "You are in room 4. This is the entry way to the house. Only one way in and out.",
            5: "You are in room 5. This is the starting room. This room is oddly empty.",
            6: "You are in room 6. This is the second bedroom in the house. Find the rest.",
            7: "You are in room 7. This is bedroom number 3. Find the others.",
            8: "You are in room 8. This is the fourth bedroom in the house. Have you found the others?",
            9: "You are in room 9. This is the office. Why is it in the corner?"
        }
        return room_defs[room]
