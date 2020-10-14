from Game.Displayable import Displayable


"""Square class- 
   parameters: 
                1. x(int)
                2 .y(int)
                3. picture- path to the picture of the square (string)
                4. height(int)
                5. width(int)
   attributes:             
                1. characters []- list of the characters that are on this square (List(Character(obj)))
   """


class Square(Displayable):
    # Constructor
    def __init__(self, picture, x, y, height, width):
        self.picture = picture
        Displayable.__init__(self, height, width, x, y)  # Change for ratio!!!
        self.characters = []

    # Sets the picture path
    def setPicture(self, picture):
        self.picture = picture

    # Get the picture path
    def getPicture(self):
        return self.picture

    # Adds character to characters list
    def addCharacter(self, player):
        self.characters.append(player)

    # Remove player from the characters list
    def removeCharacter(self, player):
        for i in range(len(self.characters)):
            if self.characters[i].getName() == player.getName():
                self.characters.remove(self.characters[i])