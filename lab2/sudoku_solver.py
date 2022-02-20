from clauses import *
import utils

c1 = at_least_one_value()
c2 = only_one_value()
c3 = filled_row()
c4 = filled_column()
c5 = filled_grid()

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

c6 = given_constraints(sudoku_sample)
c = c1 + c2 + c3 + c4 + c5 +c6
assert(c[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9] )
assert(c[-1] == [699] )
assert(c[len(c) -1] == [699] ) #3257
assert(rcv(9,9,9) ==  729)

input_filename = 'lab2/input.cnf'
utils.save_dimacs_cnf(range(0, rcv(9,9,9)), c, input_filename, True)
output_SAT = utils.solve(input_filename, True)
assert( output_SAT[0]== 'SAT')
var_solution = dict(output_SAT[1])

#inverse of rcv function
def rcv_inv(index, max_row = 9, max_column = 9):
    value = ( (index -1 ) % 9 ) + 1
    column = int( (index - value)/max_column % 9 + 1 )
    row = int( (index - value - (column-1) * 9)/ (max_column * max_row) ) + 1

    return [row, column, value]

assert(rcv_inv(rcv(1,5,9)) == [1,5,9]) 
assert(rcv_inv(rcv(7,7,7)) == [7,7,7]) 

solution = ''
for key,is_sol in var_solution.items():
    if is_sol :
        row, col, val = rcv_inv(key)
        solution += str(val)

assert(solution == '967235418438791256125684973296853417478126359531794268396457218857129643214836759')     

#solver encapsulation
def solve(sudoku: str):
    c = c1 + c2 + c3 + c4 + c5 + given_constraints(sudoku)
    input_filename = 'lab2/input.cnf'
    utils.save_dimacs_cnf(range(0, rcv(9,9,9)), c, input_filename, False)
    output_SAT = utils.solve(input_filename, False)
    var_solution = dict(output_SAT[1])
    solution = ''
    for key,is_sol in var_solution.items():
        if is_sol :
            row, col, val = rcv_inv(key)
            solution += str(val)

    return solution 

assert(solve(sudoku_sample) == '967235418438791256125684973296853417478126359531794268396457218857129643214836759')     





