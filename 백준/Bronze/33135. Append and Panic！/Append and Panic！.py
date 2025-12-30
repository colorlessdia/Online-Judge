S = sorted(input())

char_list = [S[0]]

for i in range(1, len(S)):
    char = S[i]

    if char == char_list[-1]:
        continue

    char_list.append(char)

length = len(S) - len(char_list)

print(length)