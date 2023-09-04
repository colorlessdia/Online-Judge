n = int(input())
want_list = list(map(int, input().split()))
want_dict = dict()

cnt = 0

for i in want_list:
    if i in want_dict:
        cnt += 1
    else:
        want_dict[i] = 1

print(cnt)