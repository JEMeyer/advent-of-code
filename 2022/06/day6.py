#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"


def part_1(lines):
    fully_contained_pairs = 0
    for line in lines:
        split_line = line.split(',')
        elf_1 = range_to_set(split_line[0])
        elf_2 = range_to_set(split_line[1])

        if elf_1.issuperset(elf_2) or elf_2.issuperset(elf_1):
            fully_contained_pairs = fully_contained_pairs + 1

    return fully_contained_pairs


def find_start_of_packet(stream):
    for i in range(len(stream)):
        substr = stream[i:i+4]

        # Check if the length of the set of the 4 characters
        # is equal to the length of the substring. If it is,
        # then the 4 characters are unique
        if len(set(substr)) == len(substr):
            return i + 4


def find_start_of_message(stream, start_index):
    for i in range(start_index - 1, len(stream)):
        substr = stream[i:i+14]

        # Check if the length of the set of the 4 characters
        # is equal to the length of the substring. If it is,
        # then the 4 characters are unique
        if len(set(substr)) == len(substr):
            return i + 14


def main():
    """ Main entry point of the app """
    file_input = open('input.txt', 'r')
    raw_input = file_input.read().splitlines()[0]
    first_start_of_packet = find_start_of_packet(raw_input)
    first_start_of_message = find_start_of_message(raw_input, first_start_of_packet)
    print('Part 1 answer: ', first_start_of_packet)
    print('Part 2 answer: ',  first_start_of_message)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
