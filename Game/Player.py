from Game.Houses import Houses
from Game.Character import Character


"""Player class- 
   parameters: 
                1.name - The player name (string)
                2.money - The player money (float) - can't be negative
                3.The character of the player.
                4.x (float) - default value=None
                5.y (float) - default value=None
   attributes:             
                1.jail- True- the player is in jail, False- the player is'nt in jail (boolean)
                2.hotels - The player's hotels (List(House (obj)))
                3.houses - The player's regular houses (List(House (obj)))
                4.height (int)
                5.width (int)
                
   """


class Player(Houses, Character):
    # Constructor- gets name,money ,character and location
    def __init__(self, name, money, character):
        self.name = name
        self.money = money
        self.jail = False
        self.amount_of_turns = 0
        self.streets = []
        self.current_square = 0
        self.color = None
        Houses.__init__(self)
        Character.__init__(self, None, None, character)

    # Set the name
    def setName(self, name):
        self.name = name

    # Set the money
    def setMoney(self, money):
        self.money = money

    # Set the jail parameter to True/False
    def setJail(self, jail):
        self.jail = jail

    # Set the current square
    def setCurrent_square(self, current_square):
        self.current_square = current_square

    # Set the color
    # Until the character update
    def setColor(self, color):
        self.color = color

    # Add a street to list of streets
    def addStreet(self, street):
        self.streets.append(street)

    # Add 1 turn to amount_of_turns
    def addOne_turn(self):
        self.amount_of_turns += 1

    # Reset the amount of turns to 1
    def resetTurns(self):
        self.amount_of_turns = 1

    # Get the name
    def getName(self):
        return self.name

    # Get the money
    def getMoney(self):
        return self.money

    # Get the color
    # Until the character update
    def getColor(self):
        return self.color

    # Get the money
    def getAmount_of_turns(self):
        return self.amount_of_turns

    # Get the streets
    def getStreets(self):
        return self.streets

    # Get the current square
    def getCurrent_square(self):
        return self.current_square

    # Returns if the player is in jail
    def isIn_jail(self):
        return self.jail

    # Reduce/Increase the money of a player
    def moneyTransaction(self, price):
        self.money = self.money + price
