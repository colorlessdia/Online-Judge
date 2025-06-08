A, B, V = map(int, input().split())

Q, R = divmod((V - A), (A - B))

if R == 0:
    print(Q + 1)
else:
    print(Q + 2)