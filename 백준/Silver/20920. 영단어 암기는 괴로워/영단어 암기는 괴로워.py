import sys

N, M = map(int, sys.stdin.readline().split())

word_dict = dict()

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) < M:
        continue
    
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, count in sorted_word_dict:
    print(word)