#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"


def caloriesToElves(calories):
    elves = []
    current_elf = 0
    for line in calories:
        if line == '\n':
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf = current_elf + int(line)
    return elves


def main():
    """ Main entry point of the app """
    calories = open('pt1input.txt', 'r')
    lines = calories.readlines()
    elves = caloriesToElves(lines)
    elves.sort(reverse=True)

    # top 1 elf
    print(elves[0])

    # top 3 elves
    print(sum(elves[0:3]))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
