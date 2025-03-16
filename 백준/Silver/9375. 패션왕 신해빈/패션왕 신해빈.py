import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    wear_dict = dict()

    for _ in range(N):
        wear_name, wear_type = input().rstrip().split()

        if wear_type not in wear_dict:
            wear_dict[wear_type] = {}
        
        wear_dict[wear_type][wear_name] = 1
    
    count_list = [len(v) for v in wear_dict.values()]
    total = 1

    for count in count_list:
        total *= count + 1
    
    print(total - 1)