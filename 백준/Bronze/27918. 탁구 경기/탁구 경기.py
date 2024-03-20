import sys

N = int(input())

winner_list = [sys.stdin.readline().rstrip() for _ in range(N)]

X, Y = 0, 0

for winner in winner_list:
    if winner == 'D':
        X += 1
    elif winner == 'P':
        Y += 1
    
    if 2 <= max(X, Y) - min(X, Y):
        break

print(f'{X}:{Y}')