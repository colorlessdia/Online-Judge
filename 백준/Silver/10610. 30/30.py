N = input()

if '0' in N:
    sum_number = sum([int(n) for n in N])

    if sum_number % 3 == 0:
        max_number = int(''.join(sorted(N, reverse=True)))
        
        print(max_number)
    else:
        print(-1)
else:
    print(-1)