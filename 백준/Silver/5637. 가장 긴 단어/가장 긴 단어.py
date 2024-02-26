import sys

max_length = 0
max_length_word = ''

while True:
    line = sys.stdin.readline().rstrip().split()

    for word in line:
        word_length = 0
        formatted_word = ''
        
        for char in word:
            if char.isalpha() or char == '-':
                word_length += 1
                formatted_word += char
        
        if max_length < word_length:
            max_length = word_length
            max_length_word = formatted_word

    if 'E-N-D' in line:
        break

print(max_length_word.lower())