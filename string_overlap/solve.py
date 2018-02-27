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
    n_test_cases = int(lines.pop(0).strip())

    for i in range(0,n_test_cases):
        test_cases.append((lines.pop(0).strip(),lines.pop(0).strip()))
    f = open('output_file','w')
    f.write(get_output_string(test_cases))

def get_output_string(test_cases):

    output_string = ""
    for i in range(len(test_cases)):
        s1 = test_cases[i][0].replace("*","####")
        s2 = test_cases[i][1].replace("*","####")
        output_string += "Case #%d: %s\n"%(i+1,str(matches(s1,s2)).upper())
    return output_string

def matches(s1,s2):


    matrix = []
    for i in range(len(s1)+1):
        matrix.append([False]*(len(s2)+1))

    matrix[0][0] = True
    for i in range(1,len(s1)+1):
        if s1[i-1] == '#':
            matrix[i][0] = True

    for j in range(1,len(s2)+1):
        if s2[j-1] == '#':
            matrix[0][j] = True

    for i in range(1,len(s1)+1):

        for j in range(1,len(s2)+1):

            m1 = s1[i-1] == '#'
            m2 = s2[j-1] == '#'

            if m1 and m2:
                matrix[i][j] = matrix[i-1][j] or matrix[i][j-1] or matrix[i-1][j-1]
            elif m1 and not m2:
                matrix[i][j] = matrix[i-1][j] or matrix[i-1][j-1]
            elif not m1 and m2:
                matrix[i][j] = matrix[i][j-1] or matrix[i-1][j-1]
            else:
                matrix[i][j] = matrix[i-1][j-1] and (s1[i-1] == s2[j-1])

    return matrix[len(s1)][len(s2)]


def convert_string_to_regex_list(string):
    converted_patterns = []
    patterns  = string.split("*")

    for i in range(len(patterns)):
        converted_patterns.append("^"+patterns[i]+"$")
        if i != len(patterns)-1:
            converted_patterns.append(STAR_PATTERN)

    return converted_patterns



if __name__ == "__main__":
    main()
