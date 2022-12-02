#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"


def play_rock_paper_scissors_pt1(games):
    total_score = 0
    for game in games:
        plays = game.split(' ')
        if plays[0] == 'A': # rock
            if plays[1] == 'X': #rock
                total_score = total_score + 4 # draw
            if plays[1] == 'Y': # paper
                total_score = total_score + 8 # win
            if plays[1] == 'Z': # sciccors
                total_score = total_score + 3 # loss
        elif plays[0] == 'B': # paper
            if plays[1] == 'X': #rock
                total_score = total_score + 1 # loss
            if plays[1] == 'Y': # paper
                total_score = total_score + 5 # draw
            if plays[1] == 'Z': # sciccors
                total_score = total_score + 9 # win
        else: # scissors
            if plays[1] == 'X': #rock
                total_score = total_score + 7 # win
            if plays[1] == 'Y': # paper
                total_score = total_score + 2 # loss
            if plays[1] == 'Z': # sciccors
                total_score = total_score + 6 # draw

    return total_score


def play_rock_paper_scissors_pt2(games):
    total_score = 0
    for game in games:
        plays = game.split(' ')
        if plays[0] == 'A': # rock
            if plays[1] == 'X': # loss
                total_score = total_score + 3
            if plays[1] == 'Y': # draw
                total_score = total_score + 4
            if plays[1] == 'Z': # win
                total_score = total_score + 8
        elif plays[0] == 'B': # paper
            if plays[1] == 'X': # loss
                total_score = total_score + 1
            if plays[1] == 'Y': # draw
                total_score = total_score + 5
            if plays[1] == 'Z': # win
                total_score = total_score + 9
        else: # scissors
            if plays[1] == 'X': # loss
                total_score = total_score + 2
            if plays[1] == 'Y': # draw
                total_score = total_score + 6
            if plays[1] == 'Z': # win
                total_score = total_score + 7

    return total_score


def main():
    """ Main entry point of the app """
    file_input = open('rps_input.txt', 'r')
    lines = file_input.read().splitlines()
    score = play_rock_paper_scissors_pt2(lines)
    print(score)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
