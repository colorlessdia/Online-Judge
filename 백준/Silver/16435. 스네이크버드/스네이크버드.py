n, l = map(int, input().split())
fruit_list = sorted(map(int, input().split()))

for fruit in fruit_list:
    if fruit <= l:
        l += 1

print(l)