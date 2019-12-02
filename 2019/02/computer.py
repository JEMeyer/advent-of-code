#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"

def runSimulation(state):
    currIdx = 0
    while state[currIdx] != 99:
        if state[currIdx] == 1:
            state[state[currIdx + 3]] = state[state[currIdx + 1]] + state[state[currIdx + 2]]
        elif state[currIdx] == 2:
            state[state[currIdx + 3]] = state[state[currIdx + 1]] * state[state[currIdx + 2]]
        currIdx += 4
    return state[0]

def main():
    """ Main entry point of the app """
    masterState = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]
    i = 0
    while i < 100:
        j = 0
        while j < 100:
            localState = list(masterState)
            localState[1] = i
            localState[2] = j
            result = runSimulation(localState)
            if result == 19690720:
                print(100 * i + j)
            j += 1
        i += 1

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()