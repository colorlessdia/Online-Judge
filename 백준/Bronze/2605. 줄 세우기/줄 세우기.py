from collections import deque

n = int(input())
number_list = list(map(int, input().split()))

line = deque()

for i, number in enumerate(number_list, 1):
    temp = deque()

    for j in range(number):
        temp.appendleft(line.pop())
    
    line.append(i)

    if len(temp) != 0:
        line += temp

print(*line)