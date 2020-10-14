from Game.Root import Root


""" Displayable class- Can be seen in the gui
    parameters: 
                1.height- the height of an object (float) 
                2.width- the width of an object (float) 
                3.x- the x axis location of an object (float) 
                4.y- the y axis location of an object (float) 
   attributes:             

    """


class Displayable(Root):
    # Constructor
    def __init__(self, height=None, width=None, x=None, y= None):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__()

    # Set the height
    def setheight(self, height):
        self.height = height

    # Set the width
    def setwidth(self, width):
        self.width = width

    # Set the x
    def setX(self, x):
        self.x = x

    # Set the y
    def setY(self, y):
        self.y = y

    # Returns the height
    def getheight(self):
        return self.height

    # Returns the width
    def getwidth(self):
        return self.width

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