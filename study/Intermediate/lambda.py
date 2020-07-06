# lambda tutorial
# anonymous function

def func(x):
    return x + 5
print(func(2))

# alternatively, for single line functions
func2 = lambda x: x + 5
print(func2(5))


# can weave them into other functions
def func3(x):
    func2 = lambda x: x + 5
    return func2(x) + 85
print(func3(5))

# can have multiple arguments with defaults
func4 = lambda x, y = 3: 2*x + y
print(func4(2))


# interaction with lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = list(map(lambda x: x + 5, a)) # significantly smartens up code
print("newlist = ", newlist)

filterlist = list(filter(lambda x: x%2 == 0, a))
print("filterlist = ", filterlist)

# x%2 == 0 gets even x
# x%2 != 0 gets odd x
