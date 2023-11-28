a, b = map(int, input().split())
k, x = map(int, input().split())

friend = 0

for s in range(a, b + 1):
    if (k - x) <= s <= (k + x):
        friend += 1

print(friend) if friend != 0 else print('IMPOSSIBLE')