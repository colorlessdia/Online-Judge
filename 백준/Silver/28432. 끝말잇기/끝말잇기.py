import sys

N = int(sys.stdin.readline())

word_history = [0] * N

target_index = 0
first_char = ''
last_char = ''

for i in range(N):
    word = sys.stdin.readline().rstrip()

    word_history[i] = word

    if word == '?':
        target_index = i

if 0 <= target_index - 1:
    first_char = word_history[target_index - 1][-1]

if target_index + 1 < len(word_history):
    last_char = word_history[target_index + 1][0]

M = int(sys.stdin.readline())

for _ in range(M):
    candidate_char = sys.stdin.readline().rstrip()

    if first_char != '' and first_char != candidate_char[0]:
        continue
    
    if last_char != '' and last_char != candidate_char[-1]:
        continue
    
    if candidate_char in word_history:
        continue
    
    print(candidate_char)