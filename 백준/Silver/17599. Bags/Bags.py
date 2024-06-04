n = int(input())
a = map(int, input().split())

count_dict = dict()

for id in a:
    if id in count_dict:
        count_dict[id] += 1
    else:
        count_dict[id] = 1

print(len(count_dict.keys()))