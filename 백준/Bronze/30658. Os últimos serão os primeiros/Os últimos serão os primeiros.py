import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    rank_list = [int(sys.stdin.readline()) for _ in range(n)]
    reversed_rank = reversed(rank_list)

    for rank in reversed_rank:
        print(rank)
    
    print(0)