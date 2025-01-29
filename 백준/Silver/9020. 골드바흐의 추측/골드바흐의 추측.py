import sys

maximum_number = 10000 + 1
prime_list = [1] * (maximum_number)

for i in range(2, int(maximum_number ** 0.5) + 1):
    
    if i < 2:
        prime_list[i] = 0
        continue
    
    if prime_list[i] == 0:
        continue
    
    for j in range(i * 2, maximum_number, i):
        
        if prime_list[j] != 0:
            prime_list[j] = 0

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    half = n // 2

    if prime_list[half] == 1:
        print(half, half)
        continue
    
    for l in range(half - 1, 1, -1):
        
        if prime_list[l] != 0 and prime_list[n - l]:
            print(l, n - l)
            break