#!/usr/bin/python3

class Car():
    # (1) Why we need this "self" crap? See below ... :-)
    def exclaim(self):
        print("I'm a car!")

    def __init__(self, name):
        # (2) access "name" attribute inside of class (generic object)
        self.name = name

car = Car(name="Mater")
car.exclaim()
# (1) -> this is what Python actually does
Car.exclaim(car)

# (2) access "name" attribute outside of class (specifi object)
print(car.name)
