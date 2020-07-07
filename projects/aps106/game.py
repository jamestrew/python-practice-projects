from board import Board

"""
1. Ask user for board
    - randomly generation (x, y inputs)
    - read from file

        --> if read from file: ask size

2. Play mode
    - interactive play
    - computer play

PLAY
"""

# step: board generation based on user input

# if random generation:
# n, m = map(int, input("Enter board dimensions (eg. 3x4 = 3 4): ").split())

fname = "test.txt"
with open(fname) as f:
    rows = f.readlines()

dim = tuple(map(int, rows[0].split()))
content = [letter for row in rows[1:] for letter in row.strip()]

grid = Board(dim, content)
print(grid)
print()

grid.kill(0, 0)
print(grid)
