import sys

input = sys.stdin.readline

N, M = map(int, input().split())

card_list = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    K = int(input())

    for i in range(N):
        front, back = card_list[i]

        if front <= K:
            card_list[i][0], card_list[i][1] = back, front
        
answer = sum([front for front, _ in card_list])

print(answer)