import sys

prime_list = []
number_list = [0] * (118 + 1)

for i in range(2, 118 + 1):
    
    if number_list[i] == 0:
        prime_list.append(i)

    for j in range(i, 118 + 1, i):
            
        if number_list[j] == 0:
            number_list[j] += 1

prime_count = len(prime_list)

N = int(sys.stdin.readline())

for _ in range(N):
    atomic_number = int(sys.stdin.readline())

    is_find = False

    for k in prime_list:
        
        if is_find:
            break
        
        for l in prime_list:
            
            if atomic_number == k + l:
                is_find = True
                break
            elif atomic_number < k + l:
                break

    if is_find:
        print('Yes')
    else:
        print('No')