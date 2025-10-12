import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = input().rstrip().split()

    char_count = dict()

    for b in B:

        if b not in char_count:
            char_count[b] = 0

        char_count[b] += 1

    C = ''.join(sorted(A))
    D = ''.join(sorted(char_count.keys()))

    if C == D:
        print('YES')
    else:
        print('NO')