import sys

input = sys.stdin.readline

fibonacci_list = [0, 1, 1] + ([0] * 42)

for i in range(2, 44 + 1):
    fibonacci = fibonacci_list[i - 2] + fibonacci_list[i - 1]
    fibonacci_list[i] = fibonacci

T = int(input())

for _ in range(T):
    N = int(input())

    number_list = []
    j = len(fibonacci_list)

    while 0 < N:
        j -= 1
        number = fibonacci_list[j]

        if N - number < 0:
            continue
        
        N -= number
        number_list.append(number)

    print(*reversed(number_list))