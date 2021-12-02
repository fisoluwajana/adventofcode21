#!/usr/bin/env python3

from part1 import read_input

def adjust_position(x, y, z, command):
    direction, distance = command.split()
    distance = int(distance)
    if direction == "forward":
        x += distance
        y += z*distance
    elif direction == "down":
        z += distance
    else:
        z -= distance 

    return(x,y,z)


def dive(input_list):
    x,y,z = (0,0,0)
    for command in input_list:
        x,y,z = adjust_position(x, y, z, command)

    return x*y


def main(input='input.txt'):
    input_list = read_input(input)
    result = dive(input_list)
    print(result)


if __name__ == '__main__':
    main()