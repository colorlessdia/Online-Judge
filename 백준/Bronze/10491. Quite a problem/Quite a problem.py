import sys

input = sys.stdin

for line in input:
    
    if 'problem' in line.rstrip().lower():
        print('yes')
    else:
        print('no')