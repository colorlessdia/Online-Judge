import sys

input = sys.stdin.readline

N, C = map(int, input().split())

play_time = 0

for i in range(1, N + 1):
    MM, SS = map(int, input().split(':'))
    sec = (MM * 60) + SS

    play_time += sec

    if 0 < i < N:
        play_time -= C

H = play_time // 3600
M = (play_time % 3600) // 60
S = (play_time % 3600) % 60
H, M, S = map(lambda x: str(x).zfill(2), [H, M, S])

print(f'{H}:{M}:{S}')