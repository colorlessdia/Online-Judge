L = int(input())
S = input()

M = 1234567891

lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
matched_hash = dict(zip(lowercase, range(1, 26 + 1)))

hash_value = 0

for i in range(L):
    char = S[i]

    hash_value += (matched_hash[char] * (31 ** i)) % M

print(hash_value)