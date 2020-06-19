import collections
from collections import namedtuple

Point = namedtuple("Point", "x y z")

newP = Point(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)
print(newP[0])
print(newP._asdict())
print(newP._fields)

newP = newP._replace(y = 1)
print(newP)

randlist = ["a", "b", "c"]
p = Point._make(randlist)
print(p)

