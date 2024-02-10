import sys

T = int(input())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())

    friend_count = 0

    candy_list = list(map(int, sys.stdin.readline().split()))

    for candy in candy_list:
        friend_count += candy // K
    
    print(friend_count)