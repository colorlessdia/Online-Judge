import sys

mirror = [sys.stdin.readline().rstrip() for _ in range(int(input()))]

state = input()

if state == '1':
    for m in mirror:
        print(m)
elif state == '2':
    for m in mirror:
        print(m[::-1])
elif state == '3':
    for m in reversed(mirror):
        print(m)