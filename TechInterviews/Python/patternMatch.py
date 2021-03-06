import sys
import re

# Strip only the beginning and ending slashes
def stripSlashes(path):
    if path.startswith('/'):
        path = path[1:]
    if path.endswith('/'):
        path = path[:-1]
    return path

def findBestWildCardMatch(patterns):
    #The best match is wildcards that are rightmost
    #Get the positions of the * and add them to get the largest number to figure out which is rightmost
    patternsDict = {}
    for pattern in patterns:
        total = 0
        for m in re.finditer("\*", pattern):
            total = total + m.start()
        patternsDict[total] = pattern # {key:value} {total:pattern}
        
    return patternsDict[sorted(patternsDict.keys())[-1]]
    
def getRePattern(pattern):
    return pattern.replace(',', '/').replace('*', '[a-zA-Z0-9_]*')

def findBestMatch(patterns, paths):
    result = []
    temp = []
    for path in paths:
        temp.clear()
        for pattern in patterns:
            rePattern = getRePattern(pattern)
            if re.search(rePattern, stripSlashes(path)):
                temp.append(pattern)
        if len(temp) == 1:
            result.append(temp[0])
        elif len(temp) > 1:
            result.append(findBestWildCardMatch(temp))
        elif len(temp) == 0:
            result.append("NO MATCH FOUND")

    return result

# Example to call this program: python34 patternMatch.py <input_file> output_file
def main(args):
    input_file = open(args[1], 'r')
    output_file = open(args[2], 'w')

    pattern_list = []
    path_list = []

    # Expects correct format in file: int N followed by pattern lines then int M followed by path lines.
    N = int(input_file.readline())
    for j in range(N):
        pattern_list.append((input_file.readline()).strip())

    M = int(input_file.readline())
    for i in range(M):
        path_list.append((input_file.readline()).strip())

    print(findBestMatch(pattern_list, path_list))

    for result in findBestMatch(pattern_list, path_list):
        output_file.write(result + "\n")
        
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main(sys.argv)

