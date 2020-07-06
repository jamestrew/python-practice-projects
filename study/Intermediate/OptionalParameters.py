# Optional Parameters

# using a equal sign in the arguments sets a defaults value
# making the argument a optional parameter
def func(x, a=2):
    return x**a

call = func(5, 1)
#print(call)

def func2(word, add = 5, freq = 1): # multiple optional parameters
    print(word*(freq + add))

#func2("James ", ,2) <--- can't do this

class car():
    def __init__(self, make, model, year, condition = "new", kms = 0):
        self.make = make
        self.model = model
        self.make = make
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This %s is a piece of shit," %self.make)

whip = car("Ford", "Fusion", 2012, "trash", 20)
wank = car("Toyota", "Wagon R", 1992)
whip.display(False)
wank.display(True)
