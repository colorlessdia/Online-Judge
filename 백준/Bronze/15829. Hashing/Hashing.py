L = int(input())
S = input()

M = 1234567891

lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
matched_hash = dict(zip(lowercase, range(1, 26 + 1)))

hash_value = 0

for i in range(L):
    H = matched_hash[S[i]] * (31 ** i)

    hash_value += H

print(hash_value % M)