import sys

number_list = [0] + ([1] * 1000)

for i in range(2, int(1000 ** 0.5) + 1):
    
    if number_list[i] == 0:
        continue
    
    for j in range(i * 2, 1000 + 1, i):
        
        if number_list[j] != 0:
            number_list[j] = 0

is_first = True

while 1:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    N, C = map(int, line.split())

    prime_list = [str(k) for k in range(1, N + 1) if number_list[k] != 0]
    length = len(prime_list)
    
    is_half = 1 if length % 2 == 0 else 0
    
    center = length // 2
    left = center - C if is_half else center - C + 1
    right = center + C if is_half else center + C

    output_primes = ' '.join(prime_list[left:center] + prime_list[center:right])

    if not is_first:
        print()

    print(f'{N} {C}: {output_primes}')

    is_first = False