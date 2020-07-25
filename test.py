class Test:

    def __repr__(self):
        return 'repr'

    def __str__(self):
        return 'str'

    def yay(self):
        print("boo")

class Main:

    def __init__(self):
        self.foo = Test()


m = Main()
m.foo.yay()
print(m.foo)
