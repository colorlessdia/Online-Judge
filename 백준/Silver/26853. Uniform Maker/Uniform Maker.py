import sys

input = sys.stdin.readline

N, M = map(int, input().split())

char_count = [[0 for _ in range(26)] for _ in range(M)]

for _ in range(N):
    word = input().rstrip()

    for i in range(M):
        char_code = ord(word[i]) - 97

        char_count[i][char_code] += 1

total_count = 0

for count_list in char_count:
    max_count = max(count_list)

    total_count += (N - max_count)

print(total_count)