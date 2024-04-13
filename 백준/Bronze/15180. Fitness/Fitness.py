import sys

S = int(sys.stdin.readline())

index = S
visited_list = [index]

while True:
    plan = sys.stdin.readline().rstrip()

    if plan == '#':
        break
    
    direction, distance = plan[0], int(plan[1])

    if direction == 'A' and 0 < index - distance:
        index -= distance
    elif direction == 'A':
        index = 8 + index - distance
    elif direction == 'C' and index + distance <= 8:
        index += distance
    elif direction == 'C':
        index = index + distance - 8
    
    visited_list.append(index)

if len(visited_list) == len(set(visited_list)) and 5 <= len(visited_list):
    print(*visited_list)
else:
    print(*visited_list, 'reject')