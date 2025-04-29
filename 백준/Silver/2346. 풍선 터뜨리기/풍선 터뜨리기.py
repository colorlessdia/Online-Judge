from collections import deque

N = int(input())
number_list = list(map(int, input().split()))

balloons = deque()

for i in range(1, N + 1):
    number = number_list[i - 1]

    balloons.append([i, number])

index_list = [0] * N

for j in range(1, N + 1):
    index, number = balloons.popleft()

    index_list[j - 1] = index

    if j == N:
        break

    if 0 <= number:
        
        for _ in range(number - 1):
            balloons.append(balloons.popleft())
    else:
        
        for _ in range(number * -1):
            balloons.appendleft(balloons.pop())

print(*index_list)