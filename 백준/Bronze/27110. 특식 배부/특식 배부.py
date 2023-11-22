n = int(input())
p = map(int, input().split())

total = 0

for pp in p:
    if pp <= n:
        total += pp
    else:
        total += n

print(total)