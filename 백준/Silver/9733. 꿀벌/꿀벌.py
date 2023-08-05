import sys

action = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
cnt_dict = dict(zip(action, [0] * len(action)))
total = 0

while 1: 
    s = sys.stdin.readline().rstrip().split()
    total += len(s)

    if s == []: break

    for ss in s:
        if ss in cnt_dict:
            cnt_dict[ss] += 1

for act in action:
    print(f'{act} {cnt_dict[act]} {round(cnt_dict[act] / total, 2):.2f}')
print(f'Total {total} 1.00')