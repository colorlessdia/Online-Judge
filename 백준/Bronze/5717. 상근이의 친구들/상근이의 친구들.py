import sys

input = sys.stdin.readline

while 1:
    friend = sum(map(int, input().split()))

    if friend == 0:
        break
    
    print(friend)