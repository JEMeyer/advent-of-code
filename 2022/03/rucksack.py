#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"


def convert_to_priority(input):
  # check if the character is a lowercase letter
  if input.islower():
    # if it is, return the corresponding number in the range 1-26
    return ord(input) - ord('a') + 1
  # check if the character is an uppercase letter
  elif input.isupper():
    # if it is, return the corresponding number in the range 27-52
    return ord(input) - ord('A') + 27
  # if it is neither a lowercase nor an uppercase letter, return 0
  else:
    return 0


def part_1(bags):
    sum_of_priorities = 0
    for bag in bags:
        compartment_1, compartment_2 = bag[:len(bag)//2], bag[len(bag)//2:]
        similar_item = set(compartment_1).intersection(set(compartment_2))
        sum_of_priorities = sum_of_priorities + convert_to_priority(str(list(similar_item)[0]))
    print('Part 1 sum of priorities: ', sum_of_priorities)

def part_2(bags):
    sum_of_priorities = 0
    for x in range(0, len(bags), 3):
        badge = set(bags[x]).intersection(set(bags[x+1])).intersection(set(bags[x+2]))
        sum_of_priorities = sum_of_priorities + convert_to_priority(str(list(badge)[0]))
    print('Part 2 sum of priorities: ', sum_of_priorities)

def main():
    """ Main entry point of the app """
    file_input = open('input.txt', 'r')
    bags = file_input.read().splitlines()
    part_1(bags)
    part_2(bags)
    




if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
