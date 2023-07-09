n = int(input())
f = 1

for i in range(1, n + 1):
    f *= i

print(len(str(f)) - len(str(int(str(f)[::-1]))))