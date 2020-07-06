class BaseClass():
    def __init__(self):
        self.x = 5

    def printHam(self):
        print("Ham")


class InClass1(BaseClass):
    def __init__(self):
        super().__init__()
        self.x = 17


class InClass2(BaseClass):
    def printHam(self):
        print("Ham2")


class subClass(InClass1, InClass2):
    def __init__(self):
        super().__init__()
        self.y = 69


t = subClass()

print(t.x)
t.printHam()
