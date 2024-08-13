N = int(input())
M = int(input())
S = input()

target = ('IO' * N) + 'I'
count = 0

for i in range(len(target) - 1, len(S)):

    if S[i] != 'I':
        continue
    
    if S[i - len(target) + 1:i + 1] == target:
        count += 1

print(count)