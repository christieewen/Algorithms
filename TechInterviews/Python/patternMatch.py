import sys
import re

def findBestWildCardMatch(patterns):
    pass

def getRePattern(pattern):
    return 'r'+'''+ re.sub(pattern, '\,', '/') + '''

def findBestMatch(patterns, paths):
    result = []
    temp = []
    for path in paths:
        temp.clear()
        for pattern in patterns:
            rePattern = getRePattern(pattern)
            if re.findall(rePattern, path):
                temp.append(pattern)
        if len(temp) > 1:
            result.append(findBestWildCardMatch(temp))
        elif len(temp) == 0:
            result.append("NO MATCH FOUND")

    return result

#['foot', 'fell', 'fastest']
# Example to call this program: python34 patternMatch.py <input_file> output_file
def main(args):
    input_file = open(args[1], 'r')
    output_file = open(args[2], 'w')

    pattern_list = []
    path_list = []

    # Expects correct format in file: int N followed by pattern lines then int M followed by path lines.
    N = int(input_file.readline())
    for j in range(N):
        pattern_list.append(input_file.readline())

    M = int(input_file.readline())
    for i in range(M):
        path_list.append(input_file.readline())

    print(findBestMatch(pattern_list, path_list))

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main(sys.argv)

