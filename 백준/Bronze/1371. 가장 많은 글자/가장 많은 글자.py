import sys
from string import ascii_lowercase

cnt_alpha = dict(zip(ascii_lowercase, [0] * len(ascii_lowercase)))

s = sys.stdin.read().replace('\n', '').replace(' ', '')

for ss in s:
    cnt_alpha[ss] += 1

max_num = 0
max_list = []

for i in sorted(cnt_alpha.items(), key=lambda x: -x[1]):
    if max_num <= i[1]:
        max_num = i[1]
        max_list.append(i[0])
    else:
        break

print(''.join(max_list))