

sudoku_sample = ['.......1.','4........','.2.......','....5.4.7','..8...3..','..1.9....','3..4..2..','.5.1.....','...8.6...']


# map row, column and value triplets to a scalar dimension value   
def rcv(row, column, value, max_row = 9, max_column = 9):
    return (row-1)* max_row * max_row + (column-1) * max_column + (value-1) + 1

assert(rcv(1,1,9) == 9)
assert(rcv(1,2,6) == 15)