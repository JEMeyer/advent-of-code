#!/usr/bin/env python
from __future__ import annotations
"""
Module Docstring
"""

__author__ = "Joe Meyer"
__license__ = "MIT"

class File:
    def __init__(self, name, size): # constructor
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name):
        self.name = name
        self.directories = []
        self.files = []

    def add_file(self, file: File):
        self.files.append(file)

    def add_folder(self, folder: 'Directory'):
        self.directories.append(folder)

    def get_size(self):
        count = 0
        for file in self.files:
            count = count + file.size
        for directory in self.directories:
            count = count + directory.get_size()
        return count

def print_filesystem(fs: Directory):
    print_filesystem_recursive(fs, 0)

def print_filesystem_recursive(fs: Directory, level: int):
    space = ' '
    print(f"{space*(2*level)}- {fs.name} (dir, size={fs.get_size()})")
    for file in fs.files:
        print(f"{space*(2*(level+1))}- {file.name} (file, size={file.size})")
    for dir in fs.directories:
        print_filesystem_recursive(dir, level + 1)

def filter_directories_max_size_and_sum(fs: Directory, max_size: int):
    count = 0
    if fs.get_size() < max_size:
        count = count + fs.get_size()
    for dir in fs.directories:
        count = count + filter_directories_max_size_and_sum(dir, max_size)

    return count

def filter_directories_smallest_folder_over_min(fs: Directory, target: int, cur_min: int):
    if fs.get_size() > target and fs.get_size() < cur_min:
        cur_min = fs.get_size()
    for dir in fs.directories:
        temp_min = filter_directories_smallest_folder_over_min(dir, target, cur_min)
        if temp_min < cur_min:
            cur_min = temp_min

    return cur_min

def create_filesystem(lines):
    filesystem = Directory('/')
    current_dir = []
    for line in lines:
        split_line = line.split(' ')
        if split_line[0] == '$':
            if split_line[1] == 'cd':
                if split_line[2][0] == '/':
                    current_dir = ['/']
                elif split_line[2] == '..':
                    current_dir.pop()
                else:
                    current_dir.append(split_line[2])
            elif split_line[1] != 'ls':
                # ls is the only other option, but I don't care about it
                raise Exception('Unknown command: ' + line)
        else:
            if split_line[0] == 'dir':
                tracker = filesystem
                for folder in current_dir:
                    if folder != '/':
                        tracker = next((directory for directory in tracker.directories if directory.name == folder))
                tracker.add_folder(Directory(split_line[1]))
            else:
                tracker = filesystem
                for folder in current_dir:
                    if folder != '/':
                        tracker = next((directory for directory in tracker.directories if directory.name == folder))
                tracker.add_file(File(split_line[1], int(split_line[0])))
    return filesystem

def part_1(lines):
    filesystem = create_filesystem(lines)

    # find the ones we care about
    print(filter_directories_max_size_and_sum(filesystem, 100000))


def part_2(lines):
    filesystem = create_filesystem(lines)

    # calculate size needed
    total_disk_size = 70000000
    unused_req = 30000000
    current_unused = total_disk_size - filesystem.get_size()
    unused_needed = unused_req - current_unused

    smallest_folder_size_to_del = filter_directories_smallest_folder_over_min(filesystem, unused_needed, 99999999999999)
    print(smallest_folder_size_to_del)


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
