import sys

input = sys.stdin.readline

N = int(input())

trash_list = [[] for _ in range(N)]

for i in range(N):
    line = input().rstrip()

    is_only = True
    trash_type = ''
    trash_length = len(line)

    for j in range(1, trash_length):
        
        if line[j - 1] != line[j]:
            is_only = False
            break

    if is_only:
        trash_type = line[0]
    
    trash_list[i] = (is_only, trash_type, trash_length)

P, C, V, S, G, F = map(int, input().split())
O = int(input())

matched_cost = dict(zip('PCVSGFO', [P, C, V, S, G, F, O]))
total_cost = 0

for i in range(N):
    is_only, trash_type, trash_length = trash_list[i]
    only_cost = trash_length * O

    if is_only:
        not_only_cost = trash_length * matched_cost[trash_type]
        total_cost += min(only_cost, not_only_cost)
    else:
        total_cost += only_cost

print(total_cost)