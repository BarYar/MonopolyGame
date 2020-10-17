from Game.Board import Board
from Game.Player import Player
from Game.Characters import Characters
import tkinter as tk
import random
import time


"""Game class- 
   parameters: 

   attributes:             
                1. players [] - List of the players that are in the game (List(Player(obj))).
                2. game_money - The amount  of money that every player gets when the game starts (int).
                    - default value=5000
                3. characters- List of the game characters,
                   each player can choose his character when the game starts (Characters(obj)).
                4. in_game- True- The game started, False- The game ended (boolean)
                5. in_turn- The turn started, False- The turn ended (boolean)
                6. current_player- Pointer for the current player (int)
                7. roll_dice_pice- PhotoImage object in tkinter (PhotoImage(Tkinter(obj))
                8. screen_width - The width of the screen.
                9. screen_height - The height of the screen.
                10. window - the window of the game (Tkinter(obj)).
                11. board - the frame of the board in the window (Tkinter(obj)).
                12. squares - The list of the squares (List(Tkinter(obj))
                13. loc - The pointer of the words (int). - default value = 0 
                14. words - The list of the squares details strings (List(string))
                15. start_screen - This screen will be create when the game start.
                16. buttons- list of the game buttons (List(tk.Button(obj)))

   """


class Mygame(Board):
    #  Constructor
    def __init__(self):
        super().__init__()
        self.players = []
        self.characters = Characters()
        self.game_money = 5000
        self.current_player = 0
        self.in_game = False
        self.in_turn = False
        self.buttons = []
        self.players_quantity = 0

    # Get the game_money
    def getGame_money(self):
        return self.game_money

    # Get the players list
    def getPlayers(self):
        return self.players

    # Get the in_game
    def getIn_game(self):
        return self.in_game

    # Get the in_turn
    def getIn_turn(self):
        return self.in_turn

    # Get the players quantity
    def getPlayers_quantity(self):
        return self.players_quantity

    # Get the player by name
    def getPlayer(self, name):
        for player in self.players:
            if player.getName() == name:
                return player

    # Remove the player by name
    def removePlayer(self, name):
        for player in self.players:
            if player.getName() == name:
                self.players.remove(player)

    # Adds the player to the players list, from the start screen
    def addPlayer(self):
        char = self.characters.getRandom_character()
        self.players.append(Player(self.name_entry.get(), self.game_money, char))
        # self.players[len(self.players)-1].loadCharacter_picture() - For future updates
        self.name_entry.delete(0, 'end')
        if self.players_quantity == len(self.players):
            self.destroyWindow(self.start_screen)

    # Set the in_game
    def setIn_game(self, in_game):
        self.in_game = in_game

    # Set the in_turn
    def setIn_turn(self, in_turn):
        self.in_turn = in_turn

    # Set the players quantity
    def setPlayers_quantity(self,quantity):
        self.players_quantity = quantity

    # Start new game
    def newGame(self):
        self.startScreen()
        self.create_board()
        self.create_players_frame()
        self.createButtons()
        self.locateStart()

    # The players enter their names and choose their character
    # This method is being called by the start screen buttons
    def players_personal_information(self, players_quantity):
        self.setPlayers_quantity(players_quantity)
        height = self.getScreen_height()
        for button in self.start_buttons:
            button.destroy()
        self.name_entry = tk.Entry(self.start_screen)
        self.name_entry.place(x=0.04 * height, y=0.11 * height, height=0.02 * height, width=0.15 * height)  # Name entry
        tk.Label(self.start_screen, font=("Times", "10", "bold"), text="Name:", bg="white")\
            .place(x=0, y=0.11 * height, height=0.02 * height, width=0.03 * height)  # Name label
        tk.Button(self.start_screen, font=("Times", "10", "bold"),
                  text="Enter", command=self.addPlayer, bg="DarkSeaGreen1")\
            .place(x=0.1*height, y=0.15 * height, height=0.02 * height, width=0.03 * height)  # Enter button

    # The start screen - welcome label and buttons for choosing players quantity
    def startScreen(self):
        height = self.getScreen_height()
        self.start_screen = tk.Tk()
        self.loadBoard_pictures()  # Load board the pictures
        self.start_screen.geometry(f"{str(int(height / 4))}x{str(int(height / 4))}")
        self.start_screen.iconbitmap(self.getIcon())  # Set the icon for the window
        self.start_screen.title("Monopoly")  # The screen title
        self.start_label = tk.Label(self.start_screen,
                                    text="Welcome to the Monopoly Game\nChoose this game players quantity.",
                                    font=("Times", "15", "bold"), bg="white").place(x=0, y=0)  # The screen label
        self.start_screen.configure(bg="white")
        self.start_buttons = []
        for i in range(3):  # Adding the quantity buttons
            self.start_buttons.append(tk.Button(self.start_screen, text=str(i+2), font=(None, 16, 'bold'),
                                                command=lambda p=i: self.players_personal_information(p+2)
                                                , bg="DarkSeaGreen1"))
            self.start_buttons[i].place(x=(i * 0.0625+0.035) * height, y=0.11 * height, height=0.03 * height,
                                        width=0.05 * height)
        self.start_screen.mainloop()

    # Destroy the window, that it gets as a parameter
    def destroyWindow(self, win):
        win.destroy()

    # Create the players details frames.
    def create_players_frame(self):
        height = self.getScreen_height()
        width = self.getScreen_width()
        self.players_frames = []
        self.players_cards_frames = []
        for i in range(self.players_quantity):
            self.players_frames.append(tk.Frame(self.getWindow(), bg="SkyBlue1", highlightthickness=True))
            self.players_frames[i].place(x=height, y=(height / self.players_quantity)*i,
                                        height=height/self.players_quantity, width=width - height)
            self.players_frame_details(i)

    # Players frame details
    def players_frame_details(self, cur_player):
        tk.Label(self.players_frames[cur_player], font=(None, 18, 'bold'),
                 text=f"Name: {self.players[cur_player].getName()}", bg="SkyBlue1").\
            place(relx=0, rely=0, relheight=1/8, relwidth=1)
        card_frame = tk.Frame(self.players_frames[cur_player], bg="SkyBlue1")
        card_frame.place(relx=0, rely=1/8, relheight=7/8, relwidth=1)
        self.addCards_frames(card_frame)

    # Add Frames to card_frames, all of the frames there are "sons" of player_frame.
    def addCards_frames(self, frame):
        self.players_cards_frames.append(frame)

    # Add cards to player card_frame.
    # Get the player num in the list.
    def addCards_player_card_frame(self, player_num):
        pass

    # Create the game buttons
    def createButtons(self):
        height = self.getScreen_height()
        self.buttons.append(tk.Button(self.getBoard(), text="Roll Dice", bg="white", font=(None, 16, 'bold')
                                      , command=self.roll_dice)
                            .place(x=0.3*height, y=0.225*height, height=0.05*height, width=0.1*height))
        self.buttons.append(tk.Button(self.getBoard(), text="Buy", bg="white", font=(None, 16, 'bold')
                                      , command=self.buy)
                            .place(x=0.3*height, y=0.3*height, height=0.05*height, width=0.1*height))
        self.buttons.append(tk.Button(self.getBoard(), text="End Turn", bg="white", font=(None, 16, 'bold')
                                      , command=self.end_turn())
                            .place(x=0.6*height, y=0.225*height, height=0.05*height, width=0.1*height))
        self.buttons.append(tk.Button(self.getBoard(), text="Show Card", bg="white", font=(None, 16, 'bold')
                                      , command=self.show_card)
                            .place(x=0.6*height, y=0.3*height, height=0.05*height, width=0.1*height))
        self.setButtons_disabled()

    # Create the player circle
    def create_player_circle(self, x, y, r, canvas):  # center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1)

    # Locate the given player on the given square
    def locatePlayer(self, player, square_num):
        colors = ["blue2", "orange", "gold", "black"]
        self.getSquares()[square_num].addPlayer_square(player)
        player_picture = tk.Canvas(self.getBoard(), bg=colors[self.current_player])
        # player_picture = player.getCharacter_picture()
        player_picture.place(x=player.getX(), y=player.getY(), height=player.getHeight(), width=player.getWidth())

    # Locate the players on the first square and set first frame to white- first player
    def locateStart(self):
        colors = ["blue2", "orange", "gold", "black"]
        color_locator = 0
        for player in self.players:
            # player_picture = tk.Canvas(self.getBoard(), bg=colors[color_locator])
            # player.setCharacter_Picture(player_picture)
            self.locatePlayer(player, 0)
            # self.getSquares()[0].addPlayer_square(player)
            # player_picture.place(x=player.getX(), y=player.getY(), height=player.getHeight(), width=player.getWidth())
            # self.create_player_circle(player.getX(), player.getY(), player.getHeight(), player_picture) -Does'nt work
            color_locator += 1

    # Set the state of  all of the buttons to disabled, for all players.
    def setButtons_disabled(self):
        pass

    # Set the state of the buttons to enabled - except roll dice for the player in i position
    def setButtons_enabled(self):
        pass

    # Set roll the dice button to enabled for the player in i position
    def setRoll_dice_enabled(self):
        pass

    # When pressing on "Roll Dice" button, this command will start
    def roll_dice(self):
        result1 = random.randint(1, 6)
        result2 = random.randint(1, 6)
        self.setResults(f" {result1}               {result2} ")
        time.sleep(1)  # Update the result
        time.sleep(2)  # Wait until the move
        self.player_move(result1+result2)

    # After the roll_dice method has ended, this method will start
    def player_move(self, moves):
        square_num = self.players[self.current_player].getCurrent_square() + moves
        if square_num == 28:
            self.players[self.current_player].moneyTransaction(400)
            square_num = 0
        elif square_num > 28:
            self.players[self.current_player].moneyTransaction(200)
            square_num = square_num - 28
        self.players[self.current_player].setCurrent_square(square_num)
        self.locatePlayer(self.players[self.current_player], square_num)

    # When pressing on "Show Card" button, this command will start
    def show_card(self):
        pass

    # When pressing on "End Turn" button, this command will start after end_turn command
    def end_show_card(self):
        pass

    # When pressing on "Buy" button, this command will start
    def buy(self):
        pass

    # When player pressing on "Quit" button, this command will start
    def quit(self):
        self.players.remove(self.players[self.current_player])
        self.setPlayers_quantity(self.getPlayers_quantity()-1)
        if len(self.players) == 1:
            self.end_game()
        pass

    # When pressing on "End Turn" button, this command will start
    def end_turn(self):
        self.in_turn = False



        if self.current_player < len(self.players)-1:
            self.current_player += 1
        else:
            self.current_player = 0
        self.end_show_card()
        self.setRoll_dice_enabled()
        pass

    # Create a label of the game winners
    def createWinners(self):
        pass

    # When pressing on "End Game" button, this command will start
    def end_game(self):
        self.in_turn = False
        self.in_game = False
        for frame in self.window.winfo_children():
            frame.destroy()
        self.createTitle()
        self.createWinners()
        pass

    # Starts the game
    def startGame(self):
        self.newGame()
        self.in_turn = True
        self.in_game = True
        while self.in_game:
            self.setRoll_dice_enabled()
            self.window.mainloop()


if __name__ == "__main__":
    game = Mygame()
    game.startGame()
