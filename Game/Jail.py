from Game.Square import Square


"""Jail class- Class for the Jail square
   parameters: 
                1. x (float)
                2. y (float)
                3. picture- path to the picture of the square (string)

   attributes:             
                1. characters []- list of the characters that are on this square (List(Character(obj)))               
                2. fine- fine for getting out of jail (int)- default value-100
                3. height (int)
                4. width (int)


   """


class Jail(Square):
    # Constructor
    def __init__(self, picture,  x, y):
        self.fine = 100
        Square.__init__(self, picture,  x, y, 0.11, 0.16)  # Change for ratio!!!

    # Set the fine
    def setFine(self, fine):
        self.fine = fine

    # Get the fine
    def getFine(self):
        return self.fine
