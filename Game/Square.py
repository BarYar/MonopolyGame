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
        self.characters = []
        super().__init__()

    # Sets the frame
    def setFrame(self, frame):
        self.frame = frame

    # Get the frame
    def getFrame(self):
        return self.frame

    # Adds character to characters list
    def addCharacter(self, player):
        self.characters.append(player)

    # Remove player from the characters list
    def removeCharacter(self, player):
        for i in range(len(self.characters)):
            if self.characters[i].getName() == player.getName():
                self.characters.remove(self.characters[i])
