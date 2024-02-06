import sys

n = int(input())

for _ in range(n):
    name = sys.stdin.readline().rstrip()

    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0

    for char in name:
        if char in vowel_list:
            vowel_count += 1
        else:
            consonant_count += 1

    print(name)
    
    if consonant_count < vowel_count:
        print(1)
    else:
        print(0)