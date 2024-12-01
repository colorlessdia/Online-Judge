import sys

T = int(sys.stdin.readline())

for t in range(T):
    acronyms, n = sys.stdin.readline().rstrip().split()

    valid_line_list = []

    for _ in range(int(n)):
        line = sys.stdin.readline().rstrip()

        extracted_acronyms = ''.join([string[0] for string in line.split()])

        if acronyms == extracted_acronyms:
            valid_line_list.append(line)
    
    print(acronyms)
    
    for valid_line in valid_line_list:
        print(valid_line)