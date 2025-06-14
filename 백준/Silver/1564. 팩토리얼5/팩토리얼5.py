N = int(input())

factorial = 1
divisor = 10 ** 13

for i in range(1, N + 1):
    factorial *= i
    
    while factorial % 10 == 0:
        factorial //= 10

    factorial %= divisor
    
print(str(factorial)[-5:])