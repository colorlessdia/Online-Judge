s = []
for _ in range(5):
    n = int(input())
    s.append(40) if n < 40 else s.append(n)

print(sum(s) // 5)