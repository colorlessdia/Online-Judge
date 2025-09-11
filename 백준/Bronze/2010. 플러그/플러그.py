import sys

input = sys.stdin.readline

N = int(input())

outlet = 1

for _ in range(N):
    plug = int(input())

    outlet -= 1
    outlet += plug

print(outlet)