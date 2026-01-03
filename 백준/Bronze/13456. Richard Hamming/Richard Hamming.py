import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    V_sequence = map(int, input().split())
    U_sequence = map(int, input().split())

    distance = 0

    for V, U in zip(V_sequence, U_sequence):
        
        if V != U:
            distance += 1
    
    print(distance)