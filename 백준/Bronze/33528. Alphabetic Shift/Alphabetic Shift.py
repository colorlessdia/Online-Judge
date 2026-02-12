S = input()

uppercase = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

for i in range(26):
    temp = []

    for s in S:
        j = (ord(s) - ord('A') - i) % 26
        temp.append(uppercase[j])
    
    print(''.join(temp))