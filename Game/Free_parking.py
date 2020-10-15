from Game.Square import Square


"""Free_parking class- Class for the Go_to_Jail square
   parameters: 
                1. x (float)
                2. y (float)
                3. picture- path to the picture of the square (string)

   attributes:             
                1.characters []- list of the characters that are on this square (List(Character(obj)))
                2. height (int)
                3. width (int)


   """


class Free_parking(Square):
    # Constructor
    def __init__(self, frame):
        self.turns = 2
        Square.__init__(self, frame)
