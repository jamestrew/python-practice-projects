grid = [i for i in range(12)]

left = [i for i in range(12) if i % 4 == 0]
right = [i + 3 for i in range(12) if i % 4 == 0]
print(left)
print(right)
