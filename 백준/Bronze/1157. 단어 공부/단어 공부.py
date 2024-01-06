import sys

s = sys.stdin.readline().rstrip()
count = dict()

for c in s:
    c = c.lower()
    if (c not in count.keys()):
        count[c] = 1
    else:
        count[c] += 1

count_list = [i for i in count.values()]
key_list = [j for j in count.keys()]
max_num = max(count_list)

if (count_list.count(max_num) >= 2):
    print('?')
else:
    print(key_list[count_list.index(max_num)].upper())