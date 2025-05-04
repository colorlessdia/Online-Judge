import sys

input = sys.stdin.readline

M = int(input())

before_coordinates = {tuple(map(int, input().split())): 1 for _ in range(M)}

N = int(input())

distance_dict = dict()

for _ in range(N):
    ax, ay = map(int, input().split())

    for bx, by in before_coordinates.keys():
        cx, cy = ax - bx, ay - by

        if (cx, cy) not in distance_dict:
            distance_dict[(cx, cy)] = 0
        
        distance_dict[(cx, cy)] += 1

for k, v in distance_dict.items():
    
    if v != M:
        continue
    
    print(*k)
    break