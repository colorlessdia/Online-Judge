import sys

N = int(sys.stdin.readline())

fee_list = [0] * N
jinju_fee = 0

for i in range(N):
    D, C = sys.stdin.readline().rstrip().split()

    fee = int(C)

    if D == 'jinju':
        jinju_fee  = fee
    
    fee_list[i] = fee

count = 0

for fee in fee_list:
    if jinju_fee < fee:
        count += 1

print(jinju_fee)
print(count)