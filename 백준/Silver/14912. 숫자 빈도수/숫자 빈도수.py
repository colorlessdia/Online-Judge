n, d = input().split()

frequency = 0

for i in range(1, int(n) + 1):
    frequency += str(i).count(d)

print(frequency)