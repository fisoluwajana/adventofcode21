#!/usr/bin/env python3

def read_input(input_file):
    input_file = open(input_file, "r")
    raw_input = input_file.readlines()
    input = [a.rstrip() for a in raw_input]
    return input

def adjust_position(x, y, command):
    direction, distance = command.split()
    distance = int(distance)
    if direction == "forward":
        x += distance
    elif direction == "down":
        y += distance
    else:
        y -= distance 

    return(x,y)


def dive(input_list):
    x,y = (0,0)
    for command in input_list:
        x,y = adjust_position(x, y, command)

    return x*y


def main(input='input.txt'):
    input_list = read_input(input)
    result = dive(input_list)
    print(result)


if __name__ == '__main__':
    main()