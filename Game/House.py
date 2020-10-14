from Game.Displayable import Displayable


"""House class- 
   parameters: 
                1.typ:typ- 0= regualr house, 1=hotel (int)
   attributes:             
                1.inGame:True- the player is in game, False- the player is not in game(boolean)
                2.price_multiple: this attribbue is depended on the type of the house (float)
                3.height(int)
                4.width(int)

   """


class House(Displayable):
    # Constructor
    def __init__(self, typ):
        self.typ = typ
        self.in_game = False
        self.price_multiple = typ * 3.4 + 1
        if self.typ == 0:
            super().__init__(10, 30)  # Change for ratio!!!
        else:
            super().__init__(13, 37)  # Change for ratio!!!

    # Set the typ -0/1
    def setTyp(self, typ):
        self.typ = typ

    # Set the player in_game param
    def setIn_game(self, in_game):
        self.in_game = in_game

    # Set the player location
    def setLocation(self, location):
        self.location = location

    # Get the typ -0/1
    def getTyp(self):
        return self.typ

    # Get the player in_game param
    def getIn_game(self):
        return self.in_game

    # Get the player price_multiple
    def getPrice_multiple(self):
        return self.price_multiple