import sys

yn = [0] * 5

for _ in range(int(input())):
    s = sys.stdin.readline().rstrip()

    for i, ss in enumerate(s):
        if ss == 'Y':
            yn[i] += 1

max_num = max(yn)
days = ''

for i, yynn in enumerate(yn, 1):
    if yynn == max_num:
        days += str(i) + ','

print(days[:-1])