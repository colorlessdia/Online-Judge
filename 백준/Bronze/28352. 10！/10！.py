N = int(input())

week = 60 * 60 * 24 * 7
factorial = 1

for i in range(2, N + 1):
    factorial *= i

print(factorial // week)