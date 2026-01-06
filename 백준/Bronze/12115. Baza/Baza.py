import sys

input = sys.stdin.readline

N, M = map(int, input().split())

number_list = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())

for _ in range(Q):
    query_list = list(map(int, input().split()))
    required_list = [(i, q) for i, q in enumerate(query_list) if q != -1]

    X = 0

    for li in number_list:
        is_valid = True

        for i, query in required_list:

            if li[i] != query:
                is_valid = False
                break
        
        if is_valid:
            X += 1
    
    print(X)