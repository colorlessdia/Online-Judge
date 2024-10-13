import sys

while True:
    date_key = sum(map(int, sys.stdin.readline().split()))

    if date_key == 0:
        break
    
    S = (date_key % 25) + 1

    ciphertext = sys.stdin.readline().rstrip()
    plaintext = ''

    for char in ciphertext:
        
        if not char.isalpha():
            plaintext += char
            continue

        char_code = ord(char) - S

        if char_code < ord('a'):
            char_code = ord('z') - (ord('a') % char_code) + 1
        
        plaintext += chr(char_code)
    
    print(plaintext)