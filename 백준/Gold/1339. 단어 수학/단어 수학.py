N = int(input())

maximum_length = -1
word_count = dict()
char_count = dict()

for _ in range(N):
    word = input()
    length = len(word)

    word_count[word] = word_count.get(word, 0) + 1

    if maximum_length < length:
        maximum_length = length

    i = length

    for char in word:
        i -= 1
        
        if char not in char_count:
            char_count[char] = [0 for _ in range(8)]

        char_count[char][i] += 1

for k, v in char_count.items():
    char_count[k] = int(''.join(map(str, v[:maximum_length][::-1])))

sorted_char_count = sorted(char_count.items(), key=lambda x: -x[1])
filtered_keys = list(map(lambda x: x[0], sorted_char_count))
number_range = [j for j in range(9, -1, -1)]
matched_number = dict(zip(filtered_keys, number_range))

maximum_sum = 0

for k, v in word_count.items():
    maximum_sum += (int(''.join([str(matched_number[c]) for c in k])) * v)

print(maximum_sum)