import sys

for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    is_time = 'No'
    is_date = 'No'

    if 0 <= x <= 23 and 0 <= y <= 59:
        is_time = 'Yes'
    
    if ((x in [1, 3, 5, 7, 8, 10, 12] and 1 <= y <= 31) or
        (x in [4, 6, 9, 11] and 1 <= y <= 30) or
        (x == 2 and 1 <= y <= 29)):
        is_date = 'Yes'

    print(is_time, is_date)