import sys

N = int(input())

for i in range(1, N + 1):
    G = int(sys.stdin.readline())
    C = map(int, sys.stdin.readline().split())

    invite_code_dict = dict()

    for code in C:
        if code in invite_code_dict:
            invite_code_dict[code] += 1
        else:
            invite_code_dict[code] = 1

    for k, v in invite_code_dict.items():
        if v == 1:
            print(f'Case #{i}: {k}')