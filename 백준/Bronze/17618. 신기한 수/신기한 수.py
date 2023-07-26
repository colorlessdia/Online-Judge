n = int(input())

cnt = 0

for i in range(1, n + 1):
    if i % sum([int(c) for c in str(i)]) == 0:
        cnt += 1

print(cnt)