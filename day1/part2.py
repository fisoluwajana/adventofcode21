#!/usr/bin/env python3

from part1 import read_input,sonar_sweep

def sonar_sweep_2(measurements):
    triples = [sum(measurements[i:i+3]) for i in range(len(measurements) -2)]
    count = sonar_sweep(triples)
    return count


def main(input='input.txt'):
    measurements = read_input(input)
    increases = sonar_sweep_2(measurements)
    print(increases)

if __name__ == '__main__':
    main()
