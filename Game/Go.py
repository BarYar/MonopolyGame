from Game.Square import Square


"""Go class- Class for the Go square
   parameters: 
                1. x (float)
                2. y (float)
                3.picture- path to the picture of the square (string)
   attributes:             
                1.characters []- list of the characters that are on this square (List(Character(obj)))
                2.passing_through_go- the money that a player will get 
                    if he's passing through the go square (int)- default value = 200
                3.landing_on_go- the money that a player will get 
                    if he's landing on the go square (int)- default value = 400
                2. height (int) 
                3. width (int)


   """


class Go(Square):
    # Constructor
    def __init__(self, picture, x, y):
        Square.__init__(self, picture, x, y, 0.22, 0.16)  # Change for ratio!!!
        self.passing_through_go = 200
        self.landing_on_go = 400

    # Set the Passing_through_go
    def setPassing_through_go(self, passing_through_go):
        self.passing_through_go = passing_through_go

    # Get the Passing_through_go
    def getPassing_through_go(self):
        return self.passing_through_go

    # Set the landing_on_go
    def setLanding_on_go(self, landing_on_go):
        self.landing_on_go = landing_on_go

    # Get the landing_on_go
    def getLanding_on_go(self):
        return self.landing_on_go