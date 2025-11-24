S = input()

count = 0
PER = ['P', 'E', 'R']

for i in range(len(S)):
    char = S[i]
    target = PER[i % 3]

    if char != target:
        count += 1

print(count)