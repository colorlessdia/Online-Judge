a, b = map(int, input().split())

for i in reversed(range(1, b + 1)):
    if i + 1 <= a:
        print((i * 2) + 1)
        break