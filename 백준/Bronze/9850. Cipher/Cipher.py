ciphertext = input()

for i in range(26):
    plaintext = ''

    for char in ciphertext:
        
        if not char.isalpha():
            plaintext += char
            continue
        
        char_code = ord(char) + i

        if ord('Z') < char_code:
            char_code = ord('A') + (char_code % ord('Z')) - 1
        
        plaintext += chr(char_code)
    
    has_LIVE = False
    has_CHIPMUNKS = False

    for word in plaintext.split():
        
        if 'LIVE' in word:
            has_LIVE = True
            continue
        
        if 'CHIPMUNKS' in word:
            has_CHIPMUNKS = True
            continue

    if has_LIVE and has_CHIPMUNKS:
        print(plaintext)
        break