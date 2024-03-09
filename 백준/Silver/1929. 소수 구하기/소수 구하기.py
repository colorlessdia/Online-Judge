M, N = map(int, input().split())

number_list = [i for i in range(N + 1)]

for j in range(2, N + 1):
    
    for index, k in enumerate(range(j, N + 1, j)):
        if index == 0:
            continue
        
        if number_list[k] != 0:
            number_list[k] = 0

for prime in number_list[M:N + 1]:
    if prime != 0 and prime != 1:
        print(prime)