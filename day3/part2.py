#!/usr/bin/env python3

from part1 import read_input, most_common
from collections import Counter

def least_common(lst):
    c = Counter(lst).most_common()
    if len(c) == 1:
        least_common = c[0][0]
    elif c[-1][1] == c[-2][1]:
        least_common = "0"
    else:
        least_common = c[-1][0]
    return least_common

def oxygen_generator_rating(input_list):
    filtered_list = input_list
    i = 0
    while len(filtered_list) > 1:
        bits = [binary[i] for binary in filtered_list]
        max_bit = most_common(bits)
        filtered_list = [binary for binary in filtered_list if binary[i] == max_bit]
        i+=1
        
    return(filtered_list[0])

def c02_scrubber_rating(input_list):
    filtered_list = input_list
    i = 0
    while len(filtered_list) > 1:
        bits = [binary[i] for binary in filtered_list]
        min_bit = least_common(bits)
        filtered_list = [binary for binary in filtered_list if binary[i] == min_bit]
        i+=1
        
    return(filtered_list[0])

def main(input='input.txt'):
    input_list = read_input(input)
    o2 = oxygen_generator_rating(input_list)
    co2 = c02_scrubber_rating(input_list)
    life_support_rating = int(o2, 2)*int(co2, 2)
    print(life_support_rating)

if __name__ == '__main__':
    main()