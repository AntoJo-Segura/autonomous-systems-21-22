from clauses import *

c1 = at_least_one_value
c2 = only_one_value
c3 = filled_row
c4 = filled_column
c5 = filled_grid

def given_constraints(sudoku, max_row = 9, max_col = 9):
    clauses = []
    for r in range(0, max_row ):
        for c in range(0, max_col):
            string_position = r * max_col + c
            constraint = sudoku[string_position]
            if constraint != '.':
                clauses.append([ rcv(r+1, c+1 ,int(constraint)) ]) 

    return clauses

sudoku_sample = '.......1.4.........2...........5.4.7..8...3....1.9....3..4..2...5.1........8.6...'

sample_result = given_constraints(sudoku_sample)

assert(sample_result[0] == [64] )
assert(sample_result[0][0] == 64 )
assert(sample_result[1] == [85] )

c6 = given_constraints







