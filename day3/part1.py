#!/usr/bin/env python3

from collections import Counter

def read_input(input_file):
    input_file = open(input_file, "r")
    raw_input = input_file.readlines()
    input = [a.rstrip() for a in raw_input]
    return input

def most_common(lst):
    c = Counter(lst).most_common()
    if c[0][1] == c[1][1]:
        most_common = "1"
    else:
        most_common = c[0][0]
    return most_common


def gamma_rate(input_list):
    gamma = ""
    for i in range(len(input_list[0])):
        bits = [binary[i] for binary in input_list]
        max_bit = most_common(bits)
        gamma += max_bit
    return gamma

def epsilon_rate(gamma):
    epsilon = ""
    for bit in gamma:
        epsilon += str(abs(1 - int(bit)))
    return epsilon 

def main(input='input.txt'):
    input_list = read_input(input)
    gamma = gamma_rate(input_list)
    epsilon = epsilon_rate(gamma)
    power_cons = int(gamma,2)*int(epsilon,2)
    print(power_cons)

if __name__ == '__main__':
    main()