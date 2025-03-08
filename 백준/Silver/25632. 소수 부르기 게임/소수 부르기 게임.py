maximum_number = 1000 + 1
number_list = [0, 0] + ([1] * (maximum_number - 2))

for i in range(2, int(maximum_number ** 0.5) + 1):
    
    if number_list[i] == 0:
        continue

    for j in range(i * 2, maximum_number, i):
        
        if number_list[j] != 0:
            number_list[j] = 0

A, B = map(int, input().split())
C, D = map(int, input().split())

yt_list = [k for k in range(A, B + 1) if number_list[k] != 0]
yj_list = [l for l in range(C, D + 1) if number_list[l] != 0]
common_list = list(set(yt_list).intersection(set(yj_list)))

winner = ''
turn = True

while 1:
    turn_name = 'yt' if turn else 'yj'

    if 0 < len(common_list):
        delete_item = common_list[-1]

        common_list.remove(delete_item)
        yj_list.remove(delete_item)
        yt_list.remove(delete_item)

        turn = not turn
        continue

    if turn_name == 'yt':
        
        if len(yt_list) == 0:
            winner = 'yj'
            break
        
        yt_list.remove(yt_list[-1])

    if turn_name == 'yj':
        
        if len(yj_list) == 0:
            winner = 'yt'
            break
        
        yj_list.remove(yj_list[-1])

    turn = not turn

print(winner)