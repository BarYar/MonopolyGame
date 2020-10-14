import tkinter as tk
import ctypes
from tkinter import font
import os
from Game.Root import Root


"""Board class- 
   parameters: 

   attributes:             
                1. screen_width - The width of the screen.
                2. screen_height - The height of the screen.
                3. window - the window of the game (Tkinter(obj)).
                4. board - the frame of the board in the window (Tkinter(obj)).
                5. squares - The list of the squares (List(Tkinter(obj))
                6. loc - The pointer of the words (int). - default value = 0 
                7. words - The list of the squares details strings (List(string))
   """


class Board(Root):
    #  Constructor
    def __init__(self):
        super().__init__()
        user32 = ctypes.windll.user32
        self.screen_width = user32.GetSystemMetrics(0)
        self.screen_height = user32.GetSystemMetrics(1)
        self.window = tk.Tk()
        self.board = tk.Frame(self.window, height=self.screen_height, width=self.screen_height)
        self.squares = []
        self.loc = 0  # Pointer for the words
        with open(f'{self.project_files_root}\Cities\Cities.txt', "r") as text:  # Squares details
            self.words = text.read().split()  # Getting it's value

    # Even lines creator
    def even_lines(self, j):
        if j == 0:
            x = 0  # x pointer
            y = 0  # y pointer
            special_square_loc = 0  # The location of the special square
        else:
            x = self.screen_height/5  # x pointer
            y = self.screen_height - self.screen_height/5  # y pointer
            special_square_loc = 6  # The location of the special square
        for i in range(7):  # This line's squares loop
            if i == special_square_loc:  # Special square
                self.squares.append(tk.Frame(self.board, height=int(self.screen_height / 5),
                                             width=int(self.screen_height / 5), bg="gold", highlightthickness=True))
                self.squares[len(self.squares) - 1].place(x=x, y=y)
                x = x + self.screen_height/5
            else:  # Normal square
                self.squares.append(tk.Frame(self.board, height=int(self.screen_height/5),
                                             width=int(self.screen_height/10), bg="white", highlightthickness=True))
                self.squares[len(self.squares) - 1].place(x=x, y=y)
                if j == 0:
                    self.square_details(self.up())
                else:
                    self.square_details(self.down())
                x = x + self.screen_height / 10
                self.loc += 4

    # Even lines creator
    def uneven_lines(self, j):
        pass
        if j == 1:
            x = self.screen_height - self.screen_height / 5   # x pointer
            y = 0  # y pointer
            special_square_loc = 0  # The location of the special square
        else:
            x = 0  # x pointer
            y = self.screen_height / 5  # y pointer
            special_square_loc = 6  # The location of the special square
        for i in range(7):  # This line's squares loop
            if i == special_square_loc:  # Special square
                self.squares.append(tk.Frame(self.board, height=int(self.screen_height / 5),
                                             width=int(self.screen_height / 5), bg="gold", highlightthickness=True))
                self.squares[len(self.squares) - 1].place(x=x, y=y)
                y = y + self.screen_height / 5
            else:  # Normal square
                self.squares.append(tk.Frame(self.board, height=int(self.screen_height / 10),
                                             width=int(self.screen_height / 5), bg="white", highlightthickness=True))
                self.squares[len(self.squares) - 1].place(x=x, y=y)
                if j == 1:
                    self.square_details(self.right())
                else:
                    self.square_details(self.left())
                y = y + self.screen_height / 10
                self.loc += 4

    # Square details creator
    def square_details(self, func):
        x, y, color_height, color_width, color_x, color_y = func
        city = tk.Label(self.squares[len(self.squares) - 1], font=("Times", "13", "italic bold"),
                        text=self.words[self.loc], bg="white")
        city.place(relheight=0.125, relwidth=1, relx=x, rely=y)
        street_and_price = tk.Label(self.squares[len(self.squares) - 1], font=("David", "12"),
                                    text=f'{self.words[self.loc+1]} {self.words[self.loc+2]}₪', bg="white")
        street_and_price.place(relheight=0.125, relwidth=1, relx=x, rely=y+0.125)
        square_color = tk.Label(self.squares[len(self.squares) - 1], bg=self.words[self.loc+3])
        square_color.place(relheight=color_height, relwidth=color_width, relx=color_x, rely=color_y)

    # Square details of the up line
    # Returns tuple of: x, y, color_height, color_width, color_x, color_y
    def up(self):
        return 0, 0, 0.125, 1, 0, 0.875

    # Square details of the up line
    # Returns tuple of: x, y, color_height, color_width, color_x, color_y
    def down(self):
        return 0, 0.75, 0.125, 1, 0, 0

    # Square details of the up line
    # Returns tuple of: x, y, color_height, color_width, color_x, color_y
    def right(self):
        return 0, 0, 1, 0.125, 0, 0

    # Square details of the up line
    # Returns tuple of: x, y, color_height, color_width, color_x, color_y
    def left(self):
        return 0, 0, 1, 0.125, 0.875, 0

    # Create the board squares
    def create_squares(self):
        for j in range(4):
            if j % 2 == 0:
                if j == 0:
                    self.even_lines(j)
                else:
                    self.even_lines(j)
            else:
                if j == 1:
                    self.uneven_lines(j)
                else:
                    self.uneven_lines(j)
        self.board.place(x=0, y=0)
        self.window.attributes("-fullscreen", True)
        self.window.mainloop()


if __name__ == "__main__":
    board = Board()
    board.create_squares()
