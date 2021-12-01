#!/usr/bin/env python3

def read_input(input_file):
    input_file = open(input_file, "r")
    raw_input = input_file.readlines()
    input = [int(a.rstrip()) for a in raw_input]
    return input

def sonar_sweep(measurements): 
    count = len([1 for i in range(len(measurements) - 1) if  measurements[i+1] > measurements[i]])
    return count

def main(input='input.txt'):
    measurements = read_input(input)
    increases = sonar_sweep(measurements)
    print(increases)

if __name__ == '__main__':
    main()
    