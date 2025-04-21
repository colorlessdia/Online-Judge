import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())
A_sequence = map(int, input().split())
B_sequence = map(int, input().split())

total_score = 0
strategy_list = []

for A, B in zip(A_sequence, B_sequence):
    total_score += A

    heappush(strategy_list, (-B, -(100 - A)))

time = 24 * N

while 0 < time:
    
    if len(strategy_list) == 0:
        break
    
    B, A = map(lambda x: -x, heappop(strategy_list))
    
    if A == 0:
        continue

    Q, R = A // B, A % B

    if A // B <= time:
        total_score += Q * B
        time -= Q

        B = R if R < B else B

        heappush(strategy_list, (-B, -R))
    else:
        total_score += time * B
        time = 0

print(total_score)