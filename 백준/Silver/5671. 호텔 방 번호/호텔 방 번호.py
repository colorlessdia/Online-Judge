import sys

room_number = dict()

for i in range(1, 5000 + 1):
    number_count = [0] * 10

    is_valid = True

    for c in str(i):
        number_count[int(c)] += 1

        if 1 < number_count[int(c)]:
            is_valid = False
            break
    
    if is_valid:
        room_number[i] = i

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    N, M = map(int, line.split())

    count = 0

    for j in range(N, M + 1):
        
        if j in room_number:
            count += 1
    
    print(count)