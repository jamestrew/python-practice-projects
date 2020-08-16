class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):  # regular method. always takes the instance as the first argument
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
