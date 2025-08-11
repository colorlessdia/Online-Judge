from collections import deque

def BFS():
    queue = deque([(0, R1, C1)])
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[R1][C1] = True

    move_list = [
        ((-3, -2), (( -1, 0), (-2, -1))),
        ((-3, 2), (( -1, 0), (-2, 1))),
        ((-2, 3), (( 0, 1), (-1, 2))),
        ((2, 3), (( 0, 1), (1, 2))),
        ((3, 2), (( 1, 0), (2, 1))),
        ((3, -2), (( 1, 0), (2, -1))),
        ((2, -3), (( 0, -1), (1, -2))),
        ((-2, -3), (( 0, -1), (-1, -2))),
    ]

    while queue:
        count, y, x = queue.popleft()

        if y == R2 and x == C2:
            return count
        
        for (dy, dx), path_list in move_list:
            Y, X = y + dy, x + dx

            if not ((0 <= Y < R) and (0 <= X < C)):
                continue

            if visited[Y][X]:
                continue

            is_valid_path = True

            for py, px in path_list:
                PY, PX = y + py, x + px

                if PY == R2 and PX == C2:
                    is_valid_path = False
                    break
            
            if not is_valid_path:
                continue

            queue.append((count + 1, Y, X))
            visited[Y][X] = True
    
    return -1

R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())

R, C = 10, 9

print(BFS())