import sys

cnt_dict = dict()
cnt_list = []

while 1:
    s = sys.stdin.readline().rstrip()
    
    if s == '0': break
    
    if s not in cnt_list:
        cnt_list.append(s)

    if s in cnt_dict:
        cnt_dict[s] += 1
    else:
        cnt_dict[s] = 1

for li in cnt_list:
    print(f'{li}: {cnt_dict[li]}')

total = sum(cnt_dict.values())

print(f'Grand Total: {total}')