N, M = map(int, input().split())

fibonacci = [0] * (M + 1)
fibonacci[1] = 1
fibonacci[2] = 1

for i in range(3, M + 1):
    fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 10

print(''.join(map(str, fibonacci[N:M + 1])))