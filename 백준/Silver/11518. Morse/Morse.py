import sys

matched_morse = dict()

for _ in range(26):
    alphabat, morse = sys.stdin.readline().rstrip().split()

    matched_morse[alphabat] = morse

N = int(sys.stdin.readline())

matched_word = dict()

for i in range(N):
    word = sys.stdin.readline().rstrip()
    formatted_word = ''.join([matched_morse[char] for char in word])

    matched_word[formatted_word] = word

while True:
    W = int(sys.stdin.readline())

    if W == 0:
        break
    
    result = []
    is_include = True
    unmatced_morse = ''

    for _ in range(W):
        morse_code = sys.stdin.readline().rstrip()

        if morse_code in matched_word:
            result.append(matched_word[morse_code])
            continue
        
        if is_include:
            unmatced_morse = morse_code
            is_include = False
            continue
    
    if is_include:
        print(*result)
    else:
        print(f'{unmatced_morse} not in dictionary.')