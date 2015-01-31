
# Example to call this program: python33 patternMatch.py <input_file> output_file 
def main(args):
    input_file = open(args[1], 'r')
    output_file = open(args[2], 'w')
    N = input_file.readline()
    for N in input_file:
        input_file.readline()
    M = input_file.readline()
    for M in input_file:
        input_file.readline()
    

if __name__ == '__main__':
    main(sys.argv)
    
