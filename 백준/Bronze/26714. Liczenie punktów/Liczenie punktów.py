N = int(input())
test = input()

step = int(N / 10)

score = 0

for i in range(0, N, step):
    test_slice = test[i:i + step]
    
    if test_slice.count('N') == 0:
        score += 1

print(score)