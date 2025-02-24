def calc_fee(time, unit_time, unit_fee):
    q = time // unit_time

    return (q + 1) * unit_fee

N = int(input())
time_sequence = map(int, input().split())

Y, M = 0, 0

for time in time_sequence:
    Y += calc_fee(time, 30, 10)
    M += calc_fee(time, 60, 15)

fee_name = 'Y' if Y < M else 'M'
fee = Y if Y <= M else M

if Y == M:
    fee_name = 'Y ' + fee_name

print(f'{fee_name} {fee}')