from collections import deque

def BFS(a, b):
    queue = deque()
    queue.append([b, 1])
    visited = set()
    visited.add(b)

    while queue:
        current_number, count = queue.popleft()

        if current_number == a:
            return count
        
        if current_number % 2 == 0:
            next_number = current_number // 2

            if next_number not in visited:
                queue.append([next_number, count + 1])
                visited.add(next_number)
        
        if current_number % 10 == 1:
            next_number = (current_number - 1) // 10

            if next_number not in visited:
                queue.append([next_number, count + 1])
                visited.add(next_number)
    
    return -1

A, B = map(int, input().split())

print(BFS(A, B))