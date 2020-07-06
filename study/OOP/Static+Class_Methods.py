class Dog():
    dogs = []
    # write class variables in here
    # used statically throughout the class/methods


    def __init__(self, name): # methods
        self.name = name
        self.dogs.append(self)

    @classmethod # decorators
    # class method receives the class 'cls' as implicit first argument
    # allows easy acces of cls vars
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod # decorators
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")

class Math():
    @staticmethod
    def add(x, x2):
        return x + x2

tim = Dog("Tim")
jim = Dog("Jim")
Dog.bark(5)
print(Dog.num_dogs())

print(Math.add(100, 1))
