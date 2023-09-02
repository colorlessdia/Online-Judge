a = sorted(map(int, input().split()), reverse=True)
b = sorted(map(int, input().split()), reverse=True)

print(sum([aa * bb for aa, bb in zip(a, b)]))