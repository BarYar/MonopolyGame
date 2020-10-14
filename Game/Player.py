from Game.Houses import Houses
from Game.Character import Character


"""Player class- 
   parameters: 
                1.name - The player name (string)
                2.money - The player money (float) - can't be negative
                3.character_name- The name of the character (string) 
                4.character_picture- The picture of the character location (string) 
                5.x (float) - default value=None
                6.y (float) - default value=None
   attributes:             
                1.jail- True- the player is in jail, False- the player is'nt in jail (boolean)
                2.hotels - The player's hotels (List(House (obj)))
                3.houses - The player's regular houses (List(House (obj)))
                4.height (int)
                5.width (int)
                
   """


class Player(Houses, Character):
    # Constructor- gets name,money ,character and location
    def __init__(self, name, money, character_name, character_picture):
        self.name = name
        self.money = money
        self.jail = False
        self.amount_of_turns = 1
        Houses.__init__(self)
        Character.__init__(self, character_name, character_picture)

    # Set the name
    def setName(self, name):
        self.name = name

    # Set the money
    def setMoney(self, money):
        self.money = money

    # Set the jail parameter to True/False
    def setJail(self, jail):
        self.jail = jail

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

    # Get the money
    def getAmount_of_turns(self):
        return self.amount_of_turns

    # Returns if the player is in jail
    def isIn_jail(self):
        return self.jail

    # Reduce/Increase the money of a player
    def money_transaction(self, price):
        self.money = self.money + price
