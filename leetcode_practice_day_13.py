# Car Information System

# Create a Python program that:
# 1. Defines a class named Car.
class car:

# 2. Uses __init__() to receive brand, model, and year.
    def __init__(self,brand,model,year):
# 3. Stores these values using self.
        self.model = model
        self.year = year
        self.brand = brand
# 4. Creates a method named display_info() to print the car's details.
    def display_info(self):
        print("\nmodel: ",self.model)
        print("year :",self.year)
        print("brand :",self.brand)
# 5. Creates two different car objects.

car1= car("toyota","corolla",2010)
car2= car("kia","sportage",2019)
# 6. Calls display_info() for both objects.
car1.display_info()
car2.display_info()