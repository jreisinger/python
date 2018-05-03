#!/usr/bin/python3

class Car():
    # (A) Why we need this "self" crap? See (A) below ... :-)
    def exclaim(self):
        print("I'm a car!")

    def __init__(self, name):
        # (B) access "name" attribute inside of class (generic object)
        self.name = name

car = Car(name="Mater")
car.exclaim()
# (A) -> this is what Python actually does
Car.exclaim(car)

# (B) access "name" attribute outside of class (specific object)
print(car.name)
