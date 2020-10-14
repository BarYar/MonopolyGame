from Game.Board import Board
from Game.Player import Player


"""Game class- 
   parameters: 

   attributes:             
                1. players [] - List of the players that are in the game (List(Player(obj))).
                2. game_money - The amount  of money that every player gets when the game starts (int).
                    - default value=5000
                3. screen_width - The width of the screen.
                4. screen_height - The height of the screen.
                5. window - the window of the game (Tkinter(obj)).
                6. board - the frame of the board in the window (Tkinter(obj)).
                7. squares - The list of the squares (List(Tkinter(obj))
                8. loc - The pointer of the words (int). - default value = 0 
                9. words - The list of the squares details strings (List(string))

   """


class Game(Board):
    #  Constructor
    def __init__(self):
        super().__init__()
        self.players = []
        self.game_money = 5000

    # Get the game_money
    def getGame_money(self):
        return self.game_money

    # Get the players list
    def getPlayers(self):
        return self.players

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