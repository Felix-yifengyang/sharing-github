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
# restaurant1 = Restaurant('大家乐','粤菜')
# restaurant2 = Restaurant('Mcdonald','chicken')
# restaurant3 = Restaurant('KFC','chicken')
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

restaurant = Restaurant('Itamomo','Italy')
print(f"{restaurant.number_serve}")
restaurant.increment_number_served()
print(f"{restaurant.number_serve}")