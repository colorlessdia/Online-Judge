N = int(input())
line = input()

start_point = 0

sentence_list = []

for i, char in enumerate(line):
    if char in ['.', '?', '!']:
        sentence_list.append(line[start_point:i].split())

        start_point = i + 2

for sentence in sentence_list:
    count = 0
    
    for word in sentence:
        if word[0].isupper() and word.isalpha():
            count += 1

    print(count)