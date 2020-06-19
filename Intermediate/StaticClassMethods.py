class Person(object):
    population = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.population.append(self)

    @classmethod
    def getPopulation(cls):
        return len(cls.population)

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name + " is " + str(self.age) + " years old.")

Jim = Person("Jim", 32)
Pam = Person("Pam", 12)



