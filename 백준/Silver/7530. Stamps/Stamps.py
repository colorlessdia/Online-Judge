import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    required_stamp, _ = map(int, input().split())
    stamp_list = sorted(map(int, input().split()), reverse=True)

    required_friend = 0
    count = 0

    for friend, stamp in enumerate(stamp_list, 1):
        count += stamp

        if required_stamp <= count:
            required_friend = friend
            break
    
    print(f'Scenario #{i}:')

    if 0 < required_friend:
        print(required_friend)
    else:
        print('impossible')

    if i != n:
        print()