import argparse
import os

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
        
        gbuses = int(lines.pop(0).strip())
        bus_infos = lines.pop(0).strip().split(' ')
        gbuses_info = []
        for i in range(0,gbuses):
            #gbuses_info.append((bus_infos[i*2], bus_infos[i*2+1]))
            gbuses_info.append(GBus(int(bus_infos[i*2]), int(bus_infos[i*2+1])))
        
        n_cities = int(lines.pop(0).strip())
        cities = []

        for i in range(0,n_cities):
            cities.append(int(lines.pop(0).strip()))
        
        # store the test case
        test_cases.append(TestCase(i,gbuses_info,cities))
        try:
            # pop the last line
            lines.pop(0)
        except :
            pass

    f = open('output_file','w')
    f.write(get_output_string(test_cases))


# gets the number of buses that pass through the given city
def get_num_buses_pass_through(city, gbuses_info):

    num = 0
    for gbus in gbuses_info:
        if city >= gbus.starting and city <= gbus.finish:
            num += 1
    return num

def get_output_string(test_cases):

    output_string = ""
    for i in range(len(test_cases)):
        output_string += "Case #%d: "%(i+1)
        for city in test_cases[i].cities:
            num_of_buses_pass_through = get_num_buses_pass_through(city,test_cases[i].gbuses)
            output_string += "%d "%(num_of_buses_pass_through)
        output_string += "\n"
    return output_string


class TestCase():

    def __init__(self, test_number, gbuses, cities):
        self.test_number = test_number
        self.gbuses = gbuses
        self.cities = cities
    
    def __str__(self):
        test_case_string = "Test Number: %d\n"%(self.test_number)
        test_case_string += "Cities: %s\n"%(str(self.cities))
        for i in range(0,len(self.gbuses)):
            test_case_string += "GBus %d: %s\n"%(i,str(self.gbuses[i]))
        return test_case_string


class GBus():

    def __init__(self, starting, finish):
        if(starting > finish):
            self.finish = starting
            self.starting = finish
        else:
            self.starting = starting
            self.finish = finish
    
    def __str__(self):
        return "(%d,%d)"%(self.starting,self.finish)


def print_test_cases(test_cases):
    for test_case in test_cases:
        print test_case


if __name__ == "__main__":
    main()