from Game.Board import Board
from Game.Player import Player
from Game.Characters import Characters

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
                7. screen_width - The width of the screen.
                8. screen_height - The height of the screen.
                9. window - the window of the game (Tkinter(obj)).
                10. board - the frame of the board in the window (Tkinter(obj)).
                11. squares - The list of the squares (List(Tkinter(obj))
                12. loc - The pointer of the words (int). - default value = 0 
                13. words - The list of the squares details strings (List(string))

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

    # Adds the player to the players list
    def addPlayer(self, player):
        self.players.append(player)

    # Set the in_game
    def setIn_game(self, in_game):
        self.in_game = in_game

    # Set the in_turn
    def setIn_turn(self, in_turn):
        self.in_turn = in_turn

    # Start new game
    def newGame(self):
        self.startScreen()
        self.players_personal_inforamtion()
        self.create_squares()
        self.create_players_frame()
        self.createTitle()
        self.createButtons()
        self.locatePlayers()

    # The players enter their names and choose their character
    def players_personal_inforamtion(self):
        pass

    # The start screen - welcome label and buttons for choosing players quantity
    def startScreen(self):
        pass

    # Create the players details frames.
    def create_players_frame(self):
        pass

    # Create the game buttons
    def createButtons(self):
        self.setButtons_disabled()
        pass

    # Create the game title- Monopoly and Monopoly sign in the middle of the board
    def createTitle(self):
        pass

    # Locate the players on the first square
    def locatePlayers(self):
        pass

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
        self.player_move()
        pass

    # After the roll_dice method has ended, this method will start
    def player_move(self):
        pass

    # When pressing on "Show Card" button, this command will start
    def show_card(self):
        pass

    # When pressing on "Buy" button, this command will start
    def buy(self):
        pass

    # When player pressing on "Quit" button, this command will start
    def quit(self):
        self.players.remove(self.players[self.current_player])
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
        self.players = ["", "", "", "" ]
        while self.in_game:
            self.setRoll_dice_enabled()
            self.window.mainloop()


if __name__ == "__main__":
    game = Mygame()
    game.startGame()
