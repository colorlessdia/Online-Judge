from collections import deque

N, K = map(int, input().split())

circle = deque(range(1, N + 1))
josephus_permutation = deque()

i = 1

while 0 < len(circle):
    
    if i == K:
        josephus_permutation.append(str(circle.popleft()))
        i = 1
        continue

    circle.append(circle.popleft())
    
    i += 1

    if K < i:
        i = 1

print(f'<{", ".join(josephus_permutation)}>')