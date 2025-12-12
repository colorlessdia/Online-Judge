N, S = input().split()
N = int(N)

char_list = []
char_set = set()

for char in S:

    if char in char_set:
        continue

    char_list.append(char)
    char_set.add(char)

D = list(str(len(S) - len(char_set) + 4))
P = list(str(N + 1906))

SMUPC_NAME = ''.join(['smupc_'] + (P + char_list + D)[::-1])

print(SMUPC_NAME)