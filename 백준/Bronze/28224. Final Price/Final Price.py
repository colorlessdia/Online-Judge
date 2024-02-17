import sys

n = int(input())

price = sum([int(sys.stdin.readline()) for _ in range(n)])

print(price)