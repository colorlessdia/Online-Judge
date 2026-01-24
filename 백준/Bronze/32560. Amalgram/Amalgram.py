A = input()
B = input()

k = [chr(i) for i in range(ord('a'), ord('z') + 1)]
v = [0] * 26

A_count = dict(zip(k, v))
B_count = dict(zip(k, v))

for a in A:
    A_count[a] += 1

for b in B:
    B_count[b] += 1

char_list = []

for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    count = max(A_count[char], B_count[char])

    if count == 0:
        continue

    for _ in range(count):
        char_list.append(char)

print(''.join(char_list))