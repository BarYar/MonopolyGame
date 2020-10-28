from Game.Displayable import Displayable


"""Square class- 
   parameters: 
                1. picture- The frame of the square (Tkinter(obj))
                2.height- the height of an object (float) 
                3.width- the width of an object (float) 
                4.x- the x axis location of an object (float) 
                5.y- the y axis location of an object (float) 
   attributes:             
                1. characters []- list of the characters that are on this square (List(Character(obj)))
   """


class Square(Displayable):
    # Constructor
    def __init__(self, frame):
        self.frame = frame
        self.players = []
        self.owned_by = None
        super().__init__()

    # Sets the frame
    def setFrame(self, frame):
        self.frame = frame

    # Get the frame
    def getFrame(self):
        return self.frame

    # Get owned_by- return None automatically
    def getOwned_by(self):
        return self.owned_by

    # Adds player to characters list, and set his x and y to square x and y
    def addPlayer_square(self, player):
        self.players.append(player)
        height = self.getScreen_height()
        # Locating the players
        if len(self.players) % 2 != 0:
            player.setX(self.getX() + int(height/30))
            player.setY(self.getY() + int(height / 30) + (((len(self.players) - 1) / 2) * 0.03 * height))
        else:
            player.setX(self.getX() + int(height/30) + height * 0.04)
            player.setY(self.getY() + int(height/30) + (((len(self.players) - 2)/2) * 0.03 * height))
        player.setHeight(int(0.028 * height))
        player.setWidth(int(0.028 * height))

    # Get the players list
    def getPlayers(self):
        return self.players

    # Remove player from the characters list
    def removePlayer(self, player):
        for i in range(len(self.players)):
            if self.players[i].getName() == player.getName():
                self.players.remove(self.players[i])
