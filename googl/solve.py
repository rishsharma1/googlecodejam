import argparse
import os
import math
import sys

def main():

    parser = argparse.ArgumentParser(description='solve Gbus challenge')
    parser.add_argument('--file',help='input file')

    args = parser.parse_args()
    input_file = None

    try:
        input_file = open(args.file,'r')
    except IOError:
        print('There was an error opening the file!')
        return

    lines = input_file.readlines()
    test_cases = []

    for line in lines[1:]:
        test_cases.append(int(line.strip()))

    f = open('output_file','w')
    f.write(get_output_string(test_cases))

def get_output_string(test_cases):
    output_string = ""
    max_k = find_max_string_fitting(max(test_cases))
    kth_zero_one_string = get_nth_zero_one_string(max_k)

    for i in range(len(test_cases)):
        kth_char = kth_zero_one_string[test_cases[i]-1]
        output_string += "Case #%d: %s\n"%(i+1,kth_char)
    return output_string

def find_max_string_fitting(max_k):

    chars_that_can_fit = 0
    i = 1
    print max_k
    while chars_that_can_fit < max_k:
        chars_that_can_fit = 2*(2**(i-1)) -1
        print chars_that_can_fit
        if chars_that_can_fit >= max_k:
            return i
        i += 1


def switch(string):
    switch_string = ""
    for char in string:
        if char == "0":
            switch_string += "1"
        else:
            switch_string += "0"

    return switch_string

def get_nth_zero_one_string(n):

    # n == 1
    zero_one_string = "0"
    previous_string = "0"

    if n == 1:
        return zero_one_string

    for i in range(1,n):
        new_string = previous_string + "0" + switch(previous_string[::-1])
        zero_one_string = new_string
        previous_string = zero_one_string

    return zero_one_string


if __name__ == "__main__":
    main()
