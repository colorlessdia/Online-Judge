import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ciphertext = sys.stdin.readline().rstrip()

    size = int(len(ciphertext) ** 0.5)

    plaintext = ''

    for i in range(size, 0, -1):
        j = i
        
        for _ in range(size):
            plaintext += ciphertext[j - 1]

            j += size
    
    print(plaintext)