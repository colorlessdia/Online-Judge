s = input()
cnt = 0

for i in range(len(s) - 3):
    if s[i:i + 4] == 'DKSH':
        cnt += 1

print(cnt)