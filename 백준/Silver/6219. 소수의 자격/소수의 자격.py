A, B, D = input().split()
A, B = int(A), int(B)

prime_list = [0, 0] + [1] * (B - 1)

count = 0

for i in range(2, B + 1):

    if prime_list[i] == 0:
        continue
    
    if (A <= i <= B) and (D in str(i)):
        count += 1
    
    for j in range(i * 2, B + 1, i):
        
        if prime_list[j] != 0:
            prime_list[j] = 0

print(count)