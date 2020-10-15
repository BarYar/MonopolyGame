from Game.Square import Square


"""Go_to_jail class- Class for the Go_to_Jail square
   parameters: 
                1. x (float)
                2. y (float)
                3. picture- path to the picture of the square (string)

   attributes:             
                1.characters []- list of the characters that are on this square (List(Character(obj)))
                2.height (int)
                3.width (int)


   """


class Go_to_jail(Square):
    # Constructor
    def __init__(self, frame):
        Square.__init__(self, frame)
