import os
import random

"""class with the root location-for pictures and files"""


class root:
    # Constructor
    def __init__(self):
        self.project_root = os.path.dirname(os.path.dirname(__file__))
        self.project_files_root = f'{self.project_root}\Files'


""" size of on object- for on screen objects"""


class Size(root):
    # Constructor
    def __init__(self, height, length):
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


""" location of on object- for on screen objects"""


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


""" Character class- each character has a picture a name and a location """


class Character(Location,Size):
    # Constructor
    def __init__(self, name, picture, x=None, y=None):
        self.name = name
        self.picture = picture
        Location.__init__(self,x, y)
        Size.__init__(self, 15, 15)#Change for sqale!!!

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
    holds a list of all the available characters"""


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


"""Player class- each player has a name, money, Character and houses[] """


class Player(Location):
    # Constructer- gets name,money ,character and location
    def __init__(self, name, money, character, x=0, y=0):
        self.name = name
        self.money = money
        self.character = character
        self.hotels = []
        self.houses = []
        super().__init__(x, y)

    # Set the name
    def setName(self, name):
        self.name = name

    # Set the money
    def setMoney(self, money):
        self.money = money

    # Set the character
    def setCharacter(self, character):
        self.character=character

    # Returns the name
    def getX(self):
        return self.name

    # Returns the money
    def getY(self):
        return self.money

    # Returns the character
    def getCharacter(self):
        return self.character

    # Set the houses for a player (default value-3 Hotels, 5 Regular)
    def setHouses(self,amount=(5,3)):
        for i in range(amount(0)):#Sets the regular houses
            self.houses.append(House(0))
        for i in range(amount(1)):#Sets the hotels
            self.hotels.append(House(1))

    # Reduce/Increase the money of a player
    def money_transaction(self,price):
        self.money=self.money+price


"""House class- 
   parameters: 
                1.type:type- 0= regualr house, 1=hotel (int)
   attributes:             
                1.location-location of the house can be none (Location)
                2.inGame:True- the player is in game, False- the player is not in game(boolean)
                3.price_multiple: this attribbue is depended on the type of the house (float)
                4.height(int)
                5.length(int)
   """


class House(Size):
    # Constructor
    def __init__(self, type):
        self.type=type
        self.in_game = False
        self.price_multiple = type + 0.9
        self.location=None
        if self.type == 0:
            super().__init__(10, 30)#Change for sqale!!!
        else:
            super().__init__(13, 37)#Change for sqale!!!

    # Set the type -0/1
    def setType(self, type):
        self.type = type

    # Set the player in_game param
    def setIn_game(self, in_game):
        self.in_game = in_game

    # Set the player location
    def setLocation(self, location):
        self.location = location

    # Get the type -0/1
    def getType(self):
        return self.type

    # Get the player in_game param
    def getIn_game(self):
        return self.in_game

    # Get the player price_multiple
    def getPrice_multiple(self):
        return self.price_multiple


"""Square class- 
   parameters: 
                1.city (string)
                2.street (string)
                3.land_price (int)
                4.x(int)
                5.y(int)
   attributes:             
                1.houses []- house (obj)
                2.height(int)
                3.length(int)
                
   """


class Square(Size,Location):
    # Constructor
    def __init__(self, city, street, land_price, x, y):
        self.city=city
        self.street=street
        self.land_price=land_price
        Size.__init__(self, 60, 60)#Change for sqale!!!
        Location.__init__(self, x, y)

    # Set the city
    def setCity(self, city):
        self.city = city

    # Set the street
    def setStreet(self, street):
        self.street = street

    # Set the land_price
    def setLand_price(self, land_price):
        self.land_price = land_price

    # Get the city
    def getCity(self):
        return self.city

    # Get the street
    def getStreet(self):
        return self.street

    # Get the land_price
    def getLand_price(self):
        return self.land_price

    # get the fine price for landing on the square
    def getFine_price(self):








