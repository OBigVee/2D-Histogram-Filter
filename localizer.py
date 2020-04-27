# import pdb
import numpy as np
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    height = len(grid)
    width = (grid[0])
    for x in range(height):
        row = []
        for y in range(width):
            hit = (color == grid[x][y])
            row.append(beliefs[x][y]* (hit * p_hit + (1-hit) * p_miss) )
        new_beliefs.append(row)
    s = sum(new_beliefs)
    for i in range(height):
        for j in range(width):
            new_beliefs[i][j] = new_beliefs[i][j]/s
    
#     if beliefs:
#         for row in range(len(grid)):
#             new_beliefs.append(np.asarray(beliefs)*p_hit)
#     else:
#         for row in range(len(grid)):
#             new_beliefs.append(np.asarray(beliefs)*p_miss)

    #
    # TODO - implement this in part 2
    #

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
