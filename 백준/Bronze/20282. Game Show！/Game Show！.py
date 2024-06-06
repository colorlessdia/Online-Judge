import sys

C = int(sys.stdin.readline())

sbecs = 100
max_sbecs = sbecs

for _ in range(C):
    V = int(sys.stdin.readline())

    sbecs += V

    if max_sbecs < sbecs:
        max_sbecs = sbecs

print(max_sbecs)