numbers = list(map(int, input().split()))

A = max(numbers)
B = min(numbers)

count = 0

while A != B:
    C = A - B

    A = max(C, B)
    B = min(C, B)

    count += 1

print(count)