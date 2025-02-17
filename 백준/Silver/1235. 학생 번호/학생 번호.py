import sys

input = sys.stdin.readline

k = 1

N = int(input())
id_list = [input().rstrip() for _ in range(N)]

while 1:
    check_duplicate_id = dict()
    
    for id in id_list:
        part = id[-k:]

        if part not in check_duplicate_id:
            check_duplicate_id[part] = 1
            continue

        break
    
    if len(check_duplicate_id) == N:
        print(k)
        break
    
    k += 1