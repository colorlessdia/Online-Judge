K = int(input())
ciphertext = input()

table = []

for i in range(0, len(ciphertext), K * 2):
    if i + K <= len(ciphertext):
        table.append(ciphertext[i:i + K])

    if i + (K * 2) <= len(ciphertext):
        table.append(ciphertext[i + K:i + (K * 2)][::-1])

plaintext = ''

for j in range(K):
    for char in table:
        plaintext += char[j]

print(plaintext)