# BROCODE
# First we make a class as a blueprint that states what are our objects attributes ( what object is, what object has)
# And te methods ( actions ) that our object does
# class names start with capital letters

class Car:

    #make: None
    #model: None
    #year: None
    #color: None

    # we use __init__ to define attributes for our object cars

    def __init__(self, make, model, year, color):
        self.make= make
        self.model=model
        self.year=year
        self.color= color


# we use SELF and it refers to the object itself

    def drive(self):
        print(f"{self.make}{self.model}{self.year}{self.color} is driving!")

    def stop(self):
        print(f"{self.make}{self.model}{self.year}{self.color} is stopped!")