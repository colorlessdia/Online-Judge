import sys

input = sys.stdin.readline

while True:
    line = input().rstrip().split()

    if line[0] == '#':
        break

    word_list = []

    for word in line:

        if len(word) <= 3:
            word_list.append(word)
            continue

        formatted_word = word[0] + word[1:-1][::-1] + word[-1]
        word_list.append(formatted_word)
    
    print(' '.join(word_list))