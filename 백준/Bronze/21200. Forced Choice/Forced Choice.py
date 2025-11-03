import sys

input = sys.stdin.readline

N, P, S = map(int, input().split())

for _ in range(S):
    card_list = list(map(int, input().split()))[1:]

    if P in card_list:
        print('KEEP')
    else:
        print('REMOVE')