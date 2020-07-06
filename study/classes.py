import datetime
class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

        Employee.num_of_emps += 1

    def __str__(self):  # __str__ called when object is to be printed
        return '{} {} gets paid {}. Wow what a rich snob'.format(self.first, self.last, self.pay)

    def fullname(self):  # regular method. always takes the instance as the first argument
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @classmethod  # takes the class as the first argument
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split()
        return cls(first, last, pay)

    @staticmethod  # doesn't pass either the instance or class automatically. similar to normal function.
    def is_workday(day):
        """ returns true if a given day is a workday (weekday)"""
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("manages -->", emp.fullname())


emp_1 = Employee('James', 'Trew', 60000)
emp_2 = Employee('Anna', 'Ishihara', 45000)
s = "Eugene Min 70000"
emp_3 = Employee.from_string(s)
print(emp_1)
print()

my_day = datetime.date(2020, 6, 17)
print(Employee.is_workday(my_day))
print()

dev_1 = Developer('Mapara', 'Papas', 0, 'Evil')
dev_2 = Developer('Mochiko', 'San', 0, 'Nice')

print(dev_1.email, dev_1.prog_lang)
print(dev_2.email, dev_2.prog_lang)
print()

mgr_1 = Manager('Fumie', 'Ishihara', 100000, [emp_2])
mgr_1.print_emps()
print(mgr_1.email)
print(emp_1 + emp_2)
print(len(emp_1))
