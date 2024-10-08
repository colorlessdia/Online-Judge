import sys

ciphertext = sys.stdin.readline().rstrip()

N = int(sys.stdin.readline())

word_list = [sys.stdin.readline().rstrip() for _ in range(N)]

for i in range(26):
    temp = ''

    for char in ciphertext:
        ascii_code = ((ord(char) + i) % ord('z')) + 1
        
        if ascii_code < ord('a'):
            ascii_code += ord('a') - 1

        temp += chr(ascii_code)
    
    for word in word_list:

        if word in temp:
            print(temp)
            break