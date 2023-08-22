s = input()
p = input()

cnt_dict = dict()

for ss in s:
    if ss in cnt_dict:
        cnt_dict[ss] += 1
    else:
        cnt_dict[ss] = 1

for pp in p:
    if pp in cnt_dict:
        cnt_dict[pp] -= 1
    else:
        cnt_dict[pp] = -1

if min(cnt_dict.values()) < 0:
    print('NO')
else:
    print('YES')