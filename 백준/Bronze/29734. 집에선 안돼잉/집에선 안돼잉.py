N, M = map(int, input().split())
T, S = map(int, input().split())

Zip_time = ((N // 8) * 8) + ((N // 8) * S)

if N % 8 == 0:
    Zip_time -= S
else:
    Zip_time += N % 8

Dok_time = T + ((M // 8) * 8) + ((M // 8) * (S + (T * 2)))

if M % 8 == 0:
    Dok_time -= S + (T * 2)
else:
    Dok_time += M % 8

if Zip_time < Dok_time:
    print('Zip')
    print(Zip_time)
else:
    print('Dok')
    print(Dok_time)