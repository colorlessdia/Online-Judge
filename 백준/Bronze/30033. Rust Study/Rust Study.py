n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

for aa, bb in zip(a, b):
    if aa <= bb:
        cnt += 1

print(cnt)