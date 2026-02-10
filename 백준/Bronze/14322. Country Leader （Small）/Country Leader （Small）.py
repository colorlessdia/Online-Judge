import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    leader_candidates = []

    for _ in range(N):
        S = input().rstrip()
        L = len(set(s for s in S if s.isalpha()))

        leader_candidates.append((L, S))
    
    leader_candidates.sort(key=lambda x: (-x[0], x[1]))
    leader = leader_candidates[0][1]
    
    print(f'Case #{t}: {leader}')