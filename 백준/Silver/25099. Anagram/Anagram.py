import sys

input = sys.stdin.readline

N = int(input())

anagram_history = dict()

for _ in range(N):
    word = input().rstrip()
    sorted_word = ''.join(sorted(word))

    if sorted_word in anagram_history:
        continue
    
    anagram_history[sorted_word] = 1
    
    print(word)