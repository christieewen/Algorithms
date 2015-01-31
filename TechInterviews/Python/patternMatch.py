import sys
import re

def findBestMatch(pattern, path):
    re.findall(r+pattern, path)
#['foot', 'fell', 'fastest']
# Example to call this program: python34 patternMatch.py <input_file> output_file 
def main(args):
    input_file = open(args[1], 'r')
    output_file = open(args[2], 'w')
    
    pattern_list = []
    path_list = []
    
    N = input_file.readline()
    for N in input_file:
        pattern_list.append(input_file.readline())
    
    M = input_file.readline()
    for M in input_file:
        path_list.append(input_file.readline())
    
if __name__ == '__main__':
    main(sys.argv)
    
