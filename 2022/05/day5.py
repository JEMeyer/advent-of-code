#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"

import re

def range_to_set(assignment):
    start = int(assignment.split('-')[0])
    end = int(assignment.split('-')[1])

    return set(range(start, end + 1))


def create_queues(starting):
    stack_count = int(starting[-1].split('   ')[-1])
    queues = [[] for _ in range(stack_count)]

    first_row = True
    for row in reversed(starting):
        if not first_row:
            cells = list(row)
            index = 0
            for i in range(1, len(row), 4):
                if cells[i] != ' ':
                    queues[index].append(cells[i])
                index = index + 1
        else:
            first_row = False
    return queues


def print_top_boxes(queues):
    for queue in queues:
        print(queue[-1])


def part_1(starting, moves):
    queues = create_queues(starting)
    for move in moves:
        x = re.findall('move (\d+) from (\d+) to (\d+)', move)
        extracted_move = x[0]

        # move X from Y to Z
        for i in range(int(extracted_move[0])):
            box = queues[int(extracted_move[1]) - 1].pop()
            queues[int(extracted_move[2]) - 1].append(box)

    print_top_boxes(queues)


def part_2(starting, moves):
    queues = create_queues(starting)
    for move in moves:
        x = re.findall('move (\d+) from (\d+) to (\d+)', move)
        extracted_move = x[0]

        boxes = []

        # move X from Y to Z
        for i in range(int(extracted_move[0])):
            boxes.append(queues[int(extracted_move[1]) - 1].pop())

        boxes = reversed(boxes)
        for box in boxes:
            queues[int(extracted_move[2]) - 1].append(box)

    print_top_boxes(queues)


def input_parser(lines):
    starting_graph = []
    moves = []
    graph_mode = True
    for line in lines:
        if line == '\n':
            graph_mode = False
        elif graph_mode:
            starting_graph.append(line)
        else:
            moves.append(line)
    return starting_graph, moves


def main():
    """ Main entry point of the app """
    file_input = open('input.txt', 'r')
    lines = file_input.readlines()
    starting_graph, moves = input_parser(lines)
    print('Part 1:')
    part_1(starting_graph, moves)
    print('Part 2:')
    part_2(starting_graph, moves)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
