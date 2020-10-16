from Game.House import House


"""Houses class- 
   parameters: 

   attributes:             
                1.hotels - The player's hotels (List(House (obj)))
                2.houses - The player's regular houses (List(House (obj)))

   """


class Houses:
    # Constructor set the houses for a player (default value-3 Hotels, 5 Regular)
    def __init__(self, amount=(5, 3)):
        self.houses = [House(0) for i in range(amount[0])]  # Sets the regular houses
        self.hotels = [House(1) for i in range(amount[1])]  # Sets the hotels

    # Sets the houses number to {amount}
    def setHouses(self, amount):
        self.houses = [House(0) for i in range(amount(0))]  # Sets the regular houses

    # Sets the houses number to {amount}
    def setHotels(self, amount):
        self.hotels = [House(1) for i in range(amount(1))]  # Sets the hotels

    # Removes an house from the list and returns it.
    def removeHouse(self):
        return self.houses.pop()

    # Removes an house from the list and returns it.
    def removeHotel(self):
        return self.hotels.pop()
