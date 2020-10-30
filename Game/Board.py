import tkinter as tk
import os
from Game.Street import Street as ST
from Game.Go import Go
from Game.Go_to_jail import Go_to_jail as GTJ
from Game.Free_parking import Free_parking as FP
from Game.Jail import Jail as JA
from Game.Displayable import Displayable
import random
import time
from PIL import Image, ImageTk

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


class Board(Displayable):
    #  Constructor
    def __init__(self):
        super().__init__()
        self.squares = []
        self.loc = 0  # Pointer for the words
        with open(f'{self.getProject_files_root()}\Cities\Cities.txt', "r") as text:  # Squares details
            self.words = text.read().split()  # Getting it's value

    # Get the window
    def getWindow(self):
        return self.window

    # Get the board
    def getBoard(self):
        return self.board

    # Get the dice
    def getDice(self):
        return self.dice

    # Set the results
    def setResults(self, results):
        self.results.set(results)

    # Get the squares
    def getSquares(self):
        return self.squares

    # Load and resize the pictures for the game
    def loadBoard_pictures(self):
        height = self.getScreen_height()
        self.roll_dice_pic = ImageTk.PhotoImage(Image.open(f'{self.project_root}\Files\Misc\dice.png')
                                                .resize(
            (int(0.15 * height), int(0.075 * height))
            , Image.ANTIALIAS))
        self.monopoly_title = ImageTk.PhotoImage(Image.open(f'{self.project_root}\Files\Misc\monopoly_title.png')
                                                 .resize((int(0.6 * height), int(0.15 * height))
                                                         , Image.ANTIALIAS))
        self.jail_pic = ImageTk.PhotoImage(Image.open(f'{self.project_root}\Files\Misc\jail.png')
                                           .resize((int(0.2 * height), int(0.2 * height))
                                                   , Image.ANTIALIAS))
        self.go_pic = ImageTk.PhotoImage(Image.open(f'{self.project_root}\Files\Misc\go.png')
                                         .resize((int(0.2 * height), int(0.2 * height))
                                                 , Image.ANTIALIAS))
        self.go_to_jail_pic = ImageTk.PhotoImage(Image.open(f'{self.project_root}\Files\Misc\go_to_jail.png')
                                                 .resize((int(0.2 * height), int(0.2 * height))
                                                         , Image.ANTIALIAS))
        self.free_parking_pic = ImageTk.PhotoImage(Image.open(f'{self.project_root}\Files\Misc\parking.png')
                                                   .resize(
            (int(0.2 * height), int(0.2 * height))
            , Image.ANTIALIAS))
        self.icon = f'{self.project_root}\Files\Misc\icon.ico'

    # Get the icon
    def getIcon(self):
        return self.icon

    # Get the monopoly title
    def getMonopoly_title(self):
        return self.monopoly_title

    # Set the icon for the window
    def setIcon_window(self):
        self.window.iconbitmap(self.icon)

    # Create and place the dice
    def createDice(self):
        self.results = tk.StringVar()
        numbers = tk.StringVar(value=self.results)
        self.dice = tk.Label(self.getBoard(), image=self.roll_dice_pic, textvariable=self.results,
                             font=(None, 16, 'bold'), compound='center', bg="DarkSeaGreen1")
        self.dice.place(x=0.425 * self.screen_height, y=0.225 * self.screen_height,
                        height=0.125 * self.screen_height, width=0.15 * self.screen_height)

    # Create the game title- Monopoly and Monopoly sign in the middle of the board
    def createTitle(self):
        background = tk.Label(self.board, bg="DarkSeaGreen1")
        background.place(x=0.2 * self.screen_height, y=0.2 * self.screen_height
                         , height=0.6 * self.screen_height, width=0.6 * self.screen_height)
        self.window.title("Monopoly")  # The title in the top left
        # The Monopoly picture
        tk.Label(self.board, image=self.monopoly_title, bg="DarkSeaGreen1"). \
            place(x=0.2 * self.screen_height, y=0.4 * self.screen_height, height=0.15 * self.screen_height,
                  width=0.6 * self.screen_height)

    # Even lines creator
    def even_lines(self, j):
        if j == 0:
            x = 0  # x pointer
            y = 0  # y pointer
            special_square_loc = 0  # The location of the special square
        else:
            x = self.screen_height / 5  # x pointer
            y = self.screen_height - self.screen_height / 5  # y pointer
            special_square_loc = 6  # The location of the special square
        for i in range(7):  # This line's squares loop
            if i == special_square_loc:  # Special square
                if special_square_loc == 6:
                    self.squares.append(FP(tk.Label(self.board, height=int(self.screen_height / 5),
                                                    width=int(self.screen_height / 5),
                                                    image=self.free_parking_pic, highlightthickness=True,
                                                    bg="DarkSeaGreen1")))

                else:
                    self.squares.append(Go(tk.Label(self.board, height=int(self.screen_height / 5),
                                                    width=int(self.screen_height / 5),
                                                    image=self.go_pic, highlightthickness=True,
                                                    bg="DarkSeaGreen1")))
                self.squares[len(self.squares) - 1].getFrame().place(x=x, y=y)
                self.squares[len(self.squares) - 1].setX(x)
                self.squares[len(self.squares) - 1].setY(y)
                x = x + self.screen_height / 5
            else:  # Normal square
                self.squares.append(ST(tk.Frame(self.board, height=int(self.screen_height / 5),
                                                width=int(self.screen_height / 10), bg="DarkSeaGreen1"
                                                , highlightthickness=True)))
                self.squares[len(self.squares) - 1].getFrame().place(x=x, y=y)
                if j == 0:
                    self.square_details(self.up())
                else:
                    self.square_details(self.down())
                self.squares[len(self.squares) - 1].setX(x)
                self.squares[len(self.squares) - 1].setY(y)
                x = x + self.screen_height / 10
                self.loc += 4

    # Even lines creator
    def uneven_lines(self, j):
        pass
        if j == 1:
            x = self.screen_height - self.screen_height / 5  # x pointer
            y = 0  # y pointer
            special_square_loc = 0  # The location of the special square
        else:
            x = 0  # x pointer
            y = self.screen_height / 5  # y pointer
            special_square_loc = 6  # The location of the special square
        for i in range(7):  # This line's squares loop
            if i == special_square_loc:  # Special square
                if special_square_loc == 6:
                    self.squares.append(GTJ(tk.Label(self.board, height=int(self.screen_height / 5),
                                                     width=int(self.screen_height / 5),
                                                     image=self.go_to_jail_pic, highlightthickness=True
                                                     , bg="DarkSeaGreen1")))

                else:
                    self.squares.append(JA(tk.Label(self.board, height=int(self.screen_height / 5),
                                                    width=int(self.screen_height / 5),
                                                    image=self.jail_pic, highlightthickness=True, bg="DarkSeaGreen1")))
                self.squares[len(self.squares) - 1].getFrame().place(x=x, y=y)
                self.squares[len(self.squares) - 1].setX(x)
                self.squares[len(self.squares) - 1].setY(y)
                y = y + self.screen_height / 5
            else:  # Normal square
                self.squares.append(ST(tk.Frame(self.board, height=int(self.screen_height / 10),
                                                width=int(self.screen_height / 5),
                                                bg="DarkSeaGreen1", highlightthickness=True)))
                self.squares[len(self.squares) - 1].getFrame().place(x=x, y=y)
                if j == 1:
                    self.square_details(self.right())
                else:
                    self.square_details(self.left())
                self.squares[len(self.squares) - 1].setX(x)
                self.squares[len(self.squares) - 1].setY(y)
                y = y + self.screen_height / 10
                self.loc += 4

    # Square details creator
    def square_details(self, func):
        x, y, color_height, color_width, color_x, color_y = func
        city = tk.Label(self.squares[len(self.squares) - 1].getFrame(), font=("Times", "13", "italic bold"),
                        text=self.words[self.loc], bg="DarkSeaGreen1")
        city.place(relheight=0.125, relwidth=1, relx=x, rely=y)
        self.squares[len(self.squares) - 1].setCity(self.words[self.loc])
        street_and_price = tk.Label(self.squares[len(self.squares) - 1].getFrame(), font=("David", "12"),
                                    text=f'{self.words[self.loc + 1]} {self.words[self.loc + 2]}₪', bg="DarkSeaGreen1")
        street_and_price.place(relheight=0.125, relwidth=1, relx=x, rely=y + 0.125)
        self.squares[len(self.squares) - 1].setStreet(self.words[self.loc + 1])
        self.squares[len(self.squares) - 1].setLand_price(int(self.words[self.loc + 2]))
        square_color = tk.Label(self.squares[len(self.squares) - 1].getFrame(), bg=self.words[self.loc + 3])
        self.squares[len(self.squares) - 1].setColor(self.words[self.loc + 3])
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

    # Sort the squares by their location on the board
    def sortSquares(self):
        fourteentwenty = []
        twentyonetwentyseven = []
        for i in range(7):
            fourteentwenty.append(self.squares[20 - i])
            twentyonetwentyseven.append(self.squares[27 - i])
        self.squares[14:20] = fourteentwenty
        self.squares[21:27] = twentyonetwentyseven

    # Create the board squares
    def create_board(self):
        # Methods for creation of the board
        self.window = tk.Tk()  # Create the window of the game
        self.board = tk.Frame(self.window, height=self.screen_height, width=self.screen_height)  # Create the board
        self.loadBoard_pictures()
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
        self.sortSquares()
        self.board.place(x=0, y=0)
        self.setIcon_window()
        self.createTitle()
        self.createDice()
        self.window.attributes("-fullscreen", True)
        # For testing
        # height = self.getScreen_height()
        # self.buttons = []
        # self.buttons.append(tk.Button(self.getBoard(), text="Roll Dice", bg="white", font=(None, 16, 'bold')
        #                               )
        #                     .place(x=0.3*height, y=0.225*height, height=0.05*height, width=0.1*height))
        # self.buttons.append(tk.Button(self.getBoard(), text="Buy", bg="white", font=(None, 16, 'bold')
        #                               )
        #                     .place(x=0.3*height, y=0.3*height, height=0.05*height, width=0.1*height))
        # self.buttons.append(tk.Button(self.getBoard(), text="End Turn", bg="white", font=(None, 16, 'bold')
        #                               )
        #                     .place(x=0.6*height, y=0.225*height, height=0.05*height, width=0.1*height))
        # self.buttons.append(tk.Button(self.getBoard(), text="Show Card", bg="white", font=(None, 16, 'bold')
        #                               )
        #                     .place(x=0.6*height, y=0.3*height, height=0.05*height, width=0.1*height))
        # self.window.mainloop()


if __name__ == "__main__":
    board = Board()
    board.create_board()
