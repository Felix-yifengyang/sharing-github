class Restaurant() :
    def __init__(self, name, type) :
        self.name = name
        self.type = type
        self.number_serve = 0
    def describe_restaurant(self) :
        print(f"The restaurant is {self.name}")
        print(f"The type is {self.type}")
    def open_restaurant(self) :
        print("Opening")
    def increment_number_served(self) :
        self.number_serve += 1
class IceCreamStand(Restaurant) :
    def __init__(self, name, type, flavors = ['chocolate']) :
        super.__init__(name, type)
    def Showflavor(self) :
        print(self.flavors)
my_icecream = IceCreamStand('Shit','Icecream')
my_icecream.Showflavor( )