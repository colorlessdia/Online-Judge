import sys
from math import ceil, floor

def formatted_height(h):
    feet, inch = divmod(h, 12)

    return f'{feet}\'{inch}"'

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    gender, mother_height, father_height = input().rstrip().split()
    mf, mi = map(int, mother_height[:-1].split("'"))
    ff, fi = map(int, father_height[:-1].split("'"))

    height = ((mf * 12) + mi) + ((ff * 12) + fi)
    
    if gender == 'B':
        height += 5
    else:
        height -= 5
    
    height /= 2
    min_height = formatted_height(ceil(height - 4))
    max_height = formatted_height(floor(height + 4))

    print(f'Case #{t}: {min_height} to {max_height}')