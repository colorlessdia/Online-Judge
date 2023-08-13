import sys

for _ in range(int(input())):
    s = sys.stdin.readline().rstrip().split()

    new_string = ''

    for ss in s:
        new_string += ss[::-1] + ' '
    
    print(new_string[:-1])