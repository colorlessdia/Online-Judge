import sys

L, N = map(int, sys.stdin.readline().split())

irregularity_word_dict = dict()

for _ in range(L):
    irregularity_word, plural = sys.stdin.readline().rstrip().split()

    irregularity_word_dict[irregularity_word] = plural

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if word in irregularity_word_dict:
        print(irregularity_word_dict[word])
    elif word[-2] not in ['a', 'e', 'i', 'o', 'u'] and word[-1] == 'y':
        print(word[:-1] + 'ies')
    elif word[-1] in ['o', 's', 'x'] or word[-2:] in ['ch', 'sh']:
        print(word + 'es')
    else:
        print(word + 's')