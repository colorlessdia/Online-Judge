a = int(input())
b = int(input())

cnt = 0

for i in range(a, b + 1):
    if 4 == len([j for j in range(1, i + 1) if i % j == 0]):
        cnt += 1

print(f'The number of RSA numbers between {a} and {b} is {cnt}')