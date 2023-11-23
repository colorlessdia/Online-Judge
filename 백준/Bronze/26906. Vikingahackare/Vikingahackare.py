import sys

t = int(input())

matched_dict = dict()

for _ in range(t):
    v, k = sys.stdin.readline().rstrip().split()
    matched_dict[k] = v

s = input()

temp = ''
stone = ''

for i, ss in enumerate(s, 1):
    temp += ss
    
    if i % 4 == 0:
        if temp in matched_dict:
            stone += matched_dict[temp]
        else:
            stone += '?'

        temp = ''

print(stone)