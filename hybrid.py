#hybrid

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} make a sound")

class Mammal(Animal):
    def feed(self):
        print("Feeds milk to babies")
        
class Bird(Animal):
    def fly(self):
        print("Can fly")

class Bat(Mammal,Bird):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print(f"{self.name} the bat screeches")

bat=Bat("Batty")
bat.speak()
bat.feed()
bat.fly()

