n = int(input())
move_list = list(map(int, input().split()))

if 0 == sum(move_list):
    print('Stay')
elif 0 < sum(move_list):
    print('Right')
elif sum(move_list) < 0:
    print('Left')