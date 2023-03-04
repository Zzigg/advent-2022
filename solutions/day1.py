import os
import sys

inputs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'inputs'))
sys.path.append(inputs_dir)

import input_reader

INPUT = input_reader.read_input(1)

def solution_1():
    elfs_bag = []
    calorie_counter = 0
    for calorie in INPUT:
        if calorie.replace('\n', '') == '':
            elfs_bag.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += int(calorie)
    
    return max(elfs_bag)

def solution_2():
    elfs_bag = []
    calorie_counter = 0
    for calorie in INPUT:
        if calorie.replace('\n', '') == '':
            elfs_bag.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += int(calorie)
    
    top_3 = 0
    for _ in range(0, 3):
        top_3 += max(elfs_bag)
        elfs_bag.pop(elfs_bag.index(max(elfs_bag)))

    return top_3
if __name__ == '__main__':
    print(f'Challeng 1:', solution_1())  
    print(f'Challeng 2:', solution_2())