import sys

n = int(input())

matched_dict = dict()

for _ in range(n):
    before, after = sys.stdin.readline().rstrip().split()

    matched_dict[before] = after

formatted_string = ''

m = int(input())

for _ in range(m):
    char = sys.stdin.readline().rstrip()

    if char in matched_dict:
        formatted_string += matched_dict[char]
    else:
        formatted_string += char

print(formatted_string)