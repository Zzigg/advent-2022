def read_input(day):
    filename = f'C:/repos/advent-2022/inputs/input{day}.txt'
    with open(filename, 'r') as file:
        lines = [line for line in file.readlines()]
    return lines