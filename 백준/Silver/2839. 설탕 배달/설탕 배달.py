N = int(input())
M = N // 5

minimum_count = None

for i in range(M, -1, -1):
    Q, R = divmod(N - (5 * i), 3)

    if R != 0:
        continue
    
    S = i + Q

    if (minimum_count == None) or (S < minimum_count):
        minimum_count = i + Q

if minimum_count:
    print(minimum_count)
else:
    print(-1)