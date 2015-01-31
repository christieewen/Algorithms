import sys
import re

def findBestWildCardMatch(patterns):
    pass

def findBestMatch(patterns, paths):
    result = []
    temp = []
    for path in paths:
        temp.clear()
...     for pattern in patterns:
...         if re.findall(r'pattern', path):
                temp.append(pattern)
        if len(temp) > 1:
            result.append(findBestWildCardMatch(temp))
        else if len(temp) == 0:
            result.append("NO MATCH FOUND")
        
        
#['foot', 'fell', 'fastest']
# Example to call this program: python34 patternMatch.py <input_file> output_file 
def main(args):
    input_file = open(args[1], 'r')
    output_file = open(args[2], 'w')
    
    pattern_list = []
    path_list = []
    
    N = input_file.readline()
    for i in range(N):
        pattern_list.append(input_file.readline())
    
    M = input_file.readline()
    for j in range(M):
        path_list.append(input_file.readline())
    
if __name__ == '__main__':
    main(sys.argv)
    
