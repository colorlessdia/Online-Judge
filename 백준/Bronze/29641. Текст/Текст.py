N = int(input())
S = input().split()

text_list = []
temp = []
count = 0

for s in S:
    length = len(s)

    if not temp:
        temp.append(s)
        count += length
        continue

    if (count + length + 1) <= N:
        temp.append(s)
        count += (length + 1)
        continue

    text_list.append(' '.join(temp))
    temp = [s]
    count = length

if temp:
    text_list.append(' '.join(temp))

for text in text_list:
    print(text)