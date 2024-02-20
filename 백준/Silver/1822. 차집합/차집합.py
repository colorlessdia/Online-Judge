nA, nB = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

element_dict = dict()

for a in A:
    element_dict[a] = 1

for b in B:
    if b in element_dict:
        del element_dict[b]

element_count = len(element_dict)
sorted_dict_keys = sorted(element_dict.keys())

print(element_count)
print(*sorted_dict_keys)