import sys

input = sys.stdin.readline

double_vowel_set = set(['aa', 'ee', 'ii', 'oo', 'uu', 'yy'])

while True:
    N = int(input())

    if N == 0:
        break

    double_vowel_word = None
    maximum_count = 0

    for _ in range(N):
        word = input().rstrip()

        if N == 1:
            double_vowel_word = word
            break

        count = 0

        for i in range(len(word) - 1):
            part = word[i:i + 2]

            if part in double_vowel_set:
                count += 1

        if maximum_count < count:
            double_vowel_word = word
            maximum_count = count

    print(double_vowel_word)