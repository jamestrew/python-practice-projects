def add7(x):
    return x + 7

def isOdd(x):
    return x%2 != 0


# filter(true/false, list)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(isOdd, a))
c = [x for x in a if isOdd(x)]
d = list(filter(isOdd, map(add7, a)))
e = list(map(add7, b))

print(a)
print(b)
print(c)
print(d)
print(e)
