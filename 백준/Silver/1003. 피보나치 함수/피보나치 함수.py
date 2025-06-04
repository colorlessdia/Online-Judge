import sys

def fibonacci(n):
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibonacci(n - 2) + fibonacci(n - 1)

input = sys.stdin.readline

count_list = [[1, 0], [0, 1]] + ([[0, 0] for _ in range(39)])

for i in range(2, 40 + 1):
    count_list[i][0] = count_list[i - 2][0] + count_list[i - 1][0]
    count_list[i][1] = count_list[i - 2][1] + count_list[i - 1][1]

T = int(input())

for _ in range(T):
    N = int(input())

    print(*count_list[N])