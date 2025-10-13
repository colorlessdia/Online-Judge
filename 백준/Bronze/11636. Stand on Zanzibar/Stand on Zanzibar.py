import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    number_list = list(map(int, input().split()))

    count = 0

    for i in range(1, len(number_list)):
        before = number_list[i - 1]
        current = number_list[i]
        difference = current - (before * 2)

        if 0 < difference:
            count += difference
    
    print(count)