

x = [[2, -2],
     [5, 3 ]]

y = [[-1, 4],
     [7, -6]]

result = [[sum(a*b for a,b in zip(x_row,y_col)) for y_col in zip(*y)] for x_row in x]

for r in result:
    print(r)
