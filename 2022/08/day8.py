#!/usr/bin/env python
import numpy as np
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"


def populate_grid(grid_rows):
    grid = np.zeros((len(grid_rows), len(grid_rows)))
    for i in range(len(grid_rows)):
        grid[i] = np.array(list(grid_rows[i]))
    return grid

def part_1(grid_rows):
    grid = populate_grid(grid_rows)
    visible_trees = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid) - 1:
                # edge of grid
                visible_trees = visible_trees + 1
            else:
                visibility = {'east': True, 'west': True, 'north': True, 'south': True}
                # check E/W
                for a in range(j):
                    if grid[i][a] >= grid[i][j]:
                        visibility['west'] = False
                for a in range(j + 1, len(grid)):
                    if grid[i][a] >= grid[i][j]:
                        visibility['east'] = False

                # check N/S
                for a in range(i):
                    if grid[a][j] >= grid[i][j]:
                        visibility['north'] = False
                for a in range(i + 1, len(grid)):
                    if grid[a][j] >= grid[i][j]:
                        visibility['south'] = False

                if visibility['north'] or visibility['south'] or visibility['east'] or visibility['west']:
                    visible_trees = visible_trees + 1
    print(visible_trees)


def look_up(grid, x, y):
    score = 0
    for i in range(y - 1, -1, -1):
        if grid[x][i] < grid[x][y]:
            score += 1
        else:
            score += 1
            break
    return score

def look_down(grid, x, y):
    score = 0
    for i in range(y + 1, len(grid[x])):
        if grid[x][i] < grid[x][y]:
            score += 1
        else:
            score += 1
            break
    return score

def look_left(grid, x, y):
    score = 0
    for i in range(x - 1, -1, -1):
        if grid[i][y] < grid[x][y]:
            score += 1
        else:
            score += 1
            break
    return score

def look_right(grid, x, y):
    score = 0
    for i in range(x + 1, len(grid[x])):
        if grid[x][i] < grid[x][y]:
            score += 1
        else:
            score += 1
            break
    return score

def part_2(grid_rows):
    grid = populate_grid(grid_rows)
    max_scenic_score = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            score = look_left(grid, i, j)
            score *= look_right(grid, i, j)
            score *= look_up(grid, i, j)
            score *= look_down(grid, i, j)

            if score > max_scenic_score:
                max_scenic_score = score
    print(max_scenic_score)


def main():
    """ Main entry point of the app """
    file_input = open('input.txt', 'r')
    raw_input = file_input.read().splitlines()
    print('Part 1:')
    part_1(raw_input)
    print('Part 2:')
    part_2(raw_input)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
