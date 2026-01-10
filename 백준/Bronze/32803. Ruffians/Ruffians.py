import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    line_1 = list(map(int, input().split()))
    line_2 = list(map(int, input().split()))

    is_find = False

    for i in range(5):
        n1 = line_1[i]

        if is_find:
            break

        for j in range(5):
            n2 = line_2[j]

            if i == j:
                continue

            if n1 == n2:
                is_find = True
                break
    
    if is_find:
        print('YES')
    else:
        print('NO')