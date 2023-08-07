s = input()
cnt_dict = dict()

for ss in s:
    if ss in cnt_dict:
        cnt_dict[ss] += 1
    else:
        cnt_dict[ss] = 1

if 2 < len(cnt_dict):
    sort_list = sorted(cnt_dict.items(), key=lambda x: x[1])
    diff = len(cnt_dict) - 2
    remove_cnt = 0

    for tpl in sort_list[:diff]:
        remove_cnt += tpl[1]
    
    print(remove_cnt)
else:
    print(0)