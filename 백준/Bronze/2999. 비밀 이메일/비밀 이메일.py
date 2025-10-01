S = input()
L = len(S)

R = 0
C = 0

for i in range(int(L ** 0.5), 0, -1):

    if L % i == 0:
        R = i
        C = L // R
        break

message = []

for i in range(R):

    for j in range(C):
        index = (j * R) + i
        message.append(S[index])

print(''.join(message))