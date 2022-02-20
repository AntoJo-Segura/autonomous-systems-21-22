# map row, column and value triplets to a scalar dimension value   
def rcv(row, column, value, max_row = 9, max_column = 9):
    return (row-1)* max_row * max_row + (column-1) * max_column + (value-1) + 1

assert(rcv(1,1,9) == 9)
assert(rcv(1,2,6) == 15)

def all_filled(max_row = 9, max_column = 9):
    clauses = []
    for r in range(1,max_row+1): 
        for c in range(1, max_column+1):
            clauses.append(
                list(map(lambda v: rcv(r,c,v), range(1,9 +1)))
            )

    return clauses
assert(all_filled()[0] == [1,2,3,4,5,6,7,8,9] )


def not_dubplicated(max_row = 9, max_column = 9):
    clauses = []

    return clauses