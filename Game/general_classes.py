import os
import random

""" root class-
    parameters: 

   attributes:             
                1.project_root- the path of the project (string) 
                2.project_files_root- the path of the files directory of the project,
                 the pictures and the text files of this project are in this directory.(string)  
    """


class root:
    # Constructor
    def __init__(self):
        self.project_root = os.path.dirname(os.path.dirname(__file__))
        self.project_files_root = f'{self.project_root}\Files'


""" Size class-
    parameters: 
                1.height- the height of an object (float) 
                2.length- the length of an object (float) 
   attributes:             
                
    """


class Size(root):
    # Constructor
    def __init__(self, height=None, length=None):
        self.height = height
        self.length = length
        super().__init__()

    # Set the height
    def setHeight(self, height):
        self.height = height

    # Set the length
    def setLength(self, length):
        self.length = length

    # Returns the height
    def getHeight(self):
        return self.height

    # Returns the length
    def getLength(self):
        return self.length

    # Returns the area of an objects
    def getArea(self):
        return self.length * self.height

    # repr function for Size class
    def __repr__(self):
        return f'His Height is: {self.height}, his length is: {self.length}'


""" Location class-
    parameters: 
                1.x- the x axis location of an object (float) 
                2.y- the y axis location of an object (float) 
   attributes:             
                
    """


class Location:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Set the x
    def setX(self, x):
        self.x = x

    # Set the y
    def setY(self, y):
        self.y = y

    # Returns the x
    def getX(self):
        return self.x

    # Returns the y
    def getY(self):
        return self.y

    # repr function for Location class
    def __repr__(self):
        return f'His x is: {self.x}, his y is: {self.y}'


""" Character class-
    parameters: 
                1.name- The name of the character (string) 
                2.picture- The picture of the character location (string) 
                3.x (float) - default value=None
                4.y (float) - default value=None
   attributes:             
                1.height (int)
                2.weight (int)
    """


class Character(Location, Size):
    # Constructor
    def __init__(self, name, picture, x=None, y=None):
        self.name = name
        self.picture = picture
        Location.__init__(self, x, y)
        Size.__init__(self, 15, 15)  # Change for sqale!!!

    # Set the name
    def setName(self, name):
        self.name = name

    # Set the picture
    def setPicture(self, picture):
        self.picture = picture

    # Returns the name
    def getName(self):
        return self.name

    # Returns the picture
    def getPicture(self):
        return self.picture

    # repr function for Size class
    def __repr__(self):
        return f'Character name is: {self.name}'


""" Character_List class-
    parameters: 
                
   attributes:             
                1.names- List of all the available character names (List(string))
                2.pictures- List of all of the pictures locations(List(string))
                3.characters- List of all of the characters, 
                 this list composed by the names and pictures (List(Character(obj)))
    """


class Character_List(root):
    # Constructor
    def __init__(self):
        self.names = ["Superman", "Ironman", "Spiderman", "Batman", "Wonder Woman",
                      "Deadpool"]  # List of all of the character names
        self.pictures = os.listdir(f'{self.project_files_root}\Characters')
        self.characters = [Character(self.names[i], self.pictures[i]) for i in range(6)]
        super().__init__()

    # Returns The available characters
    def get_available_characters(self):
        return self.names

    # Returns the given character, and remove it from the lists
    """ Possible error- might not update the pics and name lists"""

    def get_character(self, name):
        if name not in self.names:  # Check if the name is valid
            raise ValueError("Invalid name")
        # Possible code
        # loc=self.listOfNames.index(name)
        # self.listOfNames.remove(name)
        # self.listOfPics.remove(loc)
        Character = None
        for i in range(len(self.characters)):
            if (self.characters[i].getName() == name):
                Character = self.characters[i]
        return self.characters.remove(Character)

    # Returns the given amount of characters randomly - do The get_character "amount" times

    def get_random_characters(self, amount):
        characters = []
        for i in range(amount):
            characters.append(self.get_character(self.names[random.randint(len(self.names))]))
        return characters


"""House class- 
   parameters: 
                1.typ:typ- 0= regualr house, 1=hotel (int)
   attributes:             
                1.location-location of the house can be none (Location)
                2.inGame:True- the player is in game, False- the player is not in game(boolean)
                3.price_multiple: this attribbue is depended on the type of the house (float)
                4.height(int)
                5.length(int)
   """


class House(Size):
    # Constructor
    def __init__(self, typ):
        self.typ = typ
        self.in_game = False
        self.price_multiple = typ * 3.4 + 1
        self.location = None
        if self.typ == 0:
            super().__init__(10, 30)  # Change for sqale!!!
        else:
            super().__init__(13, 37)  # Change for sqale!!!

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


"""Houses class- 
   parameters: 

   attributes:             
                1.hotels - The player's hotels (List(House (obj)))
                1.houses - The player's regular houses (List(House (obj)))

   """


class Houses:
    # Constructor set the houses for a player (default value-3 Hotels, 5 Regular)
    def __init__(self, amount=(5, 3)):
        self.houses = [House(0) for i in range(amount(0))]  # Sets the regular houses
        self.hotels = [House(1) for i in range(amount(1))]  # Sets the hotels


"""Square class- 
   parameters: 
                1.name - The player name (string)
                2.money - The player money (float) - can't be negative
                3.character- The player character (Character(obj))
                4.x(int) -optional
                5.y(int) -optional
   attributes:             
                1.jail- True- the player is in jail
                 False- the player is'nt in jail (boolean)
                
   """


class Player(Location, Houses):
    # Constructor- gets name,money ,character and location
    def __init__(self, name, money, character, x=0, y=0):
        self.name = name
        self.money = money
        self.character = character
        self.jail = False
        Location.__init__(self, x, y)
        Houses.__init__(self)

    # Set the name
    def setName(self, name):
        self.name = name

    # Set the money
    def setMoney(self, money):
        self.money = money

    # Set the character
    def setCharacter(self, character):
        self.character = character

    # Set the jail parameter to True/False
    def setJail(self, jail):
        self.jail = jail

    # Returns the name
    def getX(self):
        return self.name

    # Returns the money
    def getY(self):
        return self.money

    # Returns the character
    def getCharacter(self):
        return self.character

    # Returns if the player is in jail
    def isIn_jail(self):
        return self.jail

    # Reduce/Increase the money of a player
    def money_transaction(self, price):
        self.money = self.money + price


"""Square class- 
   parameters: 
                1.x(int)
                2.y(int)
   attributes:             
                1.height(int)
                2.length(int)

   """


class Square(Size, Location):
    # Constructor
    def __init__(self, x, y):
        Size.__init__(self)  # Change for sqale!!!
        Location.__init__(self, x, y)


"""Street class- 
   parameters: 
                1.city - The city of the square- if it's a special square, this will be the square title (string)
                2.street - The address of the square- if it's a special square, this will be the square details (string)
                3.land_price - The land price of the square- if it's a special square, it's value = 0 (int)
                4.x(int)
                5.y(int)
   attributes:             
                1.houses []- house (obj)
                2.height(int)
                3.length(int)
                
   """


class Street(Square):
    # Constructor
    def __init__(self, city, street, land_price, x, y):
        self.city = city
        self.street = street
        self.land_price = land_price
        self.houses = []
        self.hotel = None
        self.card()
        Square.__init__(self, x, y)

    # Set the city
    def setCity(self, city):
        self.city = city

    # Set the street
    def setStreet(self, street):
        self.street = street

    # Set the land_price
    def setLand_price(self, land_price):
        self.land_price = land_price

    # Add the {houses} to self.houses
    # parameters:
    #               1.houses
    def addHouses(self, houses):
        for i in houses:
            self.houses.append(i)

    # Set the hotel to hotel
    # parameters:
    #               1.hotel
    def addHotel(self, hotel):
        self.hotel = hotel

    # Get the city
    def getCity(self):
        return self.city

    # Get the street
    def getStreet(self):
        return self.street

    # Get the land_price
    def getLand_price(self):
        return self.land_price

    # Get the Houses
    def getHouses(self):
        return self.houses

    # Remove all the houses from the list
    # It will happen mostly when a player wants to upgrade to hotel
    def clearHouses(self):
        self.houses = []

    # Remove all the houses and hotel from the object
    # It will happen mostly when a player quit/ lost
    def clearHouses_and_hotel(self):
        self.houses = []
        self.hotel = None

    # Get the fine price for landing on the square
    def getFine_price(self):
        sum_multiple = len(self.houses)
        if self.hotel:  # Checks if hotel is in the square
            sum_multiple = 4.4
        return self.land_price * sum_multiple

    # Get the fine or buying price
    # Get the price of the square with {amount} of houses from {typ} type
    # parameters:
    #               1.amount (int)
    #               2.typ 0/1 (int)
    #               3.payment True/False(boolean
    def get_buying_or_fine_price(self, amount, typ, payment):
        sum_price = 0
        payment_multiple = 1
        if payment:
            payment_multiple = 1.7
        if type(amount) == int and type(typ) == int:
            if amount > 0:
                if typ == 0:
                    if amount < 4:
                        sum_price = amount * self.land_price * payment_multiple
                    else:
                        raise ValueError("Invalid amount for house")
                elif typ == 1:
                    if amount < 1:
                        sum_price = self.land_price * 4.4 * payment_multiple * 1.15
                    else:
                        raise ValueError("Invalid amount for hotel")
                else:
                    raise ValueError("Invalid typ number")
        else:
            raise TypeError(f"Yo've entered a {type(typ)} type- non int type")
        return sum_price

    # Get the square card -payment and fine price for each of the available houses.
    # buying[0]-list of all the houses buying price, buying [1] - buying price of the hotel.
    # fines[0]-list of all the houses fines price, buying [1] - fines price of the hotel.
    def card(self):
        self.buying = [self.get_buying_or_fine_price(i, 0, True) for i in range(1,5)]
        self.buying.append(self.get_buying_or_fine_price(1, 1, True))
        self.fines = [self.get_buying_or_fine_price(i, 0, False) for i in range(1,5)]
        self.fines.append(self.get_buying_or_fine_price(1, 1, False))
        return self.buying, self.fines


"""Jail class- 
   parameters: 
                1. x (float)
                2. y (float)
   attributes:             
                1.players (List(Player(obj))
                2.height(int)
                3.length(int)

   """


class Jail(Square):
    # Constructor
    def __init__(self, x, y):
        Square.__init__(self, x, y)
        self.players= []

    # Adds player to players list
    def addPlayer(self, player):
        self.players.append(player)

    # Remove player from the players list
    def removePlayer(self, player):
        for i in range(len(self.players)):
            if i.getName() == player.getName():
                self.players.remove(self.players[i])


"""Squares class- 
   parameters: 
                
   attributes:             
                1.squares []- Square (obj)
                
   """


class Squares(root):
    # Constructor
    def __init__(self):
        self.squares=[]
        x = False  # var for the axis of change
        for i in range(6):
            with open("../Files/Cities/Tel-Aviv.txt", "r") as text:  # The text files that contains Tel-Aviv details
                words=text.read().split()  # Getting it's values
                self.squares.append(Square("Tel-Aviv", words[i*2], int(words[i*2+1]), -10-i*120, 10))  # Scaling!
            with open("../Files/Cities/Jerusalem.txt", "r") as text:  # The text files that contains Jerusalem details
                words = text.read().split()  # Getting it's values
                self.squares.append(Square("Jerusalem", words[i*2], int(words[i*2+1]), -10 - i * 120, 10))  # Scaling!
            if i < 4:
                with open("../Files/Cities/Haifa.txt", "r") as text:  # The text files that contains Haifa details
                    words = text.read().split()  # Getting it's values
                    self.squares.append(Square("Haifa", words[i*2], int(words[i*2 + 1]), -10, 130 + i * 120))  # Scaling!
                with open("../Files/Cities/Beer-Sheva.txt", "r") as text:  # The text files that contains Beer-Sheva details
                    words = text.read().split()  # Getting it's values
                    self.squares.append(Square("Beer-Sheva",  words[i*2], int(words[i*2 + 1]), -610, 130 + i * 120))  # Scaling!
        super().__init__()
        
    # Get the squares list
    def getSquares(self):
        return self.squares
