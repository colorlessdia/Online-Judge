def time_to_second(HH, MM):
    return (int(HH) * 60) + int(MM)

T1 = time_to_second(*input().split(':'))
T2 = time_to_second(*input().split(':'))

if T1 <= T2:
    print('YES')
else:
    print('NO')