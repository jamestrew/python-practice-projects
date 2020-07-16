class Dog:

    def bark(self):
        print("woof")

class Husky(Dog):

    def __init__(self):
        super().__init__()

    def woof(self):
        self.bark()


d = Dog()
lilo = Husky()
lilo.woof()
