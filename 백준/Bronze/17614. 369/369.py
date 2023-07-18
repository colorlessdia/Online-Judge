cnt = 0

for i in range(1, int(input()) + 1):
    if '3' in str(i):
        cnt += str(i).count('3')
    if '6' in str(i):
        cnt += str(i).count('6')
    if '9' in str(i):
        cnt += str(i).count('9')

print(cnt)