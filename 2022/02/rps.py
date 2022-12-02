#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"

move_to_points = {'A': 1, 'B': 2, 'C': 3}


def play_game(opponent, player):
    # tie
    if opponent == player:
        return 3 + move_to_points[player]
    # win
    elif (opponent == 'A' and player == 'B') or (opponent == 'B' and player == 'C') or (opponent == 'C' and player == 'A'):
        return 6 + move_to_points[player]
    #loss
    else:
        return move_to_points[player]

def pick_move(opponent, outcome):
    if outcome == 'X': #loss
        if opponent == 'A':
            return 'C'
        elif opponent == 'B':
            return 'A'
        else:
            return 'B'
    if outcome == 'Z': #win
        if opponent == 'A':
            return 'B'
        elif opponent == 'B':
            return 'C'
        else:
            return 'A'
    else: # draw
        return opponent

def convert_player_move(move, opponent_move = ''):
    if opponent_move == '': # straight mapping from XYZ to ABC
        if move == 'X':
            return 'A'
        elif move == 'Y':
            return 'B'
        else:
            return 'C'
    else:
        return pick_move(opponent_move, move)

def solve_puzzle(games, pt2 = False):
    total_score = 0
    for game in games:
        plays = game.split(' ')
        opponent_move = plays[0]
        user_input = plays[1]
        convert_move_second_param = opponent_move if pt2 else ''
        total_score = total_score + play_game(
            opponent_move,
            convert_player_move(user_input, convert_move_second_param)
        )

    return total_score


def main():
    """ Main entry point of the app """
    file_input = open('rps_input.txt', 'r')
    lines = file_input.read().splitlines()
    score = solve_puzzle(lines, True)
    print(score)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
