from collections import deque

S = input()

station = deque()
sub_station = deque()
is_sub_station = False

for char in S:

    if char == '(':
        station.pop()
        is_sub_station = True
        continue
    
    if char == ')':
        is_sub_station = False
        continue
    
    if is_sub_station:
        sub_station.append(char)
    else:
        station.append(char)

station_name = ''.join(station)
sub_station_names = ''.join(sub_station) if len(sub_station) != 0 else '-'

print(station_name)
print(sub_station_names)