from Game.Displayable import Displayable


""" Character class-
    parameters: 
                1.character_name- The name of the character (string) 
                2.character_picture- The picture of the character location (string) 
                3.x (float) - default value=None
                4.y (float) - default value=None
   attributes:             
                1.height (int)
                2.width (int)
    """


class Character(Displayable):
    # Constructor
    def __init__(self, character_name=None, character_picture=None, character=None, x=None, y=None):
        if character_name and character_picture:
            self.character_picture = character_picture
            self.character_name = character_name
        else:
            self.character_name = character.getCharacter_Name()
            self.character_picture = character.getCharacter_picture()
        super().__init__(15, 15, x, y)  # Change for ratio!!!

    # Set the name
    def setCharacter_name(self, name):
        self.name = name

    # Set the picture
    def setCharacter_Picture(self, picture):
        self.picture = picture

    # Returns the name
    def getCharacter_Name(self):
        return self.character_name

    # Returns the picture
    def getCharacter_picture(self):
        return self.character_picture

    # repr function for Size class
    def __repr__(self):
        return f'Character name is: {self.character_name},  its picture is:{self.character_picture}'
