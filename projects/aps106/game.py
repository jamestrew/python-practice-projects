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

dim = (3, 5)

grid = Board(dim)
print(grid)
