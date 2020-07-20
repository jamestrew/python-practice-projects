xdim = 8
ydim = 8
size = xdim * ydim

col = ['', '', 'r', '', 'b']

index = 0
while index < ydim - 1:
    if col[index] == '':
        col[index] = 'X'
        index -= 1
    index += 1
    print(index)
