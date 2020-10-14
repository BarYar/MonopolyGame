from Game.Square import Square


"""Street class- class for the Street square
   parameters: 
                1. city - The city of the square- if it's a special square, this will be the square title (string)
                2. street - The address of the square- if it's a special square, this will be the square details (string)
                3. land_price - The land price of the square- if it's a special square, it's value = 0 (int)
                4. picture- path to the picture of the square (string)
                5. x(int)
                6. y(int)
   attributes:             
                1. houses []- list of this square's houses (List(house(obj)))
                2. hotel - this square's hotel (House(obj)) - default value None 
                3. characters []- list of the characters that are on this square (List(Character(obj)))
                4. buying []- the buying prices of this square (1-4 houses, 1 hotel)
                5. fines []- the fines prices of this square (1-4 houses, 1 hotel)
                6. height(int)
                7. width(int)

   """


class Street(Square):
    # Constructor
    def __init__(self, city, street, land_price, picture, x, y):
        self.city = city
        self.street = street
        self.land_price = land_price
        self.houses = []
        self.hotel = None
        self.card()
        Square.__init__(self, picture, x, y, 0.11, 0.8)  # Change for ratio!!!

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
        self.buying = [self.get_buying_or_fine_price(i, 0, True) for i in range(1 ,5)]
        self.buying.append(self.get_buying_or_fine_price(1, 1, True))
        self.fines = [self.get_buying_or_fine_price(i, 0, False) for i in range(1 ,5)]
        self.fines.append(self.get_buying_or_fine_price(1, 1, False))
        return self.buying, self.fines