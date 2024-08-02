from collections import deque

N, K = map(int, input().split())
permutation = deque(range(1, N + 1))
josephus_permutation = deque()

index = 1

while 0 < len(permutation):

    if index == K:
        josephus_permutation.append(permutation.popleft())
        index = 1
        continue
    
    permutation.append(permutation.popleft())

    index += 1

print(f'<{", ".join(map(str, josephus_permutation))}>')