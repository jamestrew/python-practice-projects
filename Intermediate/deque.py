import collections
from collections import deque

d = deque("hello")
print(d)

d.append("dicks")
d.extend("dicks")
print(d)
d.appendleft("gay")
print(d)

newlist = [1, 2, 3, 4, 5]
oldlist = [6, 7, 8, 9, 0]
newlist.extend(oldlist)

print(newlist)
