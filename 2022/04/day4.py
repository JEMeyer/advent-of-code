#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"


def range_to_set(assignment):
    start = int(assignment.split('-')[0])
    end = int(assignment.split('-')[1])

    return set(range(start, end + 1))


def part_1(lines):
    fully_contained_pairs = 0
    for line in lines:
        split_line = line.split(',')
        elf_1 = range_to_set(split_line[0])
        elf_2 = range_to_set(split_line[1])

        if elf_1.issuperset(elf_2) or elf_2.issuperset(elf_1):
            fully_contained_pairs = fully_contained_pairs + 1

    return fully_contained_pairs


def part_2(lines):
    some_overlap_pairs = 0
    for line in lines:
        split_line = line.split(',')
        elf_1 = range_to_set(split_line[0])
        elf_2 = range_to_set(split_line[1])

        if (len(elf_1.intersection(elf_2)) > 0):
            some_overlap_pairs = some_overlap_pairs + 1

    return some_overlap_pairs


def main():
    """ Main entry point of the app """
    file_input = open('input.txt', 'r')
    lines = file_input.read().splitlines()
    print(part_1(lines))
    print(part_2(lines))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
