S = input()
K = 1

temp = S[0]

for s in S[1:]:
    if temp[-1] < s:
        temp += s
    else:
        K += 1
        temp = s

print(K)