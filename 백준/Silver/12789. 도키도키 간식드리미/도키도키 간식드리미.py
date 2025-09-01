from collections import deque

N = int(input())
line = deque(map(int, input().split()))

target = 1
waiting_line = deque()

while line:

    if waiting_line:

        while waiting_line:
            waiting_number = waiting_line.pop()
            
            if waiting_number == target:
                target += 1
                continue

            waiting_line.append(waiting_number)
            break

    number = line.popleft()

    if number == target:
        target += 1
        continue

    waiting_line.append(number)

while waiting_line:
    waiting_number = waiting_line.pop()

    if waiting_number == target:
        target += 1
        continue
    
    break

if N == target - 1:
    print('Nice')
else:
    print('Sad')