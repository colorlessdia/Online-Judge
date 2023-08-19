k, w, m = map(int, input().split())

print((w - k) // m) if (w - k) % m == 0 else print(((w - k) // m) + 1)