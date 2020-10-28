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
    def setPlayers_quantity(self, quantity):
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
        tk.Label(self.start_screen, font=("Times", "10", "bold"), text="Name:", bg="white") \
            .place(x=0, y=0.11 * height, height=0.02 * height, width=0.03 * height)  # Name label
        tk.Button(self.start_screen, font=("Times", "10", "bold"),
                  text="Enter", command=self.addPlayer, bg="DarkSeaGreen1") \
            .place(x=0.1 * height, y=0.15 * height, height=0.02 * height, width=0.03 * height)  # Enter button

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
            self.start_buttons.append(tk.Button(self.start_screen, text=str(i + 2), font=(None, 16, 'bold'),
                                                command=lambda p=i: self.players_personal_information(p + 2)
                                                , bg="DarkSeaGreen1"))
            self.start_buttons[i].place(x=(i * 0.0625 + 0.035) * height, y=0.11 * height, height=0.03 * height,
                                        width=0.05 * height)
        self.start_screen.mainloop()

    # Destroy the window, that it gets as a parameter
    def destroyWindow(self, win):
        win.destroy()

    # Create the players details frames.
    def create_players_frame(self):
        height = self.getScreen_height()
        width = self.getScreen_width()
        colors = ["blue2", "orange", "gold", "green"]
        self.players_frames = []
        self.players_cards_frames = []
        self.players_frames_stringVar_details = []
        for i in range(self.players_quantity):
            self.players[i].setColor(colors[i])
            self.players_frames.append(tk.Frame(self.getWindow(), bg="SkyBlue1", highlightthickness=True))
            self.players_frames[i].place(x=height, y=(height / self.players_quantity) * i,
                                         height=height / self.players_quantity, width=width - height)
            self.players_frame_details(i)

    # Players frame details
    def players_frame_details(self, cur_player):
        player_details = tk.StringVar()
        player_details.set(f"Name: {self.players[cur_player].getName()} Money: {self.players[cur_player].getMoney()}")
        tk.Label(self.players_frames[cur_player], font=(None, 18, 'bold'),
                 textvariable=player_details, bg=self.players[cur_player].getColor()). \
            place(relx=0, rely=0, relheight=1 / 8, relwidth=1)
        self.players_frames_stringVar_details.append(player_details)
        card_frame = tk.Frame(self.players_frames[cur_player], bg="SkyBlue1")
        card_frame.place(relx=0, rely=1 / 8, relheight=7 / 8, relwidth=1)
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
                                      , command=self.roll_dice))
        self.buttons[0].place(x=0.3 * height, y=0.225 * height, height=0.05 * height, width=0.1 * height)
        self.buttons.append(tk.Button(self.getBoard(), text="Buy", bg="white", font=(None, 16, 'bold'),
                                      command=self.buy))
        self.buttons[1].place(x=0.3 * height, y=0.3 * height, height=0.05 * height, width=0.1 * height)
        self.buttons.append(tk.Button(self.getBoard(), text="End Turn", bg="white", font=(None, 16, 'bold')
                                      , command=self.end_turn))
        self.buttons[2].place(x=0.6 * height, y=0.225 * height, height=0.05 * height, width=0.1 * height)
        self.buttons.append(tk.Button(self.getBoard(), text="Show Card", bg="white", font=(None, 16, 'bold')
                                      , command=self.show_card))
        self.buttons[3].place(x=0.6 * height, y=0.3 * height, height=0.05 * height, width=0.1 * height)
        self.buttons.append(tk.Button(self.getBoard(), text="End Game", bg="white", font=(None, 16, 'bold')
                                      , command=self.end_game))
        self.buttons[4].place(x=0.45 * height, y=0.7 * height, height=0.05 * height, width=0.1 * height)
        self.buttonsStates(True, 0)
        self.buttonsStates(False, 1, 2, 3, 4)

    # Change the button states the value is the button
    # state = 0 - Disabled, state = 1 - Enabled
    # enable = True - state= NORMAL,  enable = False - state= DISABLED
    def buttonsStates(self, enable, *buttons_location):
        if enable:
            for location in buttons_location:
                self.buttons[int(location)].config(state=tk.NORMAL)
        else:
            for location in buttons_location:
                self.buttons[int(location)].config(state=tk.DISABLED)

    # Locate the given player on the given square
    def locatePlayer(self, player, square_num):
        player.setCurrent_square(square_num)  # Set the player square
        self.getSquares()[square_num].addPlayer_square(player)  # Add the player to the square
        if type(player.getCharacter_picture()) != str:
            player.getCharacter_picture().destroy()  # Destroy the previous location
        player_picture = tk.Canvas(self.getBoard(), bg=player.getColor())
        player.setCharacter_Picture(player_picture)
        player_picture.place(x=player.getX(), y=player.getY(), height=player.getHeight(), width=player.getWidth())

    # Locate the players on the first square and set first frame to white- first player
    def locateStart(self):
        for player in self.players:
            self.locatePlayer(player, 0)
        self.updateCurrent_player_frame_color(1)

    # Update the frame for the current player
    def updateCurrent_player_frame_color(self, last_player):
        self.players_cards_frames[self.current_player].config(bg="white")  # Set the player frame to white
        self.players_cards_frames[last_player].config(bg="SkyBlue1")  # Set the previous player frame color to blue

    # Add the houses frames
    # Add Houses and Hotel pictures!!!!!!
    def addHouses_frames(self, square):
        hnh = tk.Label(square.getFrame(), text=f'Hotel:{square.getHotel()}\n Houses:{square.getHouses()}',
                       font=("Times", "10", "italic bold"), bg="DarkSeaGreen1")
        hnh.place(relx=0.27, rely=0.27, relheight=0.45, relwidth=0.45)

    # When pressing on "Roll Dice" button, this command will start
    def roll_dice(self):
        result1 = random.randint(1, 6)
        result2 = random.randint(1, 6)
        self.setResults(f" {result1}               {result2} ")
        time.sleep(1)  # Update the result
        self.player_move(result1 + result2, result1 == result2)
        self.buttonsStates(True, 1, 2, 3, 4)
        self.buttonsStates(False, 0)

    # After the roll_dice method has ended, this method will start
    def player_move(self, moves, double):
        current_player_turns = self.players[self.current_player].getAmount_of_turns()
        current_square = self.players[self.current_player].getCurrent_square()
        if current_square == 7 and self.players[self.current_player].isIn_jail() is True:  # Special squares
            if double:
                self.players[self.current_player].setJail(False)
                self.players[self.current_player].resetTurns()
            elif current_player_turns == 1 or current_player_turns == 2:
                self.players[self.current_player].addTurn()
            else:
                self.players[self.current_player].setJail(False)
                self.players[self.current_player].resetTurns()
                self.money_transaction_current_player(-100)
        else:  # Street squares
            square_num = current_square + moves
            if square_num == 28:
                self.money_transaction_current_player(400)
                square_num = 0
                self.buttonsStates(False, 1, 3)
            elif square_num > 28:
                self.money_transaction_current_player(200)
                square_num = square_num - 28
            elif square_num == 14 or square_num == 21:
                self.players[self.current_player].addTurn()
                self.buttonsStates(False, 1, 3)
                if square_num == 21:
                    self.players[self.current_player].setJail(True)
                    square_num = 7
            if self.squares[square_num].getOwned_by():
                self.money_transaction_current_player(-self.squares[square_num].getFine_price(),
                                                      self.squares[square_num].getOwned_by())  # Paying the fine price
                self.locatePlayer(self.players[self.current_player], square_num)
                self.end_turn()
            else:
                self.locatePlayer(self.players[self.current_player], square_num)

    # Money transaction to current player
    def money_transaction_current_player(self, money, player=None):
        money = int(money)
        if not self.moneyAvailability_current_player(money):
            height = self.getScreen_height()
            warning = tk.Label(self.getWindow(), text="You do'nt have enough money", font=(None, 16, 'bold'), fg="red")
            warning.place(x=0.3 * height, y=0.3 * height, height=0.05 * height, width=0.1 * height)
            warning.after(10000, warning.destroy)
            return False
        self.players[self.current_player].moneyTransaction(money)
        self.players_frames_stringVar_details[self.current_player]. \
            set(f'Name: {self.players[self.current_player].getName()} '
                f'Money: {self.players[self.current_player].getMoney()}')
        if player is not None:  # Fine money transaction
            player.moneyTransaction(-money)
            owner_loc = None
            for i in range(len(self.players)):
                if self.players[i] == player:
                    owner_loc = i
                    break
            self.players_frames_stringVar_details[owner_loc]. \
                set(f'Name: {self.players[owner_loc].getName()} '
                    f'Money: {self.players[owner_loc].getMoney()}')
        return True

    def moneyAvailability_current_player(self, money):
        return self.players[self.current_player].getMoney() + money >= 0

    # When pressing on "Show Card" button, this command will start
    def show_card(self):
        pass

    # When pressing on "End Turn" button, this command will start after end_turn command
    def end_show_card(self):
        pass

    # When pressing on "Buy" button, this command will start
    def buy(self):
        height = self.getScreen_height()
        houses_label = tk.Label(self.getBoard(), bg="DarkSeaGreen1", text="Houses:", font=("Times", "10", "bold"))
        houses_label.place(x=0.22 * height, y=0.35 * height, height=0.05 * height,
                           width=0.05 * height)  # Houses Label
        houses_variable = tk.StringVar()
        houses_variable.set(0)
        houses_options = tk.OptionMenu(self.getWindow(), houses_variable, 0, 1, 2, 3, 4)  # Houses Options menu
        houses_options.place(x=0.27 * height, y=0.35 * height, height=0.05 * height, width=0.05 * height)
        hotel_label = tk.Label(self.getBoard(), bg="DarkSeaGreen1", text="Hotel", font=("Times", "10", "bold"))
        hotel_label.place(x=0.32 * height, y=0.35 * height, height=0.05 * height, width=0.05 * height)  # Hotel Label
        hotel_variable = tk.StringVar()
        hotel_variable.set(0)
        hotel_options = tk.OptionMenu(self.getWindow(), hotel_variable, 0, 1)  # Houses Options menu
        hotel_options.place(x=0.37 * height, y=0.35 * height, height=0.05 * height, width=0.05 * height)
        buying_process_button = tk.Button(self.getBoard(), bg="white",
                                          font=("Times", "10", "bold"), text="Buy Now", command=self.buyingProcess)
        buying_process_button.place(x=0.45 * height, y=0.35 * height, height=0.05 * height, width=0.05 * height)
        self.buy_widgets = [houses_label, houses_options, houses_variable, hotel_label, hotel_options,
                            hotel_variable, buying_process_button]

    # The buying process
    def buyingProcess(self):
        houses, hotel = self.buy_widgets[2].get(), self.buy_widgets[5].get()
        total_price = 0
        if hotel:
            total_price = self.squares[self.players[
                self.current_player].getCurrent_square()].getBuying_or_fine_price(int(houses), 0, True)
        if houses:
            total_price = total_price + self.squares[self.players[self.current_player].getCurrent_square()]. \
                getBuying_or_fine_price(int(hotel), 1, True)
        if total_price > 0:  # If there are houses and hotels
            if self.money_transaction_current_player(-total_price):  # Money transaction is possible and it is executed
                self.squares[self.players[self.current_player].getCurrent_square()]. \
                    setOwned_by(self.players[self.current_player])
                self.squares[self.players[self.current_player].getCurrent_square()].setHouses(int(houses))
                self.squares[self.players[self.current_player].getCurrent_square()].setHotel(int(hotel))
                self.addHouses_frames(self.squares[self.players[self.current_player].getCurrent_square()])
                card = self.squares[self.players[self.current_player].getCurrent_square()] \
                    .card(self.players_cards_frames[self.current_player])
                x = self.players[self.current_player].getNext_card_x()  # Updating the next card location
                card.place(relx=x, rely=0)
                for i in range(7):  # Destroy the buy_Widgets
                    if i != 2 and i != 5:
                        self.buy_widgets[i].destroy()
                self.players[self.current_player].setNext_card_x(x + 0.25)

    # When player pressing on "Quit" button, this command will start
    def quit(self):
        self.players.remove(self.players[self.current_player])
        self.setPlayers_quantity(self.getPlayers_quantity() - 1)
        if len(self.players) == 1:
            self.end_game()
        pass

    # When pressing on "End Turn" button, this command will start
    def end_turn(self):
        self.in_turn = False
        last_player = self.current_player
        next_player = 0
        if self.current_player + 1 < len(self.players):
            next_player = self.current_player + 1
        while self.players[next_player].getCurrent_square() == 14:  # This loop is for the free_parking square
            if self.players[next_player].getAmount_of_turns() == 1:
                self.players[next_player].addTurn()
                if next_player + 1 < len(self.players):
                    next_player += 1
                else:
                    next_player = 0
            else:
                self.players[next_player].resetTurns()
        self.current_player = next_player
        self.updateCurrent_player_frame_color(last_player)
        self.end_show_card()
        self.buttonsStates(True, 0, 4)
        self.buttonsStates(False, 1, 2, 3)

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
            self.window.mainloop()


if __name__ == "__main__":
    game = Mygame()
    game.startGame()
