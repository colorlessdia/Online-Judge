import sys

n, k = map(int, sys.stdin.readline().split())

money = [int(sys.stdin.readline()) for i in range(n)]
count = 0

for m in reversed(money):
    if m > k:
        continue

    count += (k // m)
    k %= m
    
print(count)