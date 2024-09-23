import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().rstrip().split()

    formatted_string_list = []

    for string in line:
        
        if len(string) == 4:
            formatted_string_list.append('*' * 4)
            continue
        
        formatted_string_list.append(string)
    
    formatted_string = ' '.join(formatted_string_list)

    print(formatted_string)
    print()