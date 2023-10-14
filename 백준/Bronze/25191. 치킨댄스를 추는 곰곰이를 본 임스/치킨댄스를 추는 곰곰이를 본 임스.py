n = int(input())
a, b = map(int, input().split())

a //= 2

c = a + b

print(c) if c <= n else print(n)