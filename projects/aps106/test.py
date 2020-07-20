xdim = 8
ydim = 8
size = xdim * ydim

index = 61

for i in range(ydim):
    col_clr = []
    col_indices = [k + i for k in range(size) if k % ydim == 0]
    print(col_indices)
