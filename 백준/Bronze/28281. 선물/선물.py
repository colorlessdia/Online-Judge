n, x = map(int, input().split())
d = list(map(lambda p: int(p) * x, input().split()))

print(min([d[i] + d[i + 1] for i in range(len(d) - 1)]))