grid = [1, 0, 2]
check = [1 if i == 0 else 0 for i in grid]
print(check)

if all(grid):
    print("empty")
