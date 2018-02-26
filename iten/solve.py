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
        graph = {}
        tickets = int(lines.pop(0).strip())
        for i in range(0,tickets):
            key = lines.pop(0).strip()
            value = lines.pop(0).strip()
            graph[key] = value
        test_cases.append(graph)

    f = open('output_file','w')
    f.write(get_output(test_cases))    

def get_output(test_cases):
    output_string = ""

    for i in range(len(test_cases)):
        output_string += "Case #%d: "%(i+1)
        order = get_correct_order(test_cases[i])[::-1]
        for airport_one, airport_two in order:
            output_string += "%s-%s "%(airport_one,airport_two)
        output_string += "\n"
    return output_string

def get_correct_order(graph):

    parent_node = ""
    end_node = ""
    result = []
    visted = {}
    for key,value in graph.iteritems():
        if value not in graph:
            parent_node = key
            end_node = value
            break
    result.append((parent_node,end_node))
    visted[parent_node] = 1

    while len(visted) != len(graph):
        for key, value in graph.iteritems():
            if value == parent_node:
                result.append((key,parent_node))
                parent_node = key
                visted[parent_node] = 1
    
    return result
    
    
if __name__ == "__main__":
    main()