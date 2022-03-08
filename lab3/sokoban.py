#!/usr/bin/env python3

import argparse
import sys
import subprocess as sp


def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='Solve Sudoku problems.')
    parser.add_argument("-i", help="Path to the file with the Sokoban instance.")
    return parser.parse_args(argv)


class SokobanGame(object):
    """ A Sokoban Game. """
    def __init__(self, string):
        """ Create a Sokoban game object from a string representation such as the one defined in
            http://sokobano.de/wiki/index.php?title=Level_format
        """
        lines = string.split('\n')
        self.h, self.w = len(lines), max(len(x) for x in lines)
        self.player = None
        self.walls = set()
        self.boxes = set()
        self.goals = set()
        self.positions = set()
        self.gaps = set()
        self.pddl = ''
        for i, line in enumerate(lines, 0):
            for j, char in enumerate(line, 0):
                self.positions.add((i, j))
                if char == '#':  # Wall
                    self.walls.add((i, j))
                elif char == '@':  # Player
                    assert self.player is None
                    self.player = (i, j)
                elif char == '+':  # Player on goal square
                    assert self.player is None
                    self.player = (i, j)
                    self.goals.add((i, j))
                elif char == '$':  # Box
                    self.boxes.add((i, j))
                elif char == '*':  # Box on goal square
                    self.boxes.add((i, j))
                    self.goals.add((i, j))
                elif char == '.':  # Goal square
                    self.goals.add((i, j))
                elif char == ' ':  # Space
                    self.gaps.add((i,j))
                else:
                    raise ValueError(f'Unknown character "{char}"')

    def is_wall(self, x, y):
        """ Whether the given coordinate is a wall. """
        return (x, y) in self.walls

    def is_box(self, x, y):
        """ Whether the given coordinate has a box. """
        return (x, y) in self.boxes

    def is_goal(self, x, y):
        """ Whether the given coordinate is a goal location. """
        return (x, y) in self.goals

    def get_pddl(self):
        pddl  = []
        name = 'simpleone'
        pddl += ['(define (problem '+ name +')']
        pddl += ['  (:domain sokoban)']
        pddl += ['  (:objects']
        pddl += ['  teletransport - transport']
        pddl += ['  dir-right - direction']
        pddl += ['  dir-left - direction']
        pddl += ['  dir-up - direction']
        pddl += ['  dir-down - direction']
        pddl += ['  player-01 - player']

        for i,coord in enumerate(self.boxes):
            pddl += ['  box-0'+ str(i+1)+' - box']
        
        for coord in self.positions:
            pddl += ['  pos-'+ str(coord[0]) +'-'+ str(coord[1]) +' - position']
        pddl += ['  )']
        pddl += ['  (:init ']
        for coord in self.goals:
            pddl += ['  (is-goal pos-'+ str(coord[0]) +'-'+ str(coord[1]) +')']
        for i,coord in enumerate(self.boxes):
            pddl += ['  (at box-0'+ str(i)+' pos-' + str(coord[0]) +'-'+ str(coord[1]) +')']

        pddl += ['  (at player-01 pos-' + str(self.player[0]) +'-' + str(self.player[1]) +')']
        pddl += ['  (is-transported teletransport)']
        for coord in self.gaps:
            pddl += ['  (transport-position pos-'+ str(coord[0]) + '-'+ str(coord[1]) +')']

        for coord in self.positions:
            if coord not in self.goals:
                pddl += ['  (non-goal pos-'+ str(coord[0])+ '-'+ str(coord[1])+ ')']

        for coord in self.gaps:
            pddl += ['  (empty pos-'+ str(coord[0]) + '-'+ str(coord[1]) +')']

        for coord in self.gaps:
            pddl += self.move_pddl(coord)

        pddl += self.move_pddl(self.player)

        pddl +=['  (direction-move pos-2-4 pos-2-5 dir-right)']
        pddl += ['  )']
        pddl += ['  (:goal (and ']
        for i,coord in enumerate(self.boxes):
            pddl += ['  (at-goal box-0'+str(i+1)+'))']
        pddl += ['  )']
        pddl += [')']
        self.pddl = '\n'.join(pddl) 
        return self.pddl

    def move_pddl(self, coord):
        pddl  = []
        right_pos = (coord[0],coord[1]+1)
        if ( right_pos in self.gaps or right_pos in self.boxes):#right move
            pddl +=['  (direction-move pos-'+str(coord[0])+'-'+str(coord[1])+' pos-'+str(right_pos[0])+'-'+str(right_pos[1])+' dir-right)']

        left_pos = (coord[0],coord[1]-1)
        if (left_pos in self.gaps or left_pos in self.boxes ):#left move
            pddl +=['  (direction-move pos-'+str(coord[0])+'-'+str(coord[1])+' pos-'+str(left_pos[0])+'-'+str(left_pos[1])+' dir-left)']

        up_pos = (coord[0]+1,coord[1])
        if up_pos in self.gaps or up_pos in self.boxes :#up move
            pddl +=['  (direction-move pos-'+str(coord[0])+'-'+str(coord[1])+' pos-'+str(up_pos[0])+'-'+str(up_pos[1])+' dir-up)']

        down_pos =  (coord[0]-1,coord[1])   
        if down_pos in self.gaps or down_pos in self.boxes :#down move
            pddl +=['  (direction-move pos-'+str(coord[0])+'-'+str(coord[1])+' pos-'+str(down_pos[0])+'-'+str(down_pos[1])+' dir-down)']  

        return pddl 

    def save_pddl(self, output_file = 'instance_problem.pddl'):
        with open(output_file,'w') as file:
            file.write(self.pddl)
        return output_file

    def call_downward(self):
        instance = 'instance_problem.pddl'#'problem_sokoban1.pddl' #'instance_problem.pddl'
        output_file = 'solution_output.txt'
        downward_path = './downward/fast-downward.py'
        cmd = 'python '+ downward_path +' --overall-time-limit 60 --alias seq-sat-lama-2011 --plan-file '
        cmd += output_file+' domain_sokoban_2a.pddl '+ instance + ''
        print(cmd)
        print(sp.run(cmd, shell = True))
        return 1

def main(argv):
    args = parse_arguments(argv)
    with open(args.i, 'r') as file:
        board = SokobanGame(file.read().rstrip('\n'))
    
    board.get_pddl()
    board.save_pddl()
    board.call_downward()
    # print(board.pddl)

    # TODO - Some of the things that you need to do:
    #  1. (Previously) Have a domain.pddl file somewhere in disk that represents the Sokoban actions and predicates.
    #  2. Generate an instance.pddl file from the given board, and save it to disk.
    #  3. Invoke some classical planner to solve the generated instance.
    #  3. Check the output and print the plan into the screen in some readable form.


if __name__ == "__main__":
    main(sys.argv[1:])
