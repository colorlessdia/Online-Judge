import sys

input = sys.stdin.readline

N = int(input())

dance_rabbit_dict = {
    'ChongChong': 1
}

for _ in range(N):
    A, B = input().rstrip().split()
    
    if A in dance_rabbit_dict:
        dance_rabbit_dict[B] = 1
    
    if B in dance_rabbit_dict:
        dance_rabbit_dict[A] = 1

dancing_rabbit_count = len(dance_rabbit_dict.keys())

print(dancing_rabbit_count)