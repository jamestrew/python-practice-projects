
# Containers
# list
# set
# dict
# tuple

import collections
from collections import Counter


a = Counter("potato")
print(a)


b = Counter(["a", "b", "b", "c", "c", "d"])
print(b["b"])  # finds the count


c = Counter({"a":1, "b":2})  # dictionary counter


d = Counter(cats = 4, dogs = 7)
print("d - # of cats: ", d["cats"]) # finds the count

e = Counter(a=4, b=2, c=0, d=-2)
f = ["a", "b", "c", "b"]
g = ["e", "e", "e", "e"]

e.subtract(f)
print("Counter e - ", e)

e.update(g)  # adds
print("Counter e - ", e)

e.clear()
print("Counter e - ", e)

b = Counter(["a", "b", "b", "c", "c", "d"])
e = Counter(a=4, b=2, c=0, d=-2)
print(b+e)
print(b-e)
print(b & e)  # intersection
print(b | e)  # union

string = "dicks"
print("my name is {%s}", string)
