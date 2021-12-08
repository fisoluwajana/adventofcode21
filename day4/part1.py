#!/usr/bin/env python3

def bingo(input_file):
    input_file = open(input_file, "r")
    raw_input = input_file.readlines()
    input = [(a.rstrip()) for a in raw_input]
    bingo_nums = input[0].split(",")
    print(type(bingo_nums))
    input.pop(0)
    i = -1
    cards = []
    for line in input:
        if line == '':
            i+=1
            cards.append([])
        else:
            cards[i].append(list(filter(None, line.split(" "))))
    for number in bingo_nums:
        for a in range(len(cards)):
            if x in 
            for b in range(len(cards[a])):
                for c in range(len(cards[a][b])):
                    if cards[a][b][c] == number:
                        cards[a][b][c]+="x"
                        print(cards)
        

def check_bingo(card):

def check_rows():
    for row in card:
        if "x" in (row[0] and row[1] and row[2] and row[3] and row[4])
            return(True)

def check_columns(card):
    for i in range(5):
        if "x" in (card[0][i] and card[1][i] and card[2][i] and card[3][i] and card[4][i]):
            return(True)

def check_diagonals(card):
    if "x" in (card[0][0] and card[1][1] and card[2][2] and card[3][3] and card[4][4]):
        return(True)

                    
        




def main(input='test.txt'):
    input = bingo(input)
    print(input)

if __name__ == '__main__':
    main()