import sys

input = sys.stdin.readline

N = int(input())

reservation_history = dict()
minmax_history = dict()

for _ in range(N):
    name, place, start_time, end_time = input().rstrip().split()
    start_time, end_time = int(start_time), int(end_time)

    if name in reservation_history:
        continue
    
    reservation_history[name] = (place, (start_time, end_time))

    if place not in minmax_history:
        minmax_history[place] = [start_time, end_time]
        continue
    
    if start_time < minmax_history[place][0]:
        minmax_history[place][0] = start_time

    if minmax_history[place][1] < end_time:
        minmax_history[place][1] = end_time

time_table = {k: [0] * v[1] for k, v in minmax_history.items()}
maximum_number = 0

for place, time_range in reservation_history.values():
    
    for i in range(time_range[0], time_range[1]):
        time_table[place][i] += 1

        if maximum_number < time_table[place][i]:
            maximum_number = time_table[place][i]

place_list = []

for place, time_line in time_table.items():
    temp = [0, 0]
    
    for i in range(*minmax_history[place]):

        if time_line[i] == maximum_number:
            
            if temp[0] != 0:
                continue
            
            temp[0] = i
            continue
        
        if temp[0] != 0:
            temp[1] = i
            place_list.append([place, temp])
            temp = [0, 0]
    
    if temp[0] != 0:
        temp[1] = minmax_history[place][1]
        place_list.append([place, temp])

if len(place_list) == 1:
    print(place_list[0][0], *place_list[0][1])
else:
    sorted_place_list = sorted(place_list, key=lambda x: (x[0], x[1][0], x[1][1]))

    print(sorted_place_list[0][0], *sorted_place_list[0][1])