class _Private(): # underscore 'denotes' private
# just a convention, no real privacy in python
    def __init__(self, name):
        self.name = name

class NotPrivate():
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self): # underscore 'denotes' private
        print("Hello")

    def display(self):
        print("Hi")
