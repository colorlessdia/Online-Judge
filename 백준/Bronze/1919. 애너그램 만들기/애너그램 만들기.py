A = input()
B = input()

a_alphabat = [0] * 26
b_alphabat = [0] * 26

for a in A:
    ai = ord(a) - 97
    a_alphabat[ai] += 1

for b in B:
    bi = ord(b) - 97
    b_alphabat[bi] += 1

result = 0

for i in range(26):
    result += abs(a_alphabat[i] - b_alphabat[i])

print(result)