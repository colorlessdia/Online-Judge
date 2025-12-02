N = int(input())
S = input()

count = 0
char_list = list(S)

for i in range(N // 2):
    L = i
    R = N - i - 1

    if S[L] != S[R]:
        count += 1

    char = min(S[L], S[R])

    char_list[L] = char
    char_list[R] = char

palindroom = ''.join(char_list)

print(count)
print(palindroom)