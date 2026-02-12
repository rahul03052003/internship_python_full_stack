#Hierarchical

class vehicle:
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print(f"Brand: {self.brand}")
        
class car(vehicle):
    def wheels(self):
        print("Car has 4 wheels")
        
class bike(vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

c=car("Toyota")
b=bike("Honda")
c.display()
c.wheels()
b.display()
b.wheels()
