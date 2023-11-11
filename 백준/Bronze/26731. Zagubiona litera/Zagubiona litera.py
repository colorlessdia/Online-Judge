n = input()
alpha = [0] * 26

for nn in n:
    idx = ord(nn) - ord('A')
    alpha[idx] += 1

target = alpha.index(0) + ord('A')

print(chr(target))