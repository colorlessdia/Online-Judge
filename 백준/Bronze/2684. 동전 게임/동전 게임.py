import sys

P = int(input())

for _ in range(P):
    coin_sequence = sys.stdin.readline().rstrip()

    coin_sequence_case = [0] * 8

    for i in range(len(coin_sequence) - 2):
        sequence = coin_sequence[i:i + 3]

        if sequence == 'TTT':
            coin_sequence_case[0] += 1
        elif sequence == 'TTH':
            coin_sequence_case[1] += 1
        elif sequence == 'THT':
            coin_sequence_case[2] += 1
        elif sequence == 'THH':
            coin_sequence_case[3] += 1
        elif sequence == 'HTT':
            coin_sequence_case[4] += 1
        elif sequence == 'HTH':
            coin_sequence_case[5] += 1
        elif sequence == 'HHT':
            coin_sequence_case[6] += 1
        elif sequence == 'HHH':
            coin_sequence_case[7] += 1
    
    print(*coin_sequence_case)