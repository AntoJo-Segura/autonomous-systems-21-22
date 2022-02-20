# map row, column and value triplets to a scalar dimension value   
def rcv(row, column, value, max_row = 9, max_column = 9):
    return (row-1)* max_row * max_row + (column-1) * max_column + (value-1) + 1

assert(rcv(1,1,9) == 9)
assert(rcv(1,2,6) == 15)

def at_least_one_value(max_row = 9, max_column = 9):
    clauses = []
    for r in range(1,max_row+1): 
        for c in range(1, max_column+1):
            clauses.append(
                list(map(lambda v: rcv(r,c,v), range(1,9 +1)))
            )

    return clauses
assert(at_least_one_value()[0] == [1,2,3,4,5,6,7,8,9] )


def only_one_value(max_row = 9, max_column = 9):
    clauses = []
    for r in range(1,max_row + 1): 
        for c in range(1, max_column + 1):
            for v in range(1, 9 + 1):
                for v2 in range(v + 1, 9 + 1):
                    clauses.append([-rcv(r,c,v), -rcv(r,c,v2)])
    return clauses

assert(only_one_value()[7]==[-1, -9])
assert(only_one_value()[8]==[-2, -3])

def filled_row(max_row = 9, max_column = 9):
    clauses = []
    for r in range(1, max_row + 1): 
        for v in range(1, 9 + 1):
            clauses.append(
                list(map(lambda c: rcv(r,c,v), range(1,max_column +1)))
            )
    return clauses

assert(filled_row()[0]==[1, 10, 19, 28, 37, 46, 55, 64, 73])

def filled_column(max_row = 9, max_column = 9):
    clauses = []
    for r in range(1, max_column + 1): 
        for v in range(1, 9 + 1):
            clauses.append(
                list(map(lambda c: rcv(r,c,v), range(1,max_row +1)))
            )
    return clauses

assert(filled_column()[0] == [1, 10, 19, 28, 37, 46, 55, 64, 73])


def filled_grid( grid_row = 3, grid_col = 3):
    clauses = []
    for v in range(1, 9+1):
        for r in range(0, grid_row):
            for c in range(0, grid_col):
                clauses.append([
                    rcv(r * grid_row + gr, c * grid_col + gc, v)
                    for gr in range(1,grid_row+1) 
                    for gc in range(1, grid_col + 1)
                ])
    return clauses


assert(filled_grid()[0] == [1, 10, 19, 82, 91, 100, 163, 172, 181]) 
assert(filled_grid()[1] == [28, 37, 46, 109, 118, 127, 190, 199, 208]) 




