def calc_difference(s1, s2):
    return sum([1 for c1, c2 in zip(s1, s2) if c1 != c2])

A, B = input().split()

minimum_difference = len(A)

for i in range(len(B) - len(A) + 1):
    part = B[i:i + len(A)]
    difference = calc_difference(A, part)

    if difference < minimum_difference:
        minimum_difference = difference

print(minimum_difference)