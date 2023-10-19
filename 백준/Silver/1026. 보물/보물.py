n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), key=lambda x: -x)

total = 0

for aa, bb in zip(a, b):
    total += aa * bb

print(total)