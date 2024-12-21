import sys

T = int(sys.stdin.readline())

factors = [9, 3, 7]

for t in range(1, T + 1):
    id = sys.stdin.readline().rstrip()

    i = 0
    unknown_index = 0
    factor = 0
    checksum = 0

    for j in range(1, len(id) + 1):
        
        if 2 < i:
            i = 0

        if id[-j] == '?':
            unknown_index = -j
            factor = factors[i]
        else:
            checksum += int(id[-j]) * factors[i]

        i += 1

    valid_id = list(id)

    for k in range(9 + 1):
        
        if (checksum + (k * factor)) % 10  == 0:
            valid_id[unknown_index] = str(k)
            break

    print(f'Scenario #{t}:')
    print(''.join(valid_id))

    if t < T:
        print()