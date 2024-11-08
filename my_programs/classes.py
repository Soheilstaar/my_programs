

# a class is defined to create objects
class Vehicle:
    # now we define what is done in our class
    # we use initializer module to define parameters for our class
    def __init__(self, make, model):
        self.make=make
        self.model=model

    def moves(self):
        print('Moves along..')

# here we introduce an object
# my_car is an object that we created from the class Vehicle

my_car = Vehicle('Ford','Fusion')
print(my_car.make)
print(my_car.model)
my_car.moves()
##########################################################################
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

class Vehicle:
    
    def __init__(self, make, model):
        self.make=make
        self.model=model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f" I'm a ",self.make,self.model)


my_car = Vehicle('Ford','Fusion')
#print(my_car.make)
#print(my_car.model)
my_car.get_make_model()
my_car.moves()

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

# Now we create two objects for Vehicle class

class Vehicle:
    
    def __init__(self, make, model):
        self.make=make
        self.model=model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a ",self.make,self.model)


my_car = Vehicle('Ford','Fusion')
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Toyota','Prado')
your_car.get_make_model()
your_car.moves()

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

# now we make other classes that use the inits in Vehicle class

class Airplane (Vehicle):
    def moves(self):
        print('Flies along..')


class Truck (Vehicle):
    def moves(self):
        print('Rumbles along..')

class Golfcart (Vehicle):
    # pass means it inherits the original moves from the Vehicle class
    pass

boeing = Airplane('Boeing', '747')
volvo = Truck ('Volvo', 'FH12')
golfwagon = Golfcart ('Yamaha', 'GC100')

boeing.get_make_model()
boeing.moves()

volvo.get_make_model()
volvo.moves()

golfwagon.get_make_model()
golfwagon.moves()

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

# now we add other methods to Airplane class and use Super() to inherit the make and model from Vehicle class

class Airplane (Vehicle):
    def __init__(self,make,model,faa_id):
        super().__init__(make,model)
        self.faa_id = faa_id

    def moves(self):
        print(self.faa_id, 'Flies along..')


class Truck (Vehicle):
    def moves(self):
        print('Rumbles along..')

class Golfcart (Vehicle):
    # pass means it inherits the original moves from the Vehicle class
    pass

boeing = Airplane('Boeing', '747' , 'B747112233')
volvo = Truck ('Volvo', 'FH12')
golfwagon = Golfcart ('Yamaha', 'GC100')

boeing.get_make_model()
boeing.moves()

volvo.get_make_model()
volvo.moves()

golfwagon.get_make_model()
golfwagon.moves()

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

# Here we want to use Plymorphesem , responding differently in every call

for v in (my_car, your_car, boeing, volvo, golfwagon):
    v.get_make_model()
    v.moves()
# for example here we get different responses everytime we call moves()

