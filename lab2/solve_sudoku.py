from sudoku_solver import count_solution, solve

if __name__ == "__main__":
    to_solve = input()
    print( solve(to_solve) + '    This is a solution')
    print('Press y if you want to run count algorithm:')
    start = input()
    if start == 'y': count_solution(to_solve, True)