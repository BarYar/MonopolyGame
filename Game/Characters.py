import os
import random
from Game.Character import Character
from Game.Root import Root

""" Character_List class-
    parameters: 

   attributes:             
                1.names- List of all the available character names (List(string))
                2.pictures- List of all of the pictures locations(List(string))
                3.characters- List of all of the characters, 
                 this list composed by the names and pictures (List(Character(obj)))
    """


class Characters(Root):
    # Constructor
    def __init__(self):
        super().__init__()
        self.names = ["Superman", "Ironman", "Spiderman", "Batman", "Wonder Woman",
                      "Deadpool"]  # List of all of the character names
        self.pictures = os.listdir(f'{self.project_files_root}\Characters')
        self.characters = [Character(self.names[i], self.pictures[i]) for i in range(6)]

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
        character_loc = None
        for i in range(len(self.characters)):
            if self.characters[i].getCharacter_Name() == name:
                character_loc = i
        return self.characters.pop(character_loc)


    # Get random character name and picture
    def getRandom_character(self):
        num = random.randint(0, len(self.characters)-1)
        return self.get_character(self.names[num])

    # Returns the given amount of characters randomly - do The get_character "amount" times
    def get_random_characters(self, amount):
        characters = []
        for i in range(amount):
            characters.append(Character(self.getRandom_character()[0], self.getRandom_character()[1]))
        return characters



