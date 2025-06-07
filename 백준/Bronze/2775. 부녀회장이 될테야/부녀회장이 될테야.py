import sys

input = sys.stdin.readline

T = int(input())

test_case_list = [[0, 0] for _ in range(T)]
maximum_floor = 0

for t in range(T):
    K = int(input())
    N = int(input())

    test_case_list[t][0] = K
    test_case_list[t][1] = N

    if maximum_floor < K:
        maximum_floor = K

floor_list = [[0 for _ in range(14)] for _ in range(maximum_floor + 1)]

for i in range(maximum_floor + 1):
    
    for j in range(14):
        
        if i == 0:
            floor_list[i][j] = j + 1
            continue
        
        if j == 0:
            floor_list[i][j] = 1
            continue
        
        floor_list[i][j] = floor_list[i][j - 1] + floor_list[i - 1][j]
    
for test_case in test_case_list:
    floor, room = test_case
    room -= 1

    print(floor_list[floor][room])