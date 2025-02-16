def is_prime(number):
    
    for i in range(2, int(number ** 0.5) + 1):
        
        if number % i == 0:
            return False
    
    return True

a, b = map(int, input().split())

if 10 ** 7 < b:
    b = 10 ** 7

for j in range(a, b + 1):
    s = str(j)
    
    if s != s[::-1]:
        continue
    
    if is_prime(j):
        print(j)

print(-1)