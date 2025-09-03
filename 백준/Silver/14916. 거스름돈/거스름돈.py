N = int(input())

count = -1

for i in range(N // 5, -1, -1):
    r_5 = N - (i * 5)
    r_2 = r_5 % 2

    if r_2 == 0:
        q_2 = (N - (i * 5)) // 2
        count = i + q_2
        break

print(count)