a, b = sorted(input().split(), key=lambda x: len(x))

word = ''

for i in range(len(a)):
    if i % 2 == 0:
        word += a[i]
    else:
        word += b[i]

print(word)