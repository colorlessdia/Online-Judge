N = input()

length = len(N)

count = 0

if length == 1:
    count = int(N)
else:
    for i in range(1, length):
        count += i * int('9'.ljust(i, '0'))

    count += (int(N) - int('1'.ljust(length, '0')) + 1) * length

print(count)