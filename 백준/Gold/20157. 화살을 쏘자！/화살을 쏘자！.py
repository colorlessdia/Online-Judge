import sys

def GCD(A, B):
    
    if B == 0:
        return A
    
    return GCD(B, A % B)

input = sys.stdin.readline

N = int(input())

angle_dict = dict()

for _ in range(N):
    x, y = map(int, input().split())

    p, q = 0, 0

    if x == y == 0:
        continue
    elif x == 0 and 0 < y:
        p, q = 0, 1
    elif x == 0:
        p, q = 0, -1
    elif y == 0 and 0 < x:
        p, q = 1, 0
    elif y == 0:
        p, q = -1, 0
    else:
        B, A = sorted([abs(x), abs(y)])
        divisor = GCD(A, B)
        p, q = x // divisor, y // divisor

    if (p, q) not in angle_dict:
        angle_dict[(p, q)] = 1
        continue
    
    angle_dict[(p, q)] += 1

print(max(angle_dict.values()))