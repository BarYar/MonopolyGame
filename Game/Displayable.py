import ctypes
import os

""" Displayable class- Can be seen in the gui
    parameters: 
                1.height- the height of an object (float) 
                2.width- the width of an object (float) 
                3.x- the x axis location of an object (float) 
                4.y- the y axis location of an object (float) 
                5. screen_width - The width of the screen.
                6. screen_height - The height of the screen.
                7.project_root- the path of the project (string) 
                8.project_files_root- the path of the files directory of the project,
                 the pictures and the text files of this project are in this directory.(string)  
   attributes:             

    """


class Displayable:
    # Constructor
    def __init__(self, height=None, width=None, x=None, y=None):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        user32 = ctypes.windll.user32
        self.screen_width = user32.GetSystemMetrics(0)
        self.screen_height = user32.GetSystemMetrics(1)
        self.project_root = os.path.dirname(os.path.dirname(__file__))
        self.project_files_root = f'{self.project_root}\Files'
        super().__init__()

    # Set the height
    def setHeight(self, height):
        self.height = height

    # Set the width
    def setWidth(self, width):
        self.width = width

    # Set the x
    def setX(self, x):
        self.x = x

    # Set the y
    def setY(self, y):
        self.y = y

    # Returns the height
    def getHeight(self):
        return self.height

    # Returns the width
    def getWidth(self):
        return self.width

    # Get the screen_height
    def getScreen_height(self):
        return self.screen_height

    # Get the screen_width
    def getScreen_width(self):
        return self.screen_width

    # Get project root
    def getProject_root(self):
        return self.project_root

    def getProject_files_root(self):
        return self.project_files_root

    # Returns the x
    def getX(self):
        return self.x

    # Returns the y
    def getY(self):
        return self.y

    # Returns the area of an objects
    def getArea(self):
        return self.width * self.height

    # repr function for Size class
    def __repr__(self):
        return f'His height is: {self.height}, his width is: {self.width}, His x is: {self.x}, his y is: {self.y} '
