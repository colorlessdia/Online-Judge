N = int(input())
S = input()

lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
char_count_dict = dict(zip(lowercase, [0] * len(lowercase)))

for char in S:
    
    if char.isalpha():
        char_count_dict[char] += 1

maximum_count = max(char_count_dict.values())

print(maximum_count)