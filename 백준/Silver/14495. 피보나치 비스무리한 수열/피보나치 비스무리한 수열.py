f = [0, 1, 1, 1]

for i in range(4, int(input()) + 1):
    f.append(f[i - 1] + f[i - 3])

print(f[-1])