N = int(input())
S = input()

char_set = set()
char_count = {char: S.count(char) for char in S if char not in char_set}
char, count = sorted(char_count.items(), key=lambda x: -(x[1]))[0]

print(char, count)