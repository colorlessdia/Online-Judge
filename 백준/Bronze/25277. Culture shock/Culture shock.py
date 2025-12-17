N = int(input())
S = input().split()

count = 0
word_set = set(['he', 'she', 'him', 'her'])

for word in S:
    
    if word in word_set:
        count += 1

print(count)